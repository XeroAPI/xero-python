# coding: utf-8

"""
Xero Accounting API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ConversionBalances(BaseModel):
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
        "account_code": "str",
        "balance": "float",
        "balance_details": "list[BalanceDetails]",
    }

    attribute_map = {
        "account_code": "AccountCode",
        "balance": "Balance",
        "balance_details": "BalanceDetails",
    }

    def __init__(
        self, account_code=None, balance=None, balance_details=None
    ):  # noqa: E501
        """ConversionBalances - a model defined in OpenAPI"""  # noqa: E501

        self._account_code = None
        self._balance = None
        self._balance_details = None
        self.discriminator = None

        if account_code is not None:
            self.account_code = account_code
        if balance is not None:
            self.balance = balance
        if balance_details is not None:
            self.balance_details = balance_details

    @property
    def account_code(self):
        """Gets the account_code of this ConversionBalances.  # noqa: E501

        The account code for a account  # noqa: E501

        :return: The account_code of this ConversionBalances.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this ConversionBalances.

        The account code for a account  # noqa: E501

        :param account_code: The account_code of this ConversionBalances.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def balance(self):
        """Gets the balance of this ConversionBalances.  # noqa: E501

        The opening balances of the account. Debits are positive, credits are negative values  # noqa: E501

        :return: The balance of this ConversionBalances.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ConversionBalances.

        The opening balances of the account. Debits are positive, credits are negative values  # noqa: E501

        :param balance: The balance of this ConversionBalances.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def balance_details(self):
        """Gets the balance_details of this ConversionBalances.  # noqa: E501


        :return: The balance_details of this ConversionBalances.  # noqa: E501
        :rtype: list[BalanceDetails]
        """
        return self._balance_details

    @balance_details.setter
    def balance_details(self, balance_details):
        """Sets the balance_details of this ConversionBalances.


        :param balance_details: The balance_details of this ConversionBalances.  # noqa: E501
        :type: list[BalanceDetails]
        """

        self._balance_details = balance_details
