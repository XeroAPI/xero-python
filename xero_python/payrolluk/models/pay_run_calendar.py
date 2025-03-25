# coding: utf-8

"""
Xero Payroll UK

This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PayRunCalendar(BaseModel):
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
        "name": "str",
        "calendar_type": "str",
        "period_start_date": "date",
        "period_end_date": "date",
        "payment_date": "date",
        "updated_date_utc": "datetime",
    }

    attribute_map = {
        "payroll_calendar_id": "payrollCalendarID",
        "name": "name",
        "calendar_type": "calendarType",
        "period_start_date": "periodStartDate",
        "period_end_date": "periodEndDate",
        "payment_date": "paymentDate",
        "updated_date_utc": "updatedDateUTC",
    }

    def __init__(
        self,
        payroll_calendar_id=None,
        name=None,
        calendar_type=None,
        period_start_date=None,
        period_end_date=None,
        payment_date=None,
        updated_date_utc=None,
    ):  # noqa: E501
        """PayRunCalendar - a model defined in OpenAPI"""  # noqa: E501

        self._payroll_calendar_id = None
        self._name = None
        self._calendar_type = None
        self._period_start_date = None
        self._period_end_date = None
        self._payment_date = None
        self._updated_date_utc = None
        self.discriminator = None

        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        self.name = name
        self.calendar_type = calendar_type
        self.period_start_date = period_start_date
        if period_end_date is not None:
            self.period_end_date = period_end_date
        self.payment_date = payment_date
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def payroll_calendar_id(self):
        """Gets the payroll_calendar_id of this PayRunCalendar.  # noqa: E501

        Xero unique identifier for the payroll calendar  # noqa: E501

        :return: The payroll_calendar_id of this PayRunCalendar.  # noqa: E501
        :rtype: str
        """
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        """Sets the payroll_calendar_id of this PayRunCalendar.

        Xero unique identifier for the payroll calendar  # noqa: E501

        :param payroll_calendar_id: The payroll_calendar_id of this PayRunCalendar.  # noqa: E501
        :type: str
        """

        self._payroll_calendar_id = payroll_calendar_id

    @property
    def name(self):
        """Gets the name of this PayRunCalendar.  # noqa: E501

        Name of the calendar  # noqa: E501

        :return: The name of this PayRunCalendar.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PayRunCalendar.

        Name of the calendar  # noqa: E501

        :param name: The name of this PayRunCalendar.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def calendar_type(self):
        """Gets the calendar_type of this PayRunCalendar.  # noqa: E501

        Type of the calendar  # noqa: E501

        :return: The calendar_type of this PayRunCalendar.  # noqa: E501
        :rtype: str
        """
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        """Sets the calendar_type of this PayRunCalendar.

        Type of the calendar  # noqa: E501

        :param calendar_type: The calendar_type of this PayRunCalendar.  # noqa: E501
        :type: str
        """
        if calendar_type is None:
            raise ValueError(
                "Invalid value for `calendar_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "Weekly",
            "Fortnightly",
            "FourWeekly",
            "Monthly",
            "Annual",
            "Quarterly",
            "None",
        ]  # noqa: E501

        if calendar_type:
            if calendar_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `calendar_type` ({0}), must be one of {1}".format(  # noqa: E501
                        calendar_type, allowed_values
                    )
                )

        self._calendar_type = calendar_type

    @property
    def period_start_date(self):
        """Gets the period_start_date of this PayRunCalendar.  # noqa: E501

        Period start date of the calendar  # noqa: E501

        :return: The period_start_date of this PayRunCalendar.  # noqa: E501
        :rtype: date
        """
        return self._period_start_date

    @period_start_date.setter
    def period_start_date(self, period_start_date):
        """Sets the period_start_date of this PayRunCalendar.

        Period start date of the calendar  # noqa: E501

        :param period_start_date: The period_start_date of this PayRunCalendar.  # noqa: E501
        :type: date
        """
        if period_start_date is None:
            raise ValueError(
                "Invalid value for `period_start_date`, must not be `None`"
            )  # noqa: E501

        self._period_start_date = period_start_date

    @property
    def period_end_date(self):
        """Gets the period_end_date of this PayRunCalendar.  # noqa: E501

        Period end date of the calendar  # noqa: E501

        :return: The period_end_date of this PayRunCalendar.  # noqa: E501
        :rtype: date
        """
        return self._period_end_date

    @period_end_date.setter
    def period_end_date(self, period_end_date):
        """Sets the period_end_date of this PayRunCalendar.

        Period end date of the calendar  # noqa: E501

        :param period_end_date: The period_end_date of this PayRunCalendar.  # noqa: E501
        :type: date
        """

        self._period_end_date = period_end_date

    @property
    def payment_date(self):
        """Gets the payment_date of this PayRunCalendar.  # noqa: E501

        Payment date of the calendar  # noqa: E501

        :return: The payment_date of this PayRunCalendar.  # noqa: E501
        :rtype: date
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this PayRunCalendar.

        Payment date of the calendar  # noqa: E501

        :param payment_date: The payment_date of this PayRunCalendar.  # noqa: E501
        :type: date
        """
        if payment_date is None:
            raise ValueError(
                "Invalid value for `payment_date`, must not be `None`"
            )  # noqa: E501

        self._payment_date = payment_date

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this PayRunCalendar.  # noqa: E501

        UTC timestamp of the last update to the pay run calendar  # noqa: E501

        :return: The updated_date_utc of this PayRunCalendar.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this PayRunCalendar.

        UTC timestamp of the last update to the pay run calendar  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this PayRunCalendar.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc
