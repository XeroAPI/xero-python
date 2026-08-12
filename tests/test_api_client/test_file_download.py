# -*- coding: utf-8 -*-
from pathlib import Path

import pytest

from xero_python.api_client import ApiClient
from xero_python.api_client import copy_download_without_overwrite
from xero_python.api_client.configuration import Configuration


class FakeResponse:
    def __init__(self, content_disposition, data=b"file contents"):
        self.content_disposition = content_disposition
        self.data = data

    def getheader(self, name):
        if name == "Content-Disposition":
            return self.content_disposition
        return None


@pytest.fixture
def api_client(tmp_path):
    configuration = Configuration()
    configuration.temp_folder_path = str(tmp_path)
    return ApiClient(configuration=configuration)


def deserialize_file(api_client, response):
    return Path(api_client._ApiClient__deserialize_file(response))


@pytest.mark.parametrize(
    "header",
    [
        'attachment; filename="../outside.txt"',
        'attachment; filename="..\\outside.txt"',
    ],
)
def test_deserialize_file_keeps_traversal_within_temp_directory(
    api_client, tmp_path, header
):
    path = deserialize_file(api_client, FakeResponse(header))

    assert path.parent == tmp_path
    assert path.name == "outside.txt"
    assert path.read_bytes() == b"file contents"
    assert not (tmp_path.parent / "outside.txt").exists()


@pytest.mark.parametrize(
    "header",
    [
        'attachment; filename="/outside.txt"',
        'attachment; filename="C:\\outside.txt"',
        'attachment; filename="\\\\server\\share\\outside.txt"',
        'attachment; filename="NUL.txt"',
        'attachment; filename="bad\x00name.txt"',
        'attachment; filename="spoof\u202ename.txt"',
        'attachment; filename="report.csv."',
    ],
)
def test_deserialize_file_rejects_unsafe_cross_platform_names(
    api_client, tmp_path, header
):
    path = deserialize_file(api_client, FakeResponse(header))

    assert path.parent == tmp_path
    assert path.name not in {
        "outside.txt",
        "NUL.txt",
        "bad\x00name.txt",
        "spoof\u202ename.txt",
        "report.csv.",
    }
    assert path.read_bytes() == b"file contents"


def test_deserialize_file_uses_content_disposition_filename(api_client, tmp_path):
    path = deserialize_file(
        api_client, FakeResponse('attachment; filename="report.csv"')
    )

    assert path == tmp_path / "report.csv"
    assert path.read_bytes() == b"file contents"


@pytest.mark.parametrize(
    "header,expected",
    [
        (
            "attachment; filename*=UTF-8''..%5Cencoded%20report.csv",
            "encoded report.csv",
        ),
        ('attachment; filename="quarter; report.csv"', "quarter; report.csv"),
    ],
)
def test_deserialize_file_parses_encoded_and_quoted_names(
    api_client, tmp_path, header, expected
):
    path = deserialize_file(api_client, FakeResponse(header))

    assert path == tmp_path / expected
    assert path.read_bytes() == b"file contents"


def test_deserialize_file_does_not_follow_existing_symlink(api_client, tmp_path):
    target = tmp_path.parent / "symlink-target.txt"
    target.write_bytes(b"do not overwrite")
    link = tmp_path / "report.csv"
    try:
        link.symlink_to(target)
    except OSError as error:
        pytest.skip("symlinks are unavailable: {}".format(error))

    path = deserialize_file(
        api_client, FakeResponse('attachment; filename="report.csv"')
    )

    assert path != link
    assert path.parent == tmp_path
    assert path.read_bytes() == b"file contents"
    assert link.is_symlink()
    assert target.read_bytes() == b"do not overwrite"


def test_deserialize_file_preserves_existing_regular_file(api_client, tmp_path):
    destination = tmp_path / "report.csv"
    destination.write_bytes(b"do not overwrite")

    path = deserialize_file(
        api_client, FakeResponse('attachment; filename="report.csv"')
    )

    assert path != destination
    assert path.parent == tmp_path
    assert path.read_bytes() == b"file contents"
    assert destination.read_bytes() == b"do not overwrite"


def test_copy_download_preserves_destination_created_after_validation(tmp_path):
    source = tmp_path / "secure-random-file"
    source.write_bytes(b"file contents")
    destination = tmp_path / "report.csv"

    destination.write_bytes(b"created by racer")
    copied = copy_download_without_overwrite(str(source), str(destination))

    assert not copied
    assert source.read_bytes() == b"file contents"
    assert destination.read_bytes() == b"created by racer"


def test_copy_download_preserves_replacement_when_atomic_claim_fails(
    tmp_path, monkeypatch
):
    source = tmp_path / "secure-random-file"
    source.write_bytes(b"file contents")
    destination = tmp_path / "report.csv"

    def replace_name_and_fail(source_path, destination_path, follow_symlinks):
        Path(destination_path).write_bytes(b"created by racer")
        raise OSError("injected atomic-claim failure")

    monkeypatch.setattr("xero_python.api_client.os.link", replace_name_and_fail)

    copied = copy_download_without_overwrite(str(source), str(destination))

    assert not copied
    assert source.read_bytes() == b"file contents"
    assert destination.read_bytes() == b"created by racer"


@pytest.mark.parametrize(
    "header",
    [
        'attachment; filename="unterminated',
        "attachment; filename*=UTF-8''bad%ZZname",
    ],
)
def test_deserialize_file_handles_malformed_content_disposition_safely(
    api_client, tmp_path, header
):
    path = deserialize_file(api_client, FakeResponse(header))

    assert path.parent == tmp_path
    assert path.read_bytes() == b"file contents"


def test_deserialize_file_uses_generated_filename_without_filename_parameter(
    api_client, tmp_path
):
    path = deserialize_file(api_client, FakeResponse("inline"))

    assert path.parent == tmp_path
    assert path.read_bytes() == b"file contents"
