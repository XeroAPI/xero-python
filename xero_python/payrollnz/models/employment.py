# coding: utf-8

"""
Xero Payroll NZ

This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Employment(BaseModel):
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
        "payroll_calendar_id": "str",
        "pay_run_calendar_id": "str",
        "start_date": "date",
        "engagement_type": "str",
        "fixed_term_end_date": "date",
    }

    attribute_map = {
        "payroll_calendar_id": "payrollCalendarID",
        "pay_run_calendar_id": "payRunCalendarID",
        "start_date": "startDate",
        "engagement_type": "engagementType",
        "fixed_term_end_date": "fixedTermEndDate",
    }

    def __init__(
        self,
        payroll_calendar_id=None,
        pay_run_calendar_id=None,
        start_date=None,
        engagement_type=None,
        fixed_term_end_date=None,
    ):  # noqa: E501
        """Employment - a model defined in OpenAPI"""  # noqa: E501

        self._payroll_calendar_id = None
        self._pay_run_calendar_id = None
        self._start_date = None
        self._engagement_type = None
        self._fixed_term_end_date = None
        self.discriminator = None

        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if pay_run_calendar_id is not None:
            self.pay_run_calendar_id = pay_run_calendar_id
        if start_date is not None:
            self.start_date = start_date
        if engagement_type is not None:
            self.engagement_type = engagement_type
        if fixed_term_end_date is not None:
            self.fixed_term_end_date = fixed_term_end_date

    @property
    def payroll_calendar_id(self):
        """Gets the payroll_calendar_id of this Employment.  # noqa: E501

        Xero unique identifier for the payroll calendar of the employee  # noqa: E501

        :return: The payroll_calendar_id of this Employment.  # noqa: E501
        :rtype: str
        """
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        """Sets the payroll_calendar_id of this Employment.

        Xero unique identifier for the payroll calendar of the employee  # noqa: E501

        :param payroll_calendar_id: The payroll_calendar_id of this Employment.  # noqa: E501
        :type: str
        """

        self._payroll_calendar_id = payroll_calendar_id

    @property
    def pay_run_calendar_id(self):
        """Gets the pay_run_calendar_id of this Employment.  # noqa: E501

        Xero unique identifier for the payrun calendar for the employee (Deprecated in version 1.1.6)  # noqa: E501

        :return: The pay_run_calendar_id of this Employment.  # noqa: E501
        :rtype: str
        """
        return self._pay_run_calendar_id

    @pay_run_calendar_id.setter
    def pay_run_calendar_id(self, pay_run_calendar_id):
        """Sets the pay_run_calendar_id of this Employment.

        Xero unique identifier for the payrun calendar for the employee (Deprecated in version 1.1.6)  # noqa: E501

        :param pay_run_calendar_id: The pay_run_calendar_id of this Employment.  # noqa: E501
        :type: str
        """

        self._pay_run_calendar_id = pay_run_calendar_id

    @property
    def start_date(self):
        """Gets the start_date of this Employment.  # noqa: E501

        Start date of the employment (YYYY-MM-DD)  # noqa: E501

        :return: The start_date of this Employment.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Employment.

        Start date of the employment (YYYY-MM-DD)  # noqa: E501

        :param start_date: The start_date of this Employment.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def engagement_type(self):
        """Gets the engagement_type of this Employment.  # noqa: E501

        Engagement type of the employee  # noqa: E501

        :return: The engagement_type of this Employment.  # noqa: E501
        :rtype: str
        """
        return self._engagement_type

    @engagement_type.setter
    def engagement_type(self, engagement_type):
        """Sets the engagement_type of this Employment.

        Engagement type of the employee  # noqa: E501

        :param engagement_type: The engagement_type of this Employment.  # noqa: E501
        :type: str
        """

        self._engagement_type = engagement_type

    @property
    def fixed_term_end_date(self):
        """Gets the fixed_term_end_date of this Employment.  # noqa: E501

        End date for an employee with a fixed-term engagement type  # noqa: E501

        :return: The fixed_term_end_date of this Employment.  # noqa: E501
        :rtype: date
        """
        return self._fixed_term_end_date

    @fixed_term_end_date.setter
    def fixed_term_end_date(self, fixed_term_end_date):
        """Sets the fixed_term_end_date of this Employment.

        End date for an employee with a fixed-term engagement type  # noqa: E501

        :param fixed_term_end_date: The fixed_term_end_date of this Employment.  # noqa: E501
        :type: date
        """

        self._fixed_term_end_date = fixed_term_end_date
