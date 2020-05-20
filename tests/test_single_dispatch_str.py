# -*- coding: utf-8 -*-
import pytest

from xero_python.single_dispatch_str import single_dispatch_str


def test_single_dispatch_str():
    @single_dispatch_str
    def decoder(key, data):
        raise ValueError("can't decode {!r} no decoder found".format(key))

    @decoder.register("Connection")
    def _(key, data):
        return key

    def org_decoder(key, data):
        return data

    decoder.register("Organisation", org_decoder)

    @decoder.register("Identity")
    @decoder.register("User")
    @decoder.register("Person")
    def _(key, data):
        return key + data

    value = decoder("Connection", "1")
    assert value == "Connection"
    value = decoder("Organisation", "2")
    assert value == "2"
    with pytest.raises(ValueError):
        decoder("Account", "0")

    assert decoder("Identity", "") == "Identity"
    assert decoder("User", "2") == "User2"
    assert decoder("Person", " 3") == "Person 3"


def test_single_dispatch_str_empty_constructor():
    @single_dispatch_str()
    def parse(key, data):
        raise ValueError("can't parse {!r} no parser found".format(key))

    @parse.register("Connection")
    def _(key, data):
        return key

    def org_parser(key, data):
        return data

    parse.register("Organisation", org_parser)

    @parse.register("Identity")
    @parse.register("User")
    @parse.register("Person")
    def _(key, data):
        return key + data

    assert parse("Connection", "1") == "Connection"
    assert parse("Organisation", "2") == "2"
    with pytest.raises(ValueError):
        parse("Account", "0")

    assert parse("Identity", "") == "Identity"
    assert parse("User", "2") == "User2"
    assert parse("Person", " 3") == "Person 3"


def test_single_dispatch_str_key():
    def key_case_insensitive(key, data):
        return key.lower()

    @single_dispatch_str(key=key_case_insensitive)
    def saver(key, data):
        raise ValueError("can't save {!r} no saver found".format(key))

    @saver.register("connection")
    def _(key, data):
        return key

    def org_saver(key, data):
        return data

    saver.register("organisation", org_saver)

    @saver.register("identity")
    @saver.register("user")
    @saver.register("person")
    def _(key, data):
        return key + data

    assert saver("Connection", "1") == "Connection"
    assert saver("Organisation", "2") == "2"
    with pytest.raises(ValueError):
        saver("Account", "0")

    assert saver("Identity", "") == "Identity"
    assert saver("User", "2") == "User2"
    assert saver("Person", " 3") == "Person 3"
