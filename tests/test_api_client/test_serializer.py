# -*- coding: utf-8 -*-
from contextlib import contextmanager
from datetime import date, datetime, timedelta
from decimal import Decimal
from unittest import mock

import pytest
from dateutil import tz

from xero_python.api_client.deserializer import deserialize
from xero_python.api_client.serializer import (
    data_type,
    local_timezone,
    naive_to_utc,
    serialize,
    serialize_routing,
    serialize_dict,
    serialize_pass_through,
    serialize_list,
    serialize_tuple,
    serialize_float,
    serialize_datetime_ms,
    serialize_datetime,
    serialize_date_ms,
    serialize_base_model,
    serialize_enum_model,
)
from xero_python.models import BaseModel
from .test_deserializer import Shape


@contextmanager
def mock_serialize(name="serialize", side_effect=None):
    def sub_response(value, explicit_type=None):
        return value

    with mock.patch(
        "xero_python.api_client.serializer.{}".format(name),
        side_effect=side_effect or sub_response,
    ) as serialize:
        yield serialize


# data_type tests
@pytest.mark.parametrize(
    "value,explicit_type,expected",
    [
        ("value", None, "str"),
        (1, None, "int"),
        (True, None, "bool"),
        (1.0, None, "float"),
        (date.today(), None, "date"),
        (date.today(), "date[ms-format]", "date[ms-format]"),
        (datetime.today(), None, "datetime"),
        (datetime.today(), "datetime[ms-format]", "datetime[ms-format]"),
        (BaseModel(), None, "BaseModel"),
    ],
)
def test_data_type(value, explicit_type, expected):
    # given value and optional explicit data type
    # when finding serialize data type
    value_type = data_type(value, explicit_type)
    # then value_type to be as expected
    assert value_type == expected


# serialize_routing tests
@pytest.mark.parametrize(
    "value,explicit_type",
    [
        ("value", None),
        (1, None),
        (True, None),
        (1.0, None),
        (date.today(), None),
        (date.today(), "date[ms-format]"),
        (datetime.today(), None),
        (datetime.today(), "datetime[ms-format]"),
        (BaseModel(), None),
    ],
)
def test_serialize_routing(value, explicit_type):
    # when serialize test user
    def sub_response(value, explicit_type):
        return str(value)

    with mock_serialize("data_type", side_effect=sub_response) as data_type:
        key = serialize_routing(value, explicit_type)

    # then expect data_type called
    data_type.assert_called_once_with(value, explicit_type)
    # then expected result to returned from data_type()
    assert key == str(value)


@pytest.mark.parametrize(
    "value,explicit_type",
    [(dict(), None), (None, "dict"), (None, "dict[str]"), (None, "dict[User]")],
)
def test_serialize_routing_dict(value, explicit_type):
    # given dict value or explicit type
    # when finding serialize routing key
    key = serialize_routing(value, explicit_type)
    # then expected key to be 'dict'
    assert key == "dict"


@pytest.mark.parametrize(
    "value,explicit_type",
    [([], None), (None, "list"), (None, "list[str]"), (None, "list[User]")],
)
def test_serialize_routing_list(value, explicit_type):
    # given list value or explicit type
    # when finding serialize routing key
    key = serialize_routing(value, explicit_type)
    # then expected key to be 'list'
    assert key == "list"


@pytest.mark.parametrize(
    "value,explicit_type",
    [(tuple(), None), (None, "tuple"), (None, "tuple[str]"), (None, "tuple[User]")],
)
def test_serialize_routing_tuple(value, explicit_type):
    # given tuple value or explicit type
    # when finding serialize routing key
    key = serialize_routing(value, explicit_type)
    # then expected key to be 'tuple'
    assert key == "tuple"


# serialize tests
def test_serialize():
    # given default serialize function
    default_serialize = serialize.registry[""]  # get default implementation

    class User(BaseModel):
        """
        test api model
        """

    value = User()
    # when serialize test user
    with mock_serialize("serialize_model") as serialize_model:
        result = default_serialize(value)

    # then expect serialize_model called
    serialize_model.assert_called_once_with(value)
    # then expected result to returned from serialize_model()
    assert result is value


