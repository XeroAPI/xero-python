# -*- coding: utf-8 -*-
from pathlib import Path

import pytest

from xero_python.api_client import ApiClient
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


def test_deserialize_file_keeps_download_within_temp_directory(api_client, tmp_path):
    path = deserialize_file(
        api_client, FakeResponse('attachment; filename="../outside.txt"')
    )

    assert path.parent == tmp_path
    assert path.name == "outside.txt"
    assert path.read_bytes() == b"file contents"
    assert not (tmp_path.parent / "outside.txt").exists()


def test_deserialize_file_uses_content_disposition_filename(api_client, tmp_path):
    path = deserialize_file(
        api_client, FakeResponse('attachment; filename="report.csv"')
    )

    assert path == tmp_path / "report.csv"
    assert path.read_bytes() == b"file contents"


def test_deserialize_file_uses_generated_filename_without_filename_parameter(
    api_client, tmp_path
):
    path = deserialize_file(api_client, FakeResponse("inline"))

    assert path.parent == tmp_path
    assert path.read_bytes() == b"file contents"
