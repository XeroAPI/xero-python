# coding: utf-8

"""
Xero Accounting API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Setup(BaseModel):
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
        "conversion_date": "ConversionDate",
        "conversion_balances": "list[ConversionBalances]",
        "accounts": "list[Account]",
    }

    attribute_map = {
        "conversion_date": "ConversionDate",
        "conversion_balances": "ConversionBalances",
        "accounts": "Accounts",
    }

    def __init__(
        self, conversion_date=None, conversion_balances=None, accounts=None
    ):  # noqa: E501
        """Setup - a model defined in OpenAPI"""  # noqa: E501

        self._conversion_date = None
        self._conversion_balances = None
        self._accounts = None
        self.discriminator = None

        if conversion_date is not None:
            self.conversion_date = conversion_date
        if conversion_balances is not None:
            self.conversion_balances = conversion_balances
        if accounts is not None:
            self.accounts = accounts

    @property
    def conversion_date(self):
        """Gets the conversion_date of this Setup.  # noqa: E501


        :return: The conversion_date of this Setup.  # noqa: E501
        :rtype: ConversionDate
        """
        return self._conversion_date

    @conversion_date.setter
    def conversion_date(self, conversion_date):
        """Sets the conversion_date of this Setup.


        :param conversion_date: The conversion_date of this Setup.  # noqa: E501
        :type: ConversionDate
        """

        self._conversion_date = conversion_date

    @property
    def conversion_balances(self):
        """Gets the conversion_balances of this Setup.  # noqa: E501

        Balance supplied for each account that has a value as at the conversion date.  # noqa: E501

        :return: The conversion_balances of this Setup.  # noqa: E501
        :rtype: list[ConversionBalances]
        """
        return self._conversion_balances

    @conversion_balances.setter
    def conversion_balances(self, conversion_balances):
        """Sets the conversion_balances of this Setup.

        Balance supplied for each account that has a value as at the conversion date.  # noqa: E501

        :param conversion_balances: The conversion_balances of this Setup.  # noqa: E501
        :type: list[ConversionBalances]
        """

        self._conversion_balances = conversion_balances

    @property
    def accounts(self):
        """Gets the accounts of this Setup.  # noqa: E501


        :return: The accounts of this Setup.  # noqa: E501
        :rtype: list[Account]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this Setup.


        :param accounts: The accounts of this Setup.  # noqa: E501
        :type: list[Account]
        """

        self._accounts = accounts
