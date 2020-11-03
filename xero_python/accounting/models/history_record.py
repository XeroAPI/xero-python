# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.3.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class HistoryRecord(BaseModel):
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
        "details": "str",
        "changes": "str",
        "user": "str",
        "date_utc": "datetime[ms-format]",
    }

    attribute_map = {
        "details": "Details",
        "changes": "Changes",
        "user": "User",
        "date_utc": "DateUTC",
    }

    def __init__(
        self, details=None, changes=None, user=None, date_utc=None
    ):  # noqa: E501
        """HistoryRecord - a model defined in OpenAPI"""  # noqa: E501

        self._details = None
        self._changes = None
        self._user = None
        self._date_utc = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if changes is not None:
            self.changes = changes
        if user is not None:
            self.user = user
        if date_utc is not None:
            self.date_utc = date_utc

    @property
    def details(self):
        """Gets the details of this HistoryRecord.  # noqa: E501

        details  # noqa: E501

        :return: The details of this HistoryRecord.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this HistoryRecord.

        details  # noqa: E501

        :param details: The details of this HistoryRecord.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def changes(self):
        """Gets the changes of this HistoryRecord.  # noqa: E501

        Name of branding theme  # noqa: E501

        :return: The changes of this HistoryRecord.  # noqa: E501
        :rtype: str
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this HistoryRecord.

        Name of branding theme  # noqa: E501

        :param changes: The changes of this HistoryRecord.  # noqa: E501
        :type: str
        """

        self._changes = changes

    @property
    def user(self):
        """Gets the user of this HistoryRecord.  # noqa: E501

        has a value of 0  # noqa: E501

        :return: The user of this HistoryRecord.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this HistoryRecord.

        has a value of 0  # noqa: E501

        :param user: The user of this HistoryRecord.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def date_utc(self):
        """Gets the date_utc of this HistoryRecord.  # noqa: E501

        UTC timestamp of creation date of branding theme  # noqa: E501

        :return: The date_utc of this HistoryRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._date_utc

    @date_utc.setter
    def date_utc(self, date_utc):
        """Sets the date_utc of this HistoryRecord.

        UTC timestamp of creation date of branding theme  # noqa: E501

        :param date_utc: The date_utc of this HistoryRecord.  # noqa: E501
        :type: datetime
        """

        self._date_utc = date_utc
