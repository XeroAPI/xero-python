# coding: utf-8

"""
Xero Accounting API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ReportFields(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"field_id": "str", "description": "str", "value": "str"}

    attribute_map = {
        "field_id": "FieldID",
        "description": "Description",
        "value": "Value",
    }

    def __init__(self, field_id=None, description=None, value=None):  # noqa: E501
        """ReportFields - a model defined in OpenAPI"""  # noqa: E501

        self._field_id = None
        self._description = None
        self._value = None
        self.discriminator = None

        if field_id is not None:
            self.field_id = field_id
        if description is not None:
            self.description = description
        if value is not None:
            self.value = value

    @property
    def field_id(self):
        """Gets the field_id of this ReportFields.  # noqa: E501


        :return: The field_id of this ReportFields.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this ReportFields.


        :param field_id: The field_id of this ReportFields.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def description(self):
        """Gets the description of this ReportFields.  # noqa: E501


        :return: The description of this ReportFields.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReportFields.


        :param description: The description of this ReportFields.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """Gets the value of this ReportFields.  # noqa: E501


        :return: The value of this ReportFields.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ReportFields.


        :param value: The value of this ReportFields.  # noqa: E501
        :type: str
        """

        self._value = value
