# coding: utf-8

"""
Xero Finance API

The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BalanceSheetAccountDetail(BaseModel):
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
        "code": "str",
        "account_id": "str",
        "name": "str",
        "reporting_code": "str",
        "total": "float",
    }

    attribute_map = {
        "code": "code",
        "account_id": "accountID",
        "name": "name",
        "reporting_code": "reportingCode",
        "total": "total",
    }

    def __init__(
        self, code=None, account_id=None, name=None, reporting_code=None, total=None
    ):  # noqa: E501
        """BalanceSheetAccountDetail - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._account_id = None
        self._name = None
        self._reporting_code = None
        self._total = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if reporting_code is not None:
            self.reporting_code = reporting_code
        if total is not None:
            self.total = total

    @property
    def code(self):
        """Gets the code of this BalanceSheetAccountDetail.  # noqa: E501

        Accounting code  # noqa: E501

        :return: The code of this BalanceSheetAccountDetail.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BalanceSheetAccountDetail.

        Accounting code  # noqa: E501

        :param code: The code of this BalanceSheetAccountDetail.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def account_id(self):
        """Gets the account_id of this BalanceSheetAccountDetail.  # noqa: E501

        ID of the account  # noqa: E501

        :return: The account_id of this BalanceSheetAccountDetail.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BalanceSheetAccountDetail.

        ID of the account  # noqa: E501

        :param account_id: The account_id of this BalanceSheetAccountDetail.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this BalanceSheetAccountDetail.  # noqa: E501

        Account name  # noqa: E501

        :return: The name of this BalanceSheetAccountDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BalanceSheetAccountDetail.

        Account name  # noqa: E501

        :param name: The name of this BalanceSheetAccountDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reporting_code(self):
        """Gets the reporting_code of this BalanceSheetAccountDetail.  # noqa: E501

        Reporting code  # noqa: E501

        :return: The reporting_code of this BalanceSheetAccountDetail.  # noqa: E501
        :rtype: str
        """
        return self._reporting_code

    @reporting_code.setter
    def reporting_code(self, reporting_code):
        """Sets the reporting_code of this BalanceSheetAccountDetail.

        Reporting code  # noqa: E501

        :param reporting_code: The reporting_code of this BalanceSheetAccountDetail.  # noqa: E501
        :type: str
        """

        self._reporting_code = reporting_code

    @property
    def total(self):
        """Gets the total of this BalanceSheetAccountDetail.  # noqa: E501

        Total movement on this account  # noqa: E501

        :return: The total of this BalanceSheetAccountDetail.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BalanceSheetAccountDetail.

        Total movement on this account  # noqa: E501

        :param total: The total of this BalanceSheetAccountDetail.  # noqa: E501
        :type: float
        """

        self._total = total
