# -*- coding: utf-8 -*-
from contextlib import contextmanager
from datetime import date, datetime, timedelta
from decimal import Decimal
from enum import Enum
from unittest import mock

import pytest
from dateutil import tz

from tests import FakeClass, FakeMethod
from xero_python.api_client.deserializer import (
    deserialize,
    deserialize_bool,
    deserialize_date,
    deserialize_date_ms,
    deserialize_datetime,
    deserialize_datetime_ms,
    deserialize_decimal,
    deserialize_int,
    deserialize_list,
    deserialize_model,
    deserialize_routing,
    deserialize_str,
)


@contextmanager
def mock_deserialize(name="deserialize"):
    def sub_response(key, value, model_finder):
        return value

    with mock.patch(
        "xero_python.api_client.deserializer.{}".format(name), side_effect=sub_response
    ) as deserialize:
        yield deserialize


# deserialize_routing tests
@pytest.mark.parametrize(
    "data_type", ["str", "int", "bool", "float", "date", "datetime", "User"]
)
def test_deserialize_routing(data_type):
    # given plain data type
    # when finding deserialize routing key
    key = deserialize_routing(data_type, data=None, model_finder=None)
    # then expected data_type to be key
    assert key == data_type


@pytest.mark.parametrize(
    "data_type", ["list[{}]".format(key) for key in ("str", "User")]
)
def test_deserialize_routing_list(data_type):
    # given list data type
    # when finding deserialize routing key
    key = deserialize_routing(data_type, data=None, model_finder=None)
    # then expected key to be 'list'
    assert key == "list"


# deserialize tests
def test_deserialize():
    # given default deserialize function
    default_deserialize = deserialize.registry[""]  # get default implementation
    data = {"field": "value"}

    class User:
        pass

    model_finder = FakeClass()
    model_finder.find_model = FakeMethod(return_value=User)
    # when finding deserialize routing key
    with mock_deserialize("deserialize_model") as deserialize_model:
        result = default_deserialize("User", data, model_finder)

    # then expect find_model called
    assert len(model_finder.find_model.calls) == 1
    call_args, call_kwargs = model_finder.find_model.calls[0]
    assert call_args == ("User",)
    assert call_kwargs == {}
    # then expect deserialize_mode called
    deserialize_model.assert_called_once_with(User, data, model_finder)
    # then expected result to returned from deserialize_model()
    assert result is data


# deserialize_list tests
def test_deserialize_list():
    # given proper data type
    data_type = "list[number]"
    data = (1, 2, 3, 4)
    model_finder = None
    # when deserialize list of items
    with mock_deserialize() as deserialize:
        result = deserialize_list(data_type, data, model_finder)
    # then expected deserialized list result
    assert isinstance(result, list)
    assert len(result) == len(data)
    assert result == list(data)
    deserialize.assert_has_calls([mock.call("number", i, None) for i in data])


def test_deserialize_list_key_error():
    # given invalid data type key
    data_type = "list[number"
    data = (1, 2, 3, 4)
    model_finder = None
    # when deserialize list of items
    with pytest.raises(ValueError):
        deserialize_list(data_type, data, model_finder)


# deserialize_int tests
@pytest.mark.parametrize("data,expected", [(n, int(n)) for n in ("1", "-1", 2)])
def test_deserialize_int(data, expected):
    # given data type int
    data_type = "int"
    # when deserialize integer
    result = deserialize_int(data_type, data, model_finder=None)
    # then expect result to be integer
    assert isinstance(result, int)
    assert result == expected


# deserialize_decimal tests
@pytest.mark.parametrize(
    "data,expected", [(n, Decimal(n)) for n in ("1.04", "-1.1", Decimal("0.032"))]
)
def test_deserialize_decimal(data, expected):
    # given data type float
    data_type = "float"
    # when deserialize decimal
    result = deserialize_decimal(data_type, data, model_finder=None)
    # then expect result to be Decimal
    assert isinstance(result, Decimal)
    assert result == expected


# deserialize_str tests
@pytest.mark.parametrize("data,expected", [(s, str(s)) for s in (1, True, "text")])
def test_deserialize_str(data, expected):
    # given data type string
    data_type = "str"
    # when deserialize string
    result = deserialize_str(data_type, data, model_finder=None)
    # then expect result to be string
    assert isinstance(result, str)
    assert result == expected


# deserialize_bool tests
@pytest.mark.parametrize("data,expected", [(True, True), (False, False)])
def test_deserialize_bool(data, expected):
    # given data type bool
    data_type = "bool"
    # when deserialize bool
    result = deserialize_bool(data_type, data, model_finder=None)
    # then expect result to be boolean
    assert isinstance(result, bool)
    assert result == expected


@pytest.mark.parametrize("data", [None, "", "1", "0", 1, 0])
def test_deserialize_bool_error(data):
    # given data type bool
    data_type = "bool"
    # when deserialize bool
    with pytest.raises(ValueError):
        deserialize_bool(data_type, data, model_finder=None)


# deserialize_date tests
@pytest.mark.parametrize(
    "data,expected",
    [
        ("2020-04-03", date(2020, 4, 3)),
        ("2020-02-28", date(2020, 2, 28)),
        ("2019-08-01", date(2019, 8, 1)),
    ],
)
def test_deserialize_date(data, expected):
    # given data type date
    data_type = "date"
    # when deserialize date
    result = deserialize_date(data_type, data, model_finder=None)
    # then expect result to be date
    assert isinstance(result, date)
    assert result == expected


@pytest.mark.parametrize("data", [None, "", "2019-oo-01"])
def test_deserialize_date_error(data):
    # given data type date
    data_type = "date"
    # when deserialize date
    with pytest.raises(ValueError):
        deserialize_date(data_type, data, model_finder=None)


