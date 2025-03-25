# coding: utf-8

"""
Xero Finance API

The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class AccountUsageResponse(BaseModel):
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
        "organisation_id": "str",
        "start_month": "str",
        "end_month": "str",
        "account_usage": "list[AccountUsage]",
    }

    attribute_map = {
        "organisation_id": "organisationId",
        "start_month": "startMonth",
        "end_month": "endMonth",
        "account_usage": "accountUsage",
    }

    def __init__(
        self, organisation_id=None, start_month=None, end_month=None, account_usage=None
    ):  # noqa: E501
        """AccountUsageResponse - a model defined in OpenAPI"""  # noqa: E501

        self._organisation_id = None
        self._start_month = None
        self._end_month = None
        self._account_usage = None
        self.discriminator = None

        if organisation_id is not None:
            self.organisation_id = organisation_id
        if start_month is not None:
            self.start_month = start_month
        if end_month is not None:
            self.end_month = end_month
        if account_usage is not None:
            self.account_usage = account_usage

    @property
    def organisation_id(self):
        """Gets the organisation_id of this AccountUsageResponse.  # noqa: E501

        The requested Organisation to which the data pertains  # noqa: E501

        :return: The organisation_id of this AccountUsageResponse.  # noqa: E501
        :rtype: str
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this AccountUsageResponse.

        The requested Organisation to which the data pertains  # noqa: E501

        :param organisation_id: The organisation_id of this AccountUsageResponse.  # noqa: E501
        :type: str
        """

        self._organisation_id = organisation_id

    @property
    def start_month(self):
        """Gets the start_month of this AccountUsageResponse.  # noqa: E501

        The start month of the report  # noqa: E501

        :return: The start_month of this AccountUsageResponse.  # noqa: E501
        :rtype: str
        """
        return self._start_month

    @start_month.setter
    def start_month(self, start_month):
        """Sets the start_month of this AccountUsageResponse.

        The start month of the report  # noqa: E501

        :param start_month: The start_month of this AccountUsageResponse.  # noqa: E501
        :type: str
        """

        self._start_month = start_month

    @property
    def end_month(self):
        """Gets the end_month of this AccountUsageResponse.  # noqa: E501

        The end month of the report  # noqa: E501

        :return: The end_month of this AccountUsageResponse.  # noqa: E501
        :rtype: str
        """
        return self._end_month

    @end_month.setter
    def end_month(self, end_month):
        """Sets the end_month of this AccountUsageResponse.

        The end month of the report  # noqa: E501

        :param end_month: The end_month of this AccountUsageResponse.  # noqa: E501
        :type: str
        """

        self._end_month = end_month

    @property
    def account_usage(self):
        """Gets the account_usage of this AccountUsageResponse.  # noqa: E501


        :return: The account_usage of this AccountUsageResponse.  # noqa: E501
        :rtype: list[AccountUsage]
        """
        return self._account_usage

    @account_usage.setter
    def account_usage(self, account_usage):
        """Sets the account_usage of this AccountUsageResponse.


        :param account_usage: The account_usage of this AccountUsageResponse.  # noqa: E501
        :type: list[AccountUsage]
        """

        self._account_usage = account_usage
