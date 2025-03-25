# coding: utf-8

"""
Xero Finance API

The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ContactTotalOther(BaseModel):
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
        "total_outstanding_aged": "float",
        "total_voided": "float",
        "total_credited": "float",
        "transaction_count": "int",
    }

    attribute_map = {
        "total_outstanding_aged": "totalOutstandingAged",
        "total_voided": "totalVoided",
        "total_credited": "totalCredited",
        "transaction_count": "transactionCount",
    }

    def __init__(
        self,
        total_outstanding_aged=None,
        total_voided=None,
        total_credited=None,
        transaction_count=None,
    ):  # noqa: E501
        """ContactTotalOther - a model defined in OpenAPI"""  # noqa: E501

        self._total_outstanding_aged = None
        self._total_voided = None
        self._total_credited = None
        self._transaction_count = None
        self.discriminator = None

        if total_outstanding_aged is not None:
            self.total_outstanding_aged = total_outstanding_aged
        if total_voided is not None:
            self.total_voided = total_voided
        if total_credited is not None:
            self.total_credited = total_credited
        if transaction_count is not None:
            self.transaction_count = transaction_count

    @property
    def total_outstanding_aged(self):
        """Gets the total_outstanding_aged of this ContactTotalOther.  # noqa: E501

        Total outstanding invoice value for the contact within the period where the invoices are more than 90 days old  # noqa: E501

        :return: The total_outstanding_aged of this ContactTotalOther.  # noqa: E501
        :rtype: float
        """
        return self._total_outstanding_aged

    @total_outstanding_aged.setter
    def total_outstanding_aged(self, total_outstanding_aged):
        """Sets the total_outstanding_aged of this ContactTotalOther.

        Total outstanding invoice value for the contact within the period where the invoices are more than 90 days old  # noqa: E501

        :param total_outstanding_aged: The total_outstanding_aged of this ContactTotalOther.  # noqa: E501
        :type: float
        """

        self._total_outstanding_aged = total_outstanding_aged

    @property
    def total_voided(self):
        """Gets the total_voided of this ContactTotalOther.  # noqa: E501

        Total voided value for the contact.  # noqa: E501

        :return: The total_voided of this ContactTotalOther.  # noqa: E501
        :rtype: float
        """
        return self._total_voided

    @total_voided.setter
    def total_voided(self, total_voided):
        """Sets the total_voided of this ContactTotalOther.

        Total voided value for the contact.  # noqa: E501

        :param total_voided: The total_voided of this ContactTotalOther.  # noqa: E501
        :type: float
        """

        self._total_voided = total_voided

    @property
    def total_credited(self):
        """Gets the total_credited of this ContactTotalOther.  # noqa: E501

        Total credited value for the contact.  # noqa: E501

        :return: The total_credited of this ContactTotalOther.  # noqa: E501
        :rtype: float
        """
        return self._total_credited

    @total_credited.setter
    def total_credited(self, total_credited):
        """Sets the total_credited of this ContactTotalOther.

        Total credited value for the contact.  # noqa: E501

        :param total_credited: The total_credited of this ContactTotalOther.  # noqa: E501
        :type: float
        """

        self._total_credited = total_credited

    @property
    def transaction_count(self):
        """Gets the transaction_count of this ContactTotalOther.  # noqa: E501

        Number of transactions for the contact.  # noqa: E501

        :return: The transaction_count of this ContactTotalOther.  # noqa: E501
        :rtype: int
        """
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, transaction_count):
        """Sets the transaction_count of this ContactTotalOther.

        Number of transactions for the contact.  # noqa: E501

        :param transaction_count: The transaction_count of this ContactTotalOther.  # noqa: E501
        :type: int
        """

        self._transaction_count = transaction_count