@pytest.mark.parametrize(
    "value,explicit_type", [(None, "User"), (BaseModel(), "UserModel")]
)
def test_serialize_non_model(value, explicit_type):
    # given default serialize function
    default_serialize = serialize.registry[""]  # get default implementation
    # when serialize non model value, ValueError expected
    with pytest.raises(ValueError):
        default_serialize(value, explicit_type)


# serialize_dict tests
@pytest.mark.parametrize(
    "value,explicit_type,sub_type",
    [
        ({}, None, None),
        ({"key": "value", "key2": ""}, "dict", None),
        ({"key": "1"}, "dict[int]", "int"),
    ],
)
def test_serialize_dict(value, explicit_type, sub_type):
    # given dict value
    # when serialize dict of items
    with mock_serialize() as serialize:
        result = serialize_dict(value, explicit_type)
    # then expected json serializable dict result
    assert isinstance(result, dict)
    assert len(result) == len(value)
    assert result == value
    for sub_value in value.values():
        serialize.assert_any_call(sub_value, sub_type)


def test_serialize_dict_sub_type_error():
    # given invalid sub type key
    explicit_type = "dict[number"
    value = {"key": "1"}
    # when deserialize dict of items
    with pytest.raises(ValueError):
        serialize_dict(value, explicit_type)


# serialize_list tests
@pytest.mark.parametrize(
    "value,explicit_type,sub_type",
    [
        ([], None, None),
        (["value", "val2", ""], "list", None),
        (["0", "1"], "list[int]", "int"),
    ],
)
def test_serialize_list(value, explicit_type, sub_type):
    # given list value
    # when serialize list of items
    with mock_serialize() as serialize:
        result = serialize_list(value, explicit_type)
    # then expected json serializable list result
    assert isinstance(result, list)
    assert len(result) == len(value)
    assert result == value
    for sub_value in value:
        serialize.assert_any_call(sub_value, sub_type)


def test_serialize_list_sub_type_error():
    # given invalid sub type key
    explicit_type = "list[number"
    value = ["key", "1"]
    # when deserialize list of items
    with pytest.raises(ValueError):
        serialize_list(value, explicit_type)


# serialize_tuple tests
@pytest.mark.parametrize(
    "value,explicit_type,sub_type",
    [
        (tuple(), None, None),
        (("value", "val2", ""), "tuple", None),
        (("0", "1"), "tuple[int]", "int"),
    ],
)
def test_serialize_tuple(value, explicit_type, sub_type):
    # given tuple value
    # when serialize tuple of items
    with mock_serialize() as serialize:
        result = serialize_tuple(value, explicit_type)
    # then expected json serializable tuple result
    assert isinstance(result, tuple)
    assert len(result) == len(value)
    assert result == value
    for sub_value in value:
        serialize.assert_any_call(sub_value, sub_type)


def test_serialize_tuple_sub_type_error():
    # given invalid sub type key
    explicit_type = "tuple[number"
    value = ("key", "1")
    # when deserialize tuple of items
    with pytest.raises(ValueError):
        serialize_tuple(value, explicit_type)


# serialize_pass_through tests
@pytest.mark.parametrize("value", ["string", True, -12])
def test_serialize_pass_through(value):
    # given json serializable value
    # when serialize_pass_through
    result = serialize_pass_through(value)
    # then expected result to be original value
    assert result is value


# serialize_float tests
@pytest.mark.parametrize("value", [0.0001, Decimal("0.1")])
def test_serialize_float(value):
    # given float or Decimal value
    # when serialize_float
    result = serialize_float(value)
    # then expected result to be 'float' value
    assert isinstance(result, float)
    assert result == float(value)


