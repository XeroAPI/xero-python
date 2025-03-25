# coding: utf-8

"""
Xero Accounting API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Invoices(BaseModel):
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
    openapi_types = {
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "invoices": "list[Invoice]",
    }

    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "invoices": "Invoices",
    }

    def __init__(self, pagination=None, warnings=None, invoices=None):  # noqa: E501
        """Invoices - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._warnings = None
        self._invoices = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if invoices is not None:
            self.invoices = invoices

    @property
    def pagination(self):
        """Gets the pagination of this Invoices.  # noqa: E501


        :return: The pagination of this Invoices.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this Invoices.


        :param pagination: The pagination of this Invoices.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def warnings(self):
        """Gets the warnings of this Invoices.  # noqa: E501

        Displays array of warning messages from the API  # noqa: E501

        :return: The warnings of this Invoices.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this Invoices.

        Displays array of warning messages from the API  # noqa: E501

        :param warnings: The warnings of this Invoices.  # noqa: E501
        :type: list[ValidationError]
        """

        self._warnings = warnings

    @property
    def invoices(self):
        """Gets the invoices of this Invoices.  # noqa: E501


        :return: The invoices of this Invoices.  # noqa: E501
        :rtype: list[Invoice]
        """
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        """Sets the invoices of this Invoices.


        :param invoices: The invoices of this Invoices.  # noqa: E501
        :type: list[Invoice]
        """

        self._invoices = invoices
