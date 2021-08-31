# -*- coding: utf-8 -*-
import datetime
import re
from decimal import Decimal
from enum import Enum

from dateutil import tz
from dateutil.parser.isoparser import isoparse, DEFAULT_ISOPARSER

from xero_python.single_dispatch_str import single_dispatch_str

LIST_DATA_TYPE = re.compile(r"list\[(.*)\]")

# taken from https://github.com/django/django/blob/master/django/utils/dateparse.py
# at 4bbe8261c402694a1da3efcaafe3332f9c57af15
DATE_RE = re.compile(r"(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})$")
DATETIME_RE = re.compile(
    r"(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})"
    r"[T ](?P<hour>\d{1,2}):(?P<minute>\d{1,2})"
    r"(?::(?P<second>\d{1,2})(?:[\.,](?P<microsecond>\d{1,6})\d{0,6})?)?"
    r"(?P<tzinfo>Z|[+-]\d{2}(?::?\d{2})?)?$"
)

MS_DATETIME_RE = re.compile(r"/Date\((?P<timestamp>-?\d+)(?P<tzinfo>[+-]\d{2,4})?\)/$")
DATE_WITH_NO_DAY_RE = re.compile("(\d\d\d\d)-(\d\d)")


def deserialize_routing(data_type, data, model_finder):
    """Custom logic to find matching deserialize implementation and
       returns it's unique registration string key
    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: str key to find proper deserialize implementation
    """
    if LIST_DATA_TYPE.match(data_type):
        return "list"
    return data_type


@single_dispatch_str(key=deserialize_routing)
def deserialize(data_type, data, model_finder):
    """Deserializes data into an object.
       Default implementation search model class for given data type

    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: deserialized object.

    """
    try:
        model = model_finder.find_model(data_type)
    except AttributeError:
        raise ValueError("Can't deserialize data_type={!r}".format(data_type))
    else:
        return deserialize_model(model, data, model_finder)


@deserialize.register("list")
def deserialize_list(data_type, data, model_finder):
    """Deserializes data into a list of objects.

    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: deserialized list

    """
    try:
        sub_data_type = LIST_DATA_TYPE.match(data_type).group(1)
    except AttributeError:
        raise ValueError("Can't deserialize data_type={!r}".format(data_type))
    else:
        return [deserialize(sub_data_type, sub_data, model_finder) for sub_data in data]


@deserialize.register("int")
def deserialize_int(data_type, data, model_finder):
    """Deserializes data into an integer number.

    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: deserialized int

    """
    return int(data)


@deserialize.register("float")
def deserialize_decimal(data_type, data, model_finder):
    """Deserializes data into a Decimal number.

    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: deserialized Decimal

    """
    if data is not None:
        return data if isinstance(data, Decimal) else Decimal(data)

    return data


@deserialize.register("str")
def deserialize_str(data_type, data, model_finder):
    """Deserializes data into a string

    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: deserialized str

    """
    return str(data)


@deserialize.register("bool")
def deserialize_bool(data_type, data, model_finder):
    """Deserializes data into a boolean object.

    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: deserialized bool

    """
    # allowed json payload is true or false - parsed to bool via json.loads
    if data is not None:
        if not isinstance(data, bool):
            raise ValueError("Json parsed bool value expected. got {!r}".format(data))

    return bool(data)


@deserialize.register("date")
def deserialize_date(data_type, data, model_finder):
    """Deserializes data into a python date
       Expected input value in format YYYY-MM-DD as per
       https://tools.ietf.org/html/rfc3339#section-5.6 standard

       Raise ValueError if the input is well formatted but not a valid date.
       Return None if the input isn't well formatted.

    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: deserialized datetime.date

    """
    # based on https://github.com/django/django/blob/master/django/utils/dateparse.py
    # at 4bbe8261c402694a1da3efcaafe3332f9c57af15
    match = DATE_RE.match(str(data))
    match2 = DATETIME_RE.match(str(data))

    if data is not None:
        if match:
            kw = {k: int(v) for k, v in match.groupdict().items()}
            return datetime.date(**kw)
        elif match2:
            dt = isoparse(data)
            return dt
        else:
            raise ValueError("Invalid date value {!r}".format(data))


@deserialize.register("date[ms-format]")
def deserialize_date_ms(data_type, data, model_finder):
    """Deserializes data into a python date
       Expected input value in format /Date(timestamp_in_milliseconds)/

       Raise ValueError if the input is well formatted but not a valid date.
       Return None if the input isn't well formatted.

    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: deserialized datetime.date

    """
    ms_datetime = deserialize_datetime_ms(data_type, data, model_finder)
    # shift datetime to utc timezone to make sure utc date used
    return ms_datetime.astimezone(tz=tz.UTC).date()


@deserialize.register("datetime")
def deserialize_datetime(data_type, data, model_finder):
    """Deserializes data into a python datetime

       Expected input value in format YYYY-MM-DDTHH:mm:ss[Z] as per
       https://tools.ietf.org/html/rfc3339#section-5.6 standard

       Raise ValueError if the input is well formatted but not a valid datetime.
       Return None if the input isn't well formatted.

    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: deserialized datetime.datetime

    """
    if data is not None:
        try:
            dt = isoparse(data)
        except (ValueError, TypeError):
            raise ValueError("Invalid datetime value {!r}".format(data))

        if not dt.tzinfo:
            # timezone naive datetime from Xero API response always in UTC
            dt = dt.replace(tzinfo=tz.UTC)

        return dt


@deserialize.register("datetime[ms-format]")
def deserialize_datetime_ms(data_type, data, model_finder):
    """Deserializes data into a python datetime

       Expected input value in format /Date(timestamp_in_milliseconds)/

       Raise ValueError if the input is well formatted but not a valid datetime.
       Return None if the input isn't well formatted.

    :param data_type: class literal for deserialized object, or string of class name
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for data_type class literal

    :return: deserialized datetime.datetime

    """
    match = MS_DATETIME_RE.match(str(data))
    if match:
        tz_str = match.groupdict()["tzinfo"]
        if tz_str:
            tz_info = DEFAULT_ISOPARSER.parse_tzstr(tz_str)
        else:
            # timezone naive datetime from Xero API response always in UTC
            tz_info = tz.UTC

        timestamp_ms = int(match.groupdict()["timestamp"])
        timestamp_s = timestamp_ms / 1000
        return datetime.datetime.fromtimestamp(timestamp_s, tz=tz_info)
    elif DATE_WITH_NO_DAY_RE.match(str(data)):
        return datetime.datetime.strptime(data + "-01", "%Y-%m-%d")
    else:
        raise ValueError("Invalid datetime value {!r}".format(data))


def deserialize_model(model, data, model_finder):
    """Deserializes data into model instance.

    :param model: class object
    :param data: data to be parsed
    :param model_finder: ModelFinder instance to find class for class literal

    :return: deserialized model instance.

    """
    if data is None:
        return model("")

    if issubclass(model, Enum):
        return model(data)

    if not isinstance(data, (list, dict)):
        raise ValueError("list or dict value expected. got {!r}".format(data))

    kwargs = {}
    for attr, attr_type in model.openapi_types.items():
        attr_key = model.attribute_map[attr]
        if attr_key in data:
            value = data[attr_key]
            kwargs[attr] = deserialize(attr_type, value, model_finder)

    instance = model(**kwargs)
    return instance