# serialize_datetime tests
@pytest.mark.parametrize(
    "value,expected",
    [
        (date(2020, 4, 3), "2020-04-03"),
        (date(2020, 2, 28), "2020-02-28"),
        (date(2019, 8, 1), "2019-08-01"),
        (datetime(2020, 4, 3, 5, 35, 6), "2020-04-03T05:35:06"),
        (datetime(2020, 2, 28, 11, 2, 54), "2020-02-28T11:02:54"),
        (datetime(2019, 12, 7, 18, 46, 19, 518784), "2019-12-07T18:46:19.518784"),
        (
            datetime(2019, 12, 10, 12, 59, 59, tzinfo=tz.UTC),
            "2019-12-10T12:59:59+00:00",
        ),
        (
            datetime(2019, 12, 7, 18, 46, 19, tzinfo=tz.gettz("Pacific/Auckland")),
            "2019-12-07T18:46:19+13:00",
        ),
    ],
)
def test_serialize_datetime(value, expected):
    # given date value
    # when serialize date or datetime
    result = serialize_datetime(value)
    # then expect result to ISO-8601 string
    assert isinstance(result, str)
    assert result == expected


# serialize_datetime_ms tests
@pytest.mark.parametrize(
    "value,expected",
    [
        (datetime.fromtimestamp(0.0), "/Date(0)/"),
        (datetime(1960, 1, 1, tzinfo=tz.UTC), "/Date(-315619200000+0000)/"),
        (datetime.fromtimestamp(1439424000.0), "/Date(1439424000000)/"),
        (datetime.fromtimestamp(1439434356.790), "/Date(1439434356790)/"),
        (datetime(2015, 8, 13, tzinfo=tz.UTC), "/Date(1439424000000+0000)/"),
        (
            datetime(2016, 10, 13, 20, 13, 36, 437000, tzinfo=tz.UTC),
            "/Date(1476389616437+0000)/",
        ),
        (
            datetime(
                2016,
                10,
                14,
                9,
                13,
                36,
                437000,
                tzinfo=tz.tzoffset(None, timedelta(hours=13)),
            ),
            "/Date(1476389616437+1300)/",
        ),
    ],
)
def test_serialize_datetime_ms(value, expected):
    # given datetime value
    # when serialize datetime
    result = serialize_datetime_ms(value)
    # then expect result to be date string in MS json format
    assert isinstance(result, str)
    assert result == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        # Sydney stayed on UTC+10 all year round until 1971, so noon-thirty
        # local is 02:30 UTC. Applying today's daylight saving rule instead
        # would place it an hour earlier, at 01:30 UTC.
        (datetime(1960, 1, 1, 12, 30), datetime(1960, 1, 1, 2, 30, tzinfo=tz.UTC)),
        # By 1990 daylight saving was in force each January, so UTC+11 applies.
        (datetime(1990, 1, 1, 12, 30), datetime(1990, 1, 1, 1, 30, tzinfo=tz.UTC)),
    ],
)
def test_naive_to_utc_uses_historical_offsets_of_a_fixed_timezone(
    monkeypatch, value, expected
):
    monkeypatch.setattr(
        "xero_python.api_client.serializer.local_timezone",
        lambda: tz.gettz("Australia/Sydney"),
    )

    assert naive_to_utc(value) == expected


def test_local_timezone_agrees_with_the_tz_database_before_the_epoch():
    zone_name = pytest.importorskip("tzlocal").get_localzone_name()
    historical_zone = tz.gettz(zone_name)
    if historical_zone is None:
        pytest.skip("no tz database entry for {}".format(zone_name))
    value = datetime(1960, 1, 1, 12, 30)

    assert (
        value.replace(tzinfo=local_timezone()).utcoffset()
        == value.replace(tzinfo=historical_zone).utcoffset()
    )


