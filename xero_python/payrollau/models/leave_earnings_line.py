# coding: utf-8

"""
Xero Payroll AU API

This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LeaveEarningsLine(BaseModel):
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
        "earnings_rate_id": "str",
        "rate_per_unit": "float",
        "number_of_units": "float",
        "pay_out_type": "PayOutType",
    }

    attribute_map = {
        "earnings_rate_id": "EarningsRateID",
        "rate_per_unit": "RatePerUnit",
        "number_of_units": "NumberOfUnits",
        "pay_out_type": "PayOutType",
    }

    def __init__(
        self,
        earnings_rate_id=None,
        rate_per_unit=None,
        number_of_units=None,
        pay_out_type=None,
    ):  # noqa: E501
        """LeaveEarningsLine - a model defined in OpenAPI"""  # noqa: E501

        self._earnings_rate_id = None
        self._rate_per_unit = None
        self._number_of_units = None
        self._pay_out_type = None
        self.discriminator = None

        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if pay_out_type is not None:
            self.pay_out_type = pay_out_type

    @property
    def earnings_rate_id(self):
        """Gets the earnings_rate_id of this LeaveEarningsLine.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The earnings_rate_id of this LeaveEarningsLine.  # noqa: E501
        :rtype: str
        """
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        """Sets the earnings_rate_id of this LeaveEarningsLine.

        Xero identifier  # noqa: E501

        :param earnings_rate_id: The earnings_rate_id of this LeaveEarningsLine.  # noqa: E501
        :type: str
        """

        self._earnings_rate_id = earnings_rate_id

    @property
    def rate_per_unit(self):
        """Gets the rate_per_unit of this LeaveEarningsLine.  # noqa: E501

        Rate per unit of the EarningsLine.  # noqa: E501

        :return: The rate_per_unit of this LeaveEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        """Sets the rate_per_unit of this LeaveEarningsLine.

        Rate per unit of the EarningsLine.  # noqa: E501

        :param rate_per_unit: The rate_per_unit of this LeaveEarningsLine.  # noqa: E501
        :type: float
        """

        self._rate_per_unit = rate_per_unit

    @property
    def number_of_units(self):
        """Gets the number_of_units of this LeaveEarningsLine.  # noqa: E501

        Earnings rate number of units.  # noqa: E501

        :return: The number_of_units of this LeaveEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this LeaveEarningsLine.

        Earnings rate number of units.  # noqa: E501

        :param number_of_units: The number_of_units of this LeaveEarningsLine.  # noqa: E501
        :type: float
        """

        self._number_of_units = number_of_units

    @property
    def pay_out_type(self):
        """Gets the pay_out_type of this LeaveEarningsLine.  # noqa: E501


        :return: The pay_out_type of this LeaveEarningsLine.  # noqa: E501
        :rtype: PayOutType
        """
        return self._pay_out_type

    @pay_out_type.setter
    def pay_out_type(self, pay_out_type):
        """Sets the pay_out_type of this LeaveEarningsLine.


        :param pay_out_type: The pay_out_type of this LeaveEarningsLine.  # noqa: E501
        :type: PayOutType
        """

        self._pay_out_type = pay_out_type
