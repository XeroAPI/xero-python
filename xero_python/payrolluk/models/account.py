# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.3.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Account(BaseModel):
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
    openapi_types = {"account_id": "str", "type": "str", "code": "str", "name": "str"}

    attribute_map = {
        "account_id": "accountID",
        "type": "type",
        "code": "code",
        "name": "name",
    }

    def __init__(self, account_id=None, type=None, code=None, name=None):  # noqa: E501
        """Account - a model defined in OpenAPI"""  # noqa: E501

        self._account_id = None
        self._type = None
        self._code = None
        self._name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if type is not None:
            self.type = type
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name

    @property
    def account_id(self):
        """Gets the account_id of this Account.  # noqa: E501

        The Xero identifier for Settings.  # noqa: E501

        :return: The account_id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Account.

        The Xero identifier for Settings.  # noqa: E501

        :param account_id: The account_id of this Account.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def type(self):
        """Gets the type of this Account.  # noqa: E501

        The assigned AccountType  # noqa: E501

        :return: The type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Account.

        The assigned AccountType  # noqa: E501

        :param type: The type of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "BANK",
            "EMPLOYERSNIC",
            "NICLIABILITY",
            "PAYEECONTRIBUTION",
            "PAYELIABILITY",
            "WAGESPAYABLE",
            "WAGESEXPENSE",
            "None",
        ]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def code(self):
        """Gets the code of this Account.  # noqa: E501

        A unique 3 digit number for each Account  # noqa: E501

        :return: The code of this Account.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Account.

        A unique 3 digit number for each Account  # noqa: E501

        :param code: The code of this Account.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501

        Name of the Account.  # noqa: E501

        :return: The name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.

        Name of the Account.  # noqa: E501

        :param name: The name of this Account.  # noqa: E501
        :type: str
        """

        self._name = name