# deserialize_date_ms tests
@pytest.mark.parametrize(
    "data,expected",
    [
        ("/Date(1511827200000+0000)/", date(2017, 11, 28)),
        ("/Date(1511827200000-0500)/", date(2017, 11, 28)),
        ("/Date(315619200000+0000)/", date(1980, 1, 2)),
        ("/Date(1550899400362)/", date(2019, 2, 23)),
        ("/Date(1550899400362+1300)/", date(2019, 2, 23)),
    ],
)
def test_deserialize_date_ms(data, expected):
    # given data type date in MS json format
    data_type = "date[ms-format]"
    # when deserialize date
    result = deserialize_date_ms(data_type, data, model_finder=None)
    # then expect result to be date
    assert isinstance(result, date)
    assert result == expected


@pytest.mark.parametrize("data", [None, "" "Date(1511827200000)"])
def test_deserialize_date_ms_error(data):
    # given data type date in MS json format
    data_type = "date[ms-format]"
    # when deserialize date
    with pytest.raises(ValueError):
        deserialize_date_ms(data_type, data, model_finder=None)


# deserialize_datetime tests
@pytest.mark.parametrize(
    "data,expected",
    [
        ("2020-04-03T05:35:06", datetime(2020, 4, 3, 5, 35, 6, tzinfo=tz.UTC)),
        ("2020-02-28 11:02:54", datetime(2020, 2, 28, 11, 2, 54, tzinfo=tz.UTC)),
        ("2019-12-10T12:59:59Z", datetime(2019, 12, 10, 12, 59, 59, tzinfo=tz.UTC)),
        (
            "2019-12-07T18:46:19.5187840",
            datetime(2019, 12, 7, 18, 46, 19, 518784, tzinfo=tz.UTC),
        ),
        (
            "2019-12-07T18:46:19.5187840Z",
            datetime(2019, 12, 7, 18, 46, 19, 518784, tzinfo=tz.UTC),
        ),
        (
            "2016-10-14T09:13:36.437000+13:00",
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
        ),
    ],
)
def test_deserialize_datetime(data, expected):
    # given data type datetime
    data_type = "datetime"
    # when deserialize datetime
    result = deserialize_datetime(data_type, data, model_finder=None)
    # then expect result to be datetime
    assert isinstance(result, datetime)
    assert result == expected


@pytest.mark.parametrize("data", [None, "", "invalid"])
def test_deserialize_datetime_error(data):
    # given data type datetime
    data_type = "datetime"
    # when deserialize datetime
    with pytest.raises(ValueError):
        deserialize_datetime(data_type, data, model_finder=None)


# deserialize_datetime_ms tests
@pytest.mark.parametrize(
    "data,expected",
    [
        (
            "/Date(1439434356790)/",
            datetime(2015, 8, 13, 2, 52, 36, 790000, tzinfo=tz.UTC),
        ),
        (
            "/Date(1439434356790+0000)/",
            datetime(2015, 8, 13, 2, 52, 36, 790000, tzinfo=tz.UTC),
        ),
        (
            "/Date(1476389616437+0000)/",
            datetime(2016, 10, 13, 20, 13, 36, 437000, tzinfo=tz.UTC),
        ),
        (
            "/Date(1476389616437+1300)/",
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
        ),
    ],
)
def test_deserialize_datetime_ms(data, expected):
    # given data type datetime in MS json format
    data_type = "datetime[ms-format]"
    # when deserialize datetime
    result = deserialize_datetime_ms(data_type, data, model_finder=None)
    # then expect result to be datetime
    assert isinstance(result, datetime)
    assert result == expected


@pytest.mark.parametrize("data", [None, "", "Date(1439434356790+0000/"])
def test_deserialize_datetime_ms_error(data):
    # given data type datetime in MS json format
    data_type = "datetime[ms-format]"
    # when deserialize datetime
    with pytest.raises(ValueError):
        deserialize_datetime_ms(data_type, data, model_finder=None)


# deserialize_model tests
def test_deserialize_model():
    # given test model and test data
    data = {"Value": 132, "Short": "short description"}

    class Model:
        openapi_types = {"value": "int", "description": "str"}
        attribute_map = {"value": "Value", "description": "Short"}

        def __init__(self, **kwargs):
            self.kwargs = kwargs

    # when deserialize model
    with mock_deserialize() as deserialize:
        result = deserialize_model(Model, data, model_finder=None)
    # then expect result to be model
    assert isinstance(result, Model)
    assert result.kwargs == {"value": 132, "description": "short description"}
    deserialize.assert_any_call("int", 132, None)
    deserialize.assert_any_call("str", "short description", None)


@pytest.mark.parametrize("data", [None, "", 1, True])
def test_deserialize_model_error(data):
    # given test model and invalid test data
    class Model:
        openapi_types = {"value": "int", "description": "str"}

    # when deserialize model
    with pytest.raises(ValueError):
        deserialize_model(Model, data, model_finder=None)


class Shape(Enum):
    """
    Test enum class to mimic Enum API model
    """

    SQUARE = "square"
    DIAMOND = "diamond"
    CIRCLE = "circle"


@pytest.mark.parametrize(
    "data,expected",
    [("square", Shape.SQUARE), ("diamond", Shape.DIAMOND), ("circle", Shape.CIRCLE)],
)
def test_deserialize_model_enum(data, expected):
    # given test enum model and enum value
    # when deserialize model
    result = deserialize_model(Shape, data, model_finder=None)
    # then correct Shape enum expected
    assert isinstance(result, Shape)
    assert result == expected
