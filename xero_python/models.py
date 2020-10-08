# -*- coding: utf-8 -*-
import pprint
from functools import singledispatch


class BaseModel:
    """"""

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {}  # child model to define specific mappings

    attribute_map = {}  # child model to define specific mappings

    def to_dict(self):
        """Returns the model properties as a dict"""
        return {
            key: serialize_to_dict(getattr(self, key))
            for key in self.openapi_types.keys()
        }

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, type(self)):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


@singledispatch
def serialize_to_dict(value):
    return value


@serialize_to_dict.register(BaseModel)
def serialize_model_to_dict(value):
    return value.to_dict()


@serialize_to_dict.register(list)
def serialize_list_to_dict(value):
    return [serialize_to_dict(item) for item in value]


@serialize_to_dict.register(tuple)
def serialize_tuple_to_dict(value):
    return tuple(serialize_to_dict(item) for item in value)


@serialize_to_dict.register(dict)
def serialize_dict_to_dict(value):
    return {key: serialize_to_dict(val) for key, val in value.items()}