@pytest.mark.parametrize(
    "value",
    [
        datetime(1971, 1, 1, 12, 30),
        datetime(2015, 8, 13, 12, 30),
        datetime(2024, 4, 7, 2, 30, fold=0),
        datetime(2024, 4, 7, 2, 30, fold=1),
        datetime(2024, 10, 6, 2, 30, fold=0),
        datetime(2024, 10, 6, 2, 30, fold=1),
    ],
)
def test_serialize_naive_datetime_ms_preserves_platform_timestamp_semantics(value):
    expected_ms = int(value.timestamp() * 1000)

    assert serialize_datetime_ms(value) == "/Date({})/".format(expected_ms)


@pytest.mark.parametrize(
    "value,expected",
    [
        # Float seconds truncate towards zero, so these lose the final
        # millisecond and the error changes sign either side of the epoch.
        (
            datetime(1901, 11, 4, 12, 50, 45, 768000, tzinfo=tz.UTC),
            "/Date(-2150881754232+0000)/",
        ),
        (
            datetime(1935, 5, 6, 15, 50, 10, 433000, tzinfo=tz.UTC),
            "/Date(-1093680589567+0000)/",
        ),
        (
            datetime(2004, 5, 29, 20, 46, 5, 715000, tzinfo=tz.UTC),
            "/Date(1085863565715+0000)/",
        ),
    ],
)
def test_serialize_datetime_ms_keeps_exact_milliseconds(value, expected):
    assert serialize_datetime_ms(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        datetime(1900, 1, 1, tzinfo=tz.UTC),
        datetime(1901, 11, 4, 12, 50, 45, 768000, tzinfo=tz.UTC),
        datetime(1960, 1, 1, tzinfo=tz.UTC),
        datetime(1970, 1, 1, tzinfo=tz.UTC),
        datetime(2004, 5, 29, 20, 46, 5, 715000, tzinfo=tz.UTC),
        datetime(2016, 10, 13, 20, 13, 36, 437000, tzinfo=tz.UTC),
    ],
)
def test_datetime_ms_round_trips_through_deserialize(value):
    assert (
        deserialize("datetime[ms-format]", serialize_datetime_ms(value), None) == value
    )


# serialize_date_ms tests
@pytest.mark.parametrize(
    "value,expected",
    [
        (date(1970, 1, 1), "/Date(0)/"),
        (date(1980, 1, 2), "/Date(315619200000)/"),
        (date(2017, 11, 28), "/Date(1511827200000)/"),
        (date(2019, 2, 23), "/Date(1550880000000)/"),
    ],
)
def test_serialize_date_ms(value, expected):
    # given datetime value
    # when serialize date
    result = serialize_date_ms(value)
    # then expect result to be date string in MS json format
    assert isinstance(result, str)
    assert result == expected


def test_serialize_pre_epoch_date_ms_uses_utc_midnight():
    value = date(1960, 1, 1)
    utc_value = datetime.combine(value, datetime.min.time()).replace(tzinfo=tz.UTC)
    epoch = datetime(1970, 1, 1, tzinfo=tz.UTC)
    expected_ms = int((utc_value - epoch).total_seconds() * 1000)

    assert serialize_date_ms(value) == "/Date({})/".format(expected_ms)


# serialize_base_model tests
def test_serialize_base_model():
    # given test model
    class Model(BaseModel):
        openapi_types = {"value": "int", "description": "str"}
        attribute_map = {"value": "Value", "description": "Short"}

        def __init__(self, **kwargs):
            for name, value in kwargs.items():
                setattr(self, name, value)

    value = Model(value=132, description="short description")
    # when serialize model
    with mock_serialize() as serialize:
        result = serialize_base_model(value)
    # then expect result to dictionary
    assert isinstance(result, dict)
    assert result == {"Value": 132, "Short": "short description"}
    serialize.assert_any_call(132, "int")
    serialize.assert_any_call("short description", "str")


@pytest.mark.parametrize(
    "value,expected",
    [(Shape.SQUARE, "square"), (Shape.DIAMOND, "diamond"), (Shape.CIRCLE, "circle")],
)
def test_serialize_enum_model(value, expected):
    # given test enum model instance
    # when serialize model
    result = serialize_enum_model(value)
    # then correct enum value expected
    assert isinstance(result, str)
    assert result == expected
