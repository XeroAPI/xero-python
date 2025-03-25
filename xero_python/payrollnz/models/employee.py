# coding: utf-8

"""
Xero Payroll NZ

This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Employee(BaseModel):
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
        "employee_id": "str",
        "title": "str",
        "first_name": "str",
        "last_name": "str",
        "date_of_birth": "date",
        "address": "Address",
        "email": "str",
        "gender": "str",
        "phone_number": "str",
        "start_date": "date",
        "end_date": "date",
        "payroll_calendar_id": "str",
        "updated_date_utc": "datetime",
        "created_date_utc": "datetime",
        "job_title": "str",
        "engagement_type": "str",
        "fixed_term_end_date": "date",
    }

    attribute_map = {
        "employee_id": "employeeID",
        "title": "title",
        "first_name": "firstName",
        "last_name": "lastName",
        "date_of_birth": "dateOfBirth",
        "address": "address",
        "email": "email",
        "gender": "gender",
        "phone_number": "phoneNumber",
        "start_date": "startDate",
        "end_date": "endDate",
        "payroll_calendar_id": "payrollCalendarID",
        "updated_date_utc": "updatedDateUTC",
        "created_date_utc": "createdDateUTC",
        "job_title": "jobTitle",
        "engagement_type": "engagementType",
        "fixed_term_end_date": "fixedTermEndDate",
    }

    def __init__(
        self,
        employee_id=None,
        title=None,
        first_name=None,
        last_name=None,
        date_of_birth=None,
        address=None,
        email=None,
        gender=None,
        phone_number=None,
        start_date=None,
        end_date=None,
        payroll_calendar_id=None,
        updated_date_utc=None,
        created_date_utc=None,
        job_title=None,
        engagement_type=None,
        fixed_term_end_date=None,
    ):  # noqa: E501
        """Employee - a model defined in OpenAPI"""  # noqa: E501

        self._employee_id = None
        self._title = None
        self._first_name = None
        self._last_name = None
        self._date_of_birth = None
        self._address = None
        self._email = None
        self._gender = None
        self._phone_number = None
        self._start_date = None
        self._end_date = None
        self._payroll_calendar_id = None
        self._updated_date_utc = None
        self._created_date_utc = None
        self._job_title = None
        self._engagement_type = None
        self._fixed_term_end_date = None
        self.discriminator = None

        if employee_id is not None:
            self.employee_id = employee_id
        if title is not None:
            self.title = title
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if address is not None:
            self.address = address
        if email is not None:
            self.email = email
        if gender is not None:
            self.gender = gender
        if phone_number is not None:
            self.phone_number = phone_number
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc
        if job_title is not None:
            self.job_title = job_title
        if engagement_type is not None:
            self.engagement_type = engagement_type
        if fixed_term_end_date is not None:
            self.fixed_term_end_date = fixed_term_end_date

    @property
    def employee_id(self):
        """Gets the employee_id of this Employee.  # noqa: E501

        Xero unique identifier for the employee  # noqa: E501

        :return: The employee_id of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this Employee.

        Xero unique identifier for the employee  # noqa: E501

        :param employee_id: The employee_id of this Employee.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def title(self):
        """Gets the title of this Employee.  # noqa: E501

        Title of the employee  # noqa: E501

        :return: The title of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Employee.

        Title of the employee  # noqa: E501

        :param title: The title of this Employee.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def first_name(self):
        """Gets the first_name of this Employee.  # noqa: E501

        First name of employee  # noqa: E501

        :return: The first_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Employee.

        First name of employee  # noqa: E501

        :param first_name: The first_name of this Employee.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Employee.  # noqa: E501

        Last name of employee  # noqa: E501

        :return: The last_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Employee.

        Last name of employee  # noqa: E501

        :param last_name: The last_name of this Employee.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this Employee.  # noqa: E501

        Date of birth of the employee (YYYY-MM-DD)  # noqa: E501

        :return: The date_of_birth of this Employee.  # noqa: E501
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this Employee.

        Date of birth of the employee (YYYY-MM-DD)  # noqa: E501

        :param date_of_birth: The date_of_birth of this Employee.  # noqa: E501
        :type: date
        """

        self._date_of_birth = date_of_birth

    @property
    def address(self):
        """Gets the address of this Employee.  # noqa: E501


        :return: The address of this Employee.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Employee.


        :param address: The address of this Employee.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def email(self):
        """Gets the email of this Employee.  # noqa: E501

        The email address for the employee  # noqa: E501

        :return: The email of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Employee.

        The email address for the employee  # noqa: E501

        :param email: The email of this Employee.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def gender(self):
        """Gets the gender of this Employee.  # noqa: E501

        The employee’s gender  # noqa: E501

        :return: The gender of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Employee.

        The employee’s gender  # noqa: E501

        :param gender: The gender of this Employee.  # noqa: E501
        :type: str
        """
        allowed_values = ["M", "F", "None"]  # noqa: E501

        if gender:
            if gender not in allowed_values:
                raise ValueError(
                    "Invalid value for `gender` ({0}), must be one of {1}".format(  # noqa: E501
                        gender, allowed_values
                    )
                )

        self._gender = gender

    @property
    def phone_number(self):
        """Gets the phone_number of this Employee.  # noqa: E501

        Employee phone number  # noqa: E501

        :return: The phone_number of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Employee.

        Employee phone number  # noqa: E501

        :param phone_number: The phone_number of this Employee.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def start_date(self):
        """Gets the start_date of this Employee.  # noqa: E501

        Employment start date of the employee at the time it was requested  # noqa: E501

        :return: The start_date of this Employee.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Employee.

        Employment start date of the employee at the time it was requested  # noqa: E501

        :param start_date: The start_date of this Employee.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Employee.  # noqa: E501

        Employment end date of the employee at the time it was requested  # noqa: E501

        :return: The end_date of this Employee.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Employee.

        Employment end date of the employee at the time it was requested  # noqa: E501

        :param end_date: The end_date of this Employee.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def payroll_calendar_id(self):
        """Gets the payroll_calendar_id of this Employee.  # noqa: E501

        Xero unique identifier for the payroll calendar of the employee  # noqa: E501

        :return: The payroll_calendar_id of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        """Sets the payroll_calendar_id of this Employee.

        Xero unique identifier for the payroll calendar of the employee  # noqa: E501

        :param payroll_calendar_id: The payroll_calendar_id of this Employee.  # noqa: E501
        :type: str
        """

        self._payroll_calendar_id = payroll_calendar_id

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Employee.  # noqa: E501

        UTC timestamp of last update to the employee  # noqa: E501

        :return: The updated_date_utc of this Employee.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Employee.

        UTC timestamp of last update to the employee  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Employee.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def created_date_utc(self):
        """Gets the created_date_utc of this Employee.  # noqa: E501

        UTC timestamp when the employee was created in Xero  # noqa: E501

        :return: The created_date_utc of this Employee.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        """Sets the created_date_utc of this Employee.

        UTC timestamp when the employee was created in Xero  # noqa: E501

        :param created_date_utc: The created_date_utc of this Employee.  # noqa: E501
        :type: datetime
        """

        self._created_date_utc = created_date_utc

    @property
    def job_title(self):
        """Gets the job_title of this Employee.  # noqa: E501

        Employee's job title  # noqa: E501

        :return: The job_title of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this Employee.

        Employee's job title  # noqa: E501

        :param job_title: The job_title of this Employee.  # noqa: E501
        :type: str
        """

        self._job_title = job_title

    @property
    def engagement_type(self):
        """Gets the engagement_type of this Employee.  # noqa: E501

        Engagement type of the employee  # noqa: E501

        :return: The engagement_type of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._engagement_type

    @engagement_type.setter
    def engagement_type(self, engagement_type):
        """Sets the engagement_type of this Employee.

        Engagement type of the employee  # noqa: E501

        :param engagement_type: The engagement_type of this Employee.  # noqa: E501
        :type: str
        """

        self._engagement_type = engagement_type

    @property
    def fixed_term_end_date(self):
        """Gets the fixed_term_end_date of this Employee.  # noqa: E501

        End date for an employee with a fixed-term engagement type  # noqa: E501

        :return: The fixed_term_end_date of this Employee.  # noqa: E501
        :rtype: date
        """
        return self._fixed_term_end_date

    @fixed_term_end_date.setter
    def fixed_term_end_date(self, fixed_term_end_date):
        """Sets the fixed_term_end_date of this Employee.

        End date for an employee with a fixed-term engagement type  # noqa: E501

        :param fixed_term_end_date: The fixed_term_end_date of this Employee.  # noqa: E501
        :type: date
        """

        self._fixed_term_end_date = fixed_term_end_date
