# coding: utf-8

"""
Xero Finance API

The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BankTransactionResponse(BaseModel):
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
        "bank_transaction_id": "str",
        "batch_payment_id": "str",
        "contact": "ContactResponse",
        "date": "date",
        "amount": "float",
        "line_items": "list[LineItemResponse]",
    }

    attribute_map = {
        "bank_transaction_id": "bankTransactionId",
        "batch_payment_id": "batchPaymentId",
        "contact": "contact",
        "date": "date",
        "amount": "amount",
        "line_items": "lineItems",
    }

    def __init__(
        self,
        bank_transaction_id=None,
        batch_payment_id=None,
        contact=None,
        date=None,
        amount=None,
        line_items=None,
    ):  # noqa: E501
        """BankTransactionResponse - a model defined in OpenAPI"""  # noqa: E501

        self._bank_transaction_id = None
        self._batch_payment_id = None
        self._contact = None
        self._date = None
        self._amount = None
        self._line_items = None
        self.discriminator = None

        if bank_transaction_id is not None:
            self.bank_transaction_id = bank_transaction_id
        if batch_payment_id is not None:
            self.batch_payment_id = batch_payment_id
        if contact is not None:
            self.contact = contact
        if date is not None:
            self.date = date
        if amount is not None:
            self.amount = amount
        if line_items is not None:
            self.line_items = line_items

    @property
    def bank_transaction_id(self):
        """Gets the bank_transaction_id of this BankTransactionResponse.  # noqa: E501

        Xero Identifier of transaction  # noqa: E501

        :return: The bank_transaction_id of this BankTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._bank_transaction_id

    @bank_transaction_id.setter
    def bank_transaction_id(self, bank_transaction_id):
        """Sets the bank_transaction_id of this BankTransactionResponse.

        Xero Identifier of transaction  # noqa: E501

        :param bank_transaction_id: The bank_transaction_id of this BankTransactionResponse.  # noqa: E501
        :type: str
        """

        self._bank_transaction_id = bank_transaction_id

    @property
    def batch_payment_id(self):
        """Gets the batch_payment_id of this BankTransactionResponse.  # noqa: E501

        Xero Identifier of batch payment. Present if the transaction is part of a batch.  # noqa: E501

        :return: The batch_payment_id of this BankTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._batch_payment_id

    @batch_payment_id.setter
    def batch_payment_id(self, batch_payment_id):
        """Sets the batch_payment_id of this BankTransactionResponse.

        Xero Identifier of batch payment. Present if the transaction is part of a batch.  # noqa: E501

        :param batch_payment_id: The batch_payment_id of this BankTransactionResponse.  # noqa: E501
        :type: str
        """

        self._batch_payment_id = batch_payment_id

    @property
    def contact(self):
        """Gets the contact of this BankTransactionResponse.  # noqa: E501


        :return: The contact of this BankTransactionResponse.  # noqa: E501
        :rtype: ContactResponse
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this BankTransactionResponse.


        :param contact: The contact of this BankTransactionResponse.  # noqa: E501
        :type: ContactResponse
        """

        self._contact = contact

    @property
    def date(self):
        """Gets the date of this BankTransactionResponse.  # noqa: E501

        Date of transaction - YYYY-MM-DD  # noqa: E501

        :return: The date of this BankTransactionResponse.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this BankTransactionResponse.

        Date of transaction - YYYY-MM-DD  # noqa: E501

        :param date: The date of this BankTransactionResponse.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def amount(self):
        """Gets the amount of this BankTransactionResponse.  # noqa: E501

        Amount of transaction  # noqa: E501

        :return: The amount of this BankTransactionResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BankTransactionResponse.

        Amount of transaction  # noqa: E501

        :param amount: The amount of this BankTransactionResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def line_items(self):
        """Gets the line_items of this BankTransactionResponse.  # noqa: E501

        The LineItems element can contain any number of individual LineItem sub-elements. Not included in summary mode  # noqa: E501

        :return: The line_items of this BankTransactionResponse.  # noqa: E501
        :rtype: list[LineItemResponse]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this BankTransactionResponse.

        The LineItems element can contain any number of individual LineItem sub-elements. Not included in summary mode  # noqa: E501

        :param line_items: The line_items of this BankTransactionResponse.  # noqa: E501
        :type: list[LineItemResponse]
        """

        self._line_items = line_items
