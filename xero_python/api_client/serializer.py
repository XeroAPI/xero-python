# -*- coding: utf-8 -*-
import re
from datetime import datetime, time, date
from enum import Enum
from functools import singledispatch

from dateutil import tz

from xero_python.models import BaseModel
from xero_python.single_dispatch_str import single_dispatch_str

DICT_DATA_TYPE = re.compile(r"^dict(?:\[(.*)\])?$")
LIST_DATA_TYPE = re.compile(r"^list(?:\[(.*)\])?$")
TUPLE_DATA_TYPE = re.compile(r"^tuple(?:\[(.*)\])?$")


def data_type(value, explicit_type=None):
    """Get serialization data type for given value

    :param value: instance to serialize
    :param string explicit_type: explicit serialization type for value
    :return: string value serialization type
    """
    return str(explicit_type or type(value).__name__)


def serialize_routing(value, explicit_type=None):
    """Custom logic to find matching serialize implementation and
       returns it's unique registration string key
    :param value: instance to serialize
    :param explicit_type: explicit serialization type for value

    :return: str key to find proper serialize implementation
    """
    value_type = data_type(value, explicit_type)
    if DICT_DATA_TYPE.match(value_type):
        return "dict"
    if LIST_DATA_TYPE.match(value_type):
        return "list"
    if TUPLE_DATA_TYPE.match(value_type):
        return "tuple"
    return value_type


@single_dispatch_str(key=serialize_routing)
def serialize(value, explicit_type=None):
    """Serializes data into an json serializable object.
       Default implementation search model class for given data type

    :param value: instance to serialize
    :param string explicit_type: explicit serialization type for value
    :return: serialized object
    """
    if explicit_type and explicit_type != data_type(value):
        raise ValueError(
            "Can't serialize value type {!r} to explicit type {!r}".format(
                data_type(value), explicit_type
            )
        )

    return serialize_model(value)


@serialize.register("dict")
def serialize_dict(value, explicit_type=None):
    """Serializes dict data into an json serializable object.

    :param dict value: instance to serialize
    :param string explicit_type: explicit serialization type for value
    :return: serialized object
    """
    value_type = data_type(value, explicit_type)
    try:
        sub_type = DICT_DATA_TYPE.match(value_type).group(1)
    except AttributeError:
        raise ValueError("Can't serialize value type {!r}".format(value_type))
    else:
        return {key: serialize(sub_value, sub_type) for key, sub_value in value.items()}


@serialize.register("list")
def serialize_list(value, explicit_type=None):
    """Serializes list data into an json serializable object.

    :param list value: instance to serialize
    :param string explicit_type: explicit serialization type for value
    :return: serialized object
    """
    value_type = data_type(value, explicit_type)
    try:
        sub_type = LIST_DATA_TYPE.match(value_type).group(1)
    except AttributeError:
        raise ValueError("Can't serialize value type {!r}".format(value_type))
    else:
        return [serialize(sub_value, sub_type) for sub_value in value]


@serialize.register("tuple")
def serialize_tuple(value, explicit_type=None):
    """Serializes tuple data into an json serializable object.

    :param tuple value: instance to serialize
    :param string explicit_type: explicit serialization type for value
    :return: serialized object
    """
    value_type = data_type(value, explicit_type)
    try:
        sub_type = TUPLE_DATA_TYPE.match(value_type).group(1)
    except AttributeError:
        raise ValueError("Can't serialize value type {!r}".format(value_type))
    else:
        return tuple(serialize(sub_value, sub_type) for sub_value in value)


@serialize.register("str")
@serialize.register("bool")
@serialize.register("int")
@serialize.register("bytes")
def serialize_pass_through(value, explicit_type=None):
    """Serializes data by passing them directly to json serializable object.

    :param value: instance to serialize
    :param string explicit_type: explicit serialization type for value
    :return: serialized object
    """
    return value


@serialize.register("float")
@serialize.register("Decimal")
def serialize_float(value, explicit_type=None):
    """Serializes float/decimal value as float number for json serializable object.

    :param value: instance to serialize
    :param string explicit_type: explicit serialization type for value
    :return: serialized object
    """
    return float(value)


@serialize.register("date")
@serialize.register("datetime")
def serialize_datetime(value, explicit_type=None):
    """Serializes date/datetime value as iso string for json serializable object.

    :param date value: instance to serialize
    :param string explicit_type: explicit serialization type for value
    :return: serialized object
    """
    return value.isoformat()


@serialize.register("datetime[ms-format]")
def serialize_datetime_ms(value, explicit_type=None):
    """Serializes datetime value as MS json date string

    :param datetime value: instance to serialize
    :param string explicit_type: explicit serialization type for value
    :return: serialized object
    """
    tz_str = value.strftime("%z")
    timestamp_s = value.timestamp()
    timestamp_ms = int(timestamp_s * 1000)
    return "/Date({}{})/".format(timestamp_ms, tz_str)


@serialize.register("date[ms-format]")
def serialize_date_ms(value, explicit_type=None):
    """Serializes date value as MS json date string

    :param date value: instance to serialize
    :param string explicit_type: explicit serialization type for value
    :return: serialized object
    """
    if isinstance(value, datetime):
        datetime_value = value
    elif isinstance(value, date):
        # combine date with 00:00 UTC time to get correct unix timestamp
        datetime_value = datetime.combine(value, time(tzinfo=tz.UTC))
    else:
        raise ValueError("Can't serialize {!r} into Microsoft date json format")

    timestamp_s = datetime_value.timestamp()
    timestamp_ms = int(timestamp_s * 1000)
    return "/Date({})/".format(timestamp_ms)


@singledispatch
def serialize_model(model):
    """Serializes api model into an json serializable object.

    :param model: BaseModel instance to serialize
    :return: serialized object
    """
    raise ValueError("Can't serialize value type {!r}".format(data_type(model)))


@serialize_model.register(BaseModel)
def serialize_base_model(model):
    """Serializes api model into an json serializable object.

    :param model: BaseModel instance to serialize
    :return: serialized object
    """
    serialized = {}
    for attr_name, attr_type in model.openapi_types.items():
        attr_value = getattr(model, attr_name)
        if attr_value is not None:  # TODO how do you null given field
            key = model.attribute_map[attr_name]
            attr_value = serialize(attr_value, attr_type)
            serialized[key] = attr_value

    return serialized


@serialize_model.register(Enum)
def serialize_enum_model(model):
    """Serializes api model into an json serializable object.

    :param model: BaseModel instance to serialize
    :return: serialized object
    """
    return model.value
