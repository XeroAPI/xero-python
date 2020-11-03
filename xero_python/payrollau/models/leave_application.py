# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.3.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LeaveApplication(BaseModel):
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
        "leave_application_id": "str",
        "employee_id": "str",
        "leave_type_id": "str",
        "title": "str",
        "start_date": "date[ms-format]",
        "end_date": "date[ms-format]",
        "description": "str",
        "leave_periods": "list[LeavePeriod]",
        "updated_date_utc": "datetime[ms-format]",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "leave_application_id": "LeaveApplicationID",
        "employee_id": "EmployeeID",
        "leave_type_id": "LeaveTypeID",
        "title": "Title",
        "start_date": "StartDate",
        "end_date": "EndDate",
        "description": "Description",
        "leave_periods": "LeavePeriods",
        "updated_date_utc": "UpdatedDateUTC",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        leave_application_id=None,
        employee_id=None,
        leave_type_id=None,
        title=None,
        start_date=None,
        end_date=None,
        description=None,
        leave_periods=None,
        updated_date_utc=None,
        validation_errors=None,
    ):  # noqa: E501
        """LeaveApplication - a model defined in OpenAPI"""  # noqa: E501

        self._leave_application_id = None
        self._employee_id = None
        self._leave_type_id = None
        self._title = None
        self._start_date = None
        self._end_date = None
        self._description = None
        self._leave_periods = None
        self._updated_date_utc = None
        self._validation_errors = None
        self.discriminator = None

        if leave_application_id is not None:
            self.leave_application_id = leave_application_id
        if employee_id is not None:
            self.employee_id = employee_id
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if title is not None:
            self.title = title
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if description is not None:
            self.description = description
        if leave_periods is not None:
            self.leave_periods = leave_periods
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def leave_application_id(self):
        """Gets the leave_application_id of this LeaveApplication.  # noqa: E501

        The Xero identifier for Payroll Employee  # noqa: E501

        :return: The leave_application_id of this LeaveApplication.  # noqa: E501
        :rtype: str
        """
        return self._leave_application_id

    @leave_application_id.setter
    def leave_application_id(self, leave_application_id):
        """Sets the leave_application_id of this LeaveApplication.

        The Xero identifier for Payroll Employee  # noqa: E501

        :param leave_application_id: The leave_application_id of this LeaveApplication.  # noqa: E501
        :type: str
        """

        self._leave_application_id = leave_application_id

    @property
    def employee_id(self):
        """Gets the employee_id of this LeaveApplication.  # noqa: E501

        The Xero identifier for Payroll Employee  # noqa: E501

        :return: The employee_id of this LeaveApplication.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this LeaveApplication.

        The Xero identifier for Payroll Employee  # noqa: E501

        :param employee_id: The employee_id of this LeaveApplication.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this LeaveApplication.  # noqa: E501

        The Xero identifier for Leave Type  # noqa: E501

        :return: The leave_type_id of this LeaveApplication.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this LeaveApplication.

        The Xero identifier for Leave Type  # noqa: E501

        :param leave_type_id: The leave_type_id of this LeaveApplication.  # noqa: E501
        :type: str
        """

        self._leave_type_id = leave_type_id

    @property
    def title(self):
        """Gets the title of this LeaveApplication.  # noqa: E501

        The title of the leave  # noqa: E501

        :return: The title of this LeaveApplication.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LeaveApplication.

        The title of the leave  # noqa: E501

        :param title: The title of this LeaveApplication.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def start_date(self):
        """Gets the start_date of this LeaveApplication.  # noqa: E501

        Start date of the leave (YYYY-MM-DD)  # noqa: E501

        :return: The start_date of this LeaveApplication.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this LeaveApplication.

        Start date of the leave (YYYY-MM-DD)  # noqa: E501

        :param start_date: The start_date of this LeaveApplication.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this LeaveApplication.  # noqa: E501

        End date of the leave (YYYY-MM-DD)  # noqa: E501

        :return: The end_date of this LeaveApplication.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this LeaveApplication.

        End date of the leave (YYYY-MM-DD)  # noqa: E501

        :param end_date: The end_date of this LeaveApplication.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def description(self):
        """Gets the description of this LeaveApplication.  # noqa: E501

        The Description of the Leave  # noqa: E501

        :return: The description of this LeaveApplication.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LeaveApplication.

        The Description of the Leave  # noqa: E501

        :param description: The description of this LeaveApplication.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def leave_periods(self):
        """Gets the leave_periods of this LeaveApplication.  # noqa: E501


        :return: The leave_periods of this LeaveApplication.  # noqa: E501
        :rtype: list[LeavePeriod]
        """
        return self._leave_periods

    @leave_periods.setter
    def leave_periods(self, leave_periods):
        """Sets the leave_periods of this LeaveApplication.


        :param leave_periods: The leave_periods of this LeaveApplication.  # noqa: E501
        :type: list[LeavePeriod]
        """

        self._leave_periods = leave_periods

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this LeaveApplication.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The updated_date_utc of this LeaveApplication.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this LeaveApplication.

        Last modified timestamp  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this LeaveApplication.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def validation_errors(self):
        """Gets the validation_errors of this LeaveApplication.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this LeaveApplication.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this LeaveApplication.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this LeaveApplication.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors
