# coding: utf-8

"""
Xero Finance API

The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BalanceSheetAccountType(BaseModel):
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
        "account_type": "str",
        "accounts": "list[BalanceSheetAccountDetail]",
        "total": "float",
    }

    attribute_map = {
        "account_type": "accountType",
        "accounts": "accounts",
        "total": "total",
    }

    def __init__(self, account_type=None, accounts=None, total=None):  # noqa: E501
        """BalanceSheetAccountType - a model defined in OpenAPI"""  # noqa: E501

        self._account_type = None
        self._accounts = None
        self._total = None
        self.discriminator = None

        if account_type is not None:
            self.account_type = account_type
        if accounts is not None:
            self.accounts = accounts
        if total is not None:
            self.total = total

    @property
    def account_type(self):
        """Gets the account_type of this BalanceSheetAccountType.  # noqa: E501

        The type of the account. See <a href='https://developer.xero.com/documentation/api/types#AccountTypes'>Account Types</a>  # noqa: E501

        :return: The account_type of this BalanceSheetAccountType.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this BalanceSheetAccountType.

        The type of the account. See <a href='https://developer.xero.com/documentation/api/types#AccountTypes'>Account Types</a>  # noqa: E501

        :param account_type: The account_type of this BalanceSheetAccountType.  # noqa: E501
        :type: str
        """

        self._account_type = account_type

    @property
    def accounts(self):
        """Gets the accounts of this BalanceSheetAccountType.  # noqa: E501

        A list of all accounts of this type. Refer to the Account section below for each account element detail.  # noqa: E501

        :return: The accounts of this BalanceSheetAccountType.  # noqa: E501
        :rtype: list[BalanceSheetAccountDetail]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this BalanceSheetAccountType.

        A list of all accounts of this type. Refer to the Account section below for each account element detail.  # noqa: E501

        :param accounts: The accounts of this BalanceSheetAccountType.  # noqa: E501
        :type: list[BalanceSheetAccountDetail]
        """

        self._accounts = accounts

    @property
    def total(self):
        """Gets the total of this BalanceSheetAccountType.  # noqa: E501

        Total value of all the accounts in this type  # noqa: E501

        :return: The total of this BalanceSheetAccountType.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BalanceSheetAccountType.

        Total value of all the accounts in this type  # noqa: E501

        :param total: The total of this BalanceSheetAccountType.  # noqa: E501
        :type: float
        """

        self._total = total
