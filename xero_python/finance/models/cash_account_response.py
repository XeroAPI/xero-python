# coding: utf-8

"""
Xero Finance API

The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class CashAccountResponse(BaseModel):
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
        "unreconciled_amount_pos": "float",
        "unreconciled_amount_neg": "float",
        "starting_balance": "float",
        "account_balance": "float",
        "balance_currency": "str",
    }

    attribute_map = {
        "unreconciled_amount_pos": "unreconciledAmountPos",
        "unreconciled_amount_neg": "unreconciledAmountNeg",
        "starting_balance": "startingBalance",
        "account_balance": "accountBalance",
        "balance_currency": "balanceCurrency",
    }

    def __init__(
        self,
        unreconciled_amount_pos=None,
        unreconciled_amount_neg=None,
        starting_balance=None,
        account_balance=None,
        balance_currency=None,
    ):  # noqa: E501
        """CashAccountResponse - a model defined in OpenAPI"""  # noqa: E501

        self._unreconciled_amount_pos = None
        self._unreconciled_amount_neg = None
        self._starting_balance = None
        self._account_balance = None
        self._balance_currency = None
        self.discriminator = None

        if unreconciled_amount_pos is not None:
            self.unreconciled_amount_pos = unreconciled_amount_pos
        if unreconciled_amount_neg is not None:
            self.unreconciled_amount_neg = unreconciled_amount_neg
        if starting_balance is not None:
            self.starting_balance = starting_balance
        if account_balance is not None:
            self.account_balance = account_balance
        if balance_currency is not None:
            self.balance_currency = balance_currency

    @property
    def unreconciled_amount_pos(self):
        """Gets the unreconciled_amount_pos of this CashAccountResponse.  # noqa: E501

        Total value of transactions in the journals which are not reconciled to bank statement lines, and have a positive (debit) value.  # noqa: E501

        :return: The unreconciled_amount_pos of this CashAccountResponse.  # noqa: E501
        :rtype: float
        """
        return self._unreconciled_amount_pos

    @unreconciled_amount_pos.setter
    def unreconciled_amount_pos(self, unreconciled_amount_pos):
        """Sets the unreconciled_amount_pos of this CashAccountResponse.

        Total value of transactions in the journals which are not reconciled to bank statement lines, and have a positive (debit) value.  # noqa: E501

        :param unreconciled_amount_pos: The unreconciled_amount_pos of this CashAccountResponse.  # noqa: E501
        :type: float
        """

        self._unreconciled_amount_pos = unreconciled_amount_pos

    @property
    def unreconciled_amount_neg(self):
        """Gets the unreconciled_amount_neg of this CashAccountResponse.  # noqa: E501

        Total value of transactions in the journals which are not reconciled to bank statement lines, and have a negative (credit) value.  # noqa: E501

        :return: The unreconciled_amount_neg of this CashAccountResponse.  # noqa: E501
        :rtype: float
        """
        return self._unreconciled_amount_neg

    @unreconciled_amount_neg.setter
    def unreconciled_amount_neg(self, unreconciled_amount_neg):
        """Sets the unreconciled_amount_neg of this CashAccountResponse.

        Total value of transactions in the journals which are not reconciled to bank statement lines, and have a negative (credit) value.  # noqa: E501

        :param unreconciled_amount_neg: The unreconciled_amount_neg of this CashAccountResponse.  # noqa: E501
        :type: float
        """

        self._unreconciled_amount_neg = unreconciled_amount_neg

    @property
    def starting_balance(self):
        """Gets the starting_balance of this CashAccountResponse.  # noqa: E501

        Starting (or historic) balance from the journals (manually keyed in by users on account creation - unverified).  # noqa: E501

        :return: The starting_balance of this CashAccountResponse.  # noqa: E501
        :rtype: float
        """
        return self._starting_balance

    @starting_balance.setter
    def starting_balance(self, starting_balance):
        """Sets the starting_balance of this CashAccountResponse.

        Starting (or historic) balance from the journals (manually keyed in by users on account creation - unverified).  # noqa: E501

        :param starting_balance: The starting_balance of this CashAccountResponse.  # noqa: E501
        :type: float
        """

        self._starting_balance = starting_balance

    @property
    def account_balance(self):
        """Gets the account_balance of this CashAccountResponse.  # noqa: E501

        Current cash at bank accounting value from the journals.  # noqa: E501

        :return: The account_balance of this CashAccountResponse.  # noqa: E501
        :rtype: float
        """
        return self._account_balance

    @account_balance.setter
    def account_balance(self, account_balance):
        """Sets the account_balance of this CashAccountResponse.

        Current cash at bank accounting value from the journals.  # noqa: E501

        :param account_balance: The account_balance of this CashAccountResponse.  # noqa: E501
        :type: float
        """

        self._account_balance = account_balance

    @property
    def balance_currency(self):
        """Gets the balance_currency of this CashAccountResponse.  # noqa: E501

        Currency which the cashAccount transactions relate to.  # noqa: E501

        :return: The balance_currency of this CashAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._balance_currency

    @balance_currency.setter
    def balance_currency(self, balance_currency):
        """Sets the balance_currency of this CashAccountResponse.

        Currency which the cashAccount transactions relate to.  # noqa: E501

        :param balance_currency: The balance_currency of this CashAccountResponse.  # noqa: E501
        :type: str
        """

        self._balance_currency = balance_currency
