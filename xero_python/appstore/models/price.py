# coding: utf-8

"""
Xero AppStore API

These endpoints are for Xero Partners to interact with the App Store Billing platform  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Price(BaseModel):
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
    openapi_types = {"amount": "float", "currency": "str", "id": "str"}

    attribute_map = {"amount": "amount", "currency": "currency", "id": "id"}

    def __init__(self, amount=None, currency=None, id=None):  # noqa: E501
        """Price - a model defined in OpenAPI"""  # noqa: E501

        self._amount = None
        self._currency = None
        self._id = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency
        self.id = id

    @property
    def amount(self):
        """Gets the amount of this Price.  # noqa: E501

        The net (before tax) amount.  # noqa: E501

        :return: The amount of this Price.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Price.

        The net (before tax) amount.  # noqa: E501

        :param amount: The amount of this Price.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError(
                "Invalid value for `amount`, must not be `None`"
            )  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this Price.  # noqa: E501

        The currency of the price.  # noqa: E501

        :return: The currency of this Price.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Price.

        The currency of the price.  # noqa: E501

        :param currency: The currency of this Price.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError(
                "Invalid value for `currency`, must not be `None`"
            )  # noqa: E501

        self._currency = currency

    @property
    def id(self):
        """Gets the id of this Price.  # noqa: E501

        The unique identifier of the price.  # noqa: E501

        :return: The id of this Price.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Price.

        The unique identifier of the price.  # noqa: E501

        :param id: The id of this Price.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id
