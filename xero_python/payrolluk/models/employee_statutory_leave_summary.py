# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeeStatutoryLeaveSummary(BaseModel):
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
        "statutory_leave_id": "str",
        "employee_id": "str",
        "type": "str",
        "start_date": "date",
        "end_date": "date",
        "is_entitled": "bool",
        "status": "str",
    }

    attribute_map = {
        "statutory_leave_id": "statutoryLeaveID",
        "employee_id": "employeeID",
        "type": "type",
        "start_date": "startDate",
        "end_date": "endDate",
        "is_entitled": "isEntitled",
        "status": "status",
    }

    def __init__(
        self,
        statutory_leave_id=None,
        employee_id=None,
        type=None,
        start_date=None,
        end_date=None,
        is_entitled=None,
        status=None,
    ):  # noqa: E501
        """EmployeeStatutoryLeaveSummary - a model defined in OpenAPI"""  # noqa: E501

        self._statutory_leave_id = None
        self._employee_id = None
        self._type = None
        self._start_date = None
        self._end_date = None
        self._is_entitled = None
        self._status = None
        self.discriminator = None

        if statutory_leave_id is not None:
            self.statutory_leave_id = statutory_leave_id
        if employee_id is not None:
            self.employee_id = employee_id
        if type is not None:
            self.type = type
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if is_entitled is not None:
            self.is_entitled = is_entitled
        if status is not None:
            self.status = status

    @property
    def statutory_leave_id(self):
        """Gets the statutory_leave_id of this EmployeeStatutoryLeaveSummary.  # noqa: E501

        The unique identifier (guid) of a statutory leave.  # noqa: E501

        :return: The statutory_leave_id of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :rtype: str
        """
        return self._statutory_leave_id

    @statutory_leave_id.setter
    def statutory_leave_id(self, statutory_leave_id):
        """Sets the statutory_leave_id of this EmployeeStatutoryLeaveSummary.

        The unique identifier (guid) of a statutory leave.  # noqa: E501

        :param statutory_leave_id: The statutory_leave_id of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :type: str
        """

        self._statutory_leave_id = statutory_leave_id

    @property
    def employee_id(self):
        """Gets the employee_id of this EmployeeStatutoryLeaveSummary.  # noqa: E501

        The unique identifier (guid) of the employee  # noqa: E501

        :return: The employee_id of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this EmployeeStatutoryLeaveSummary.

        The unique identifier (guid) of the employee  # noqa: E501

        :param employee_id: The employee_id of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def type(self):
        """Gets the type of this EmployeeStatutoryLeaveSummary.  # noqa: E501

        The category of statutory leave  # noqa: E501

        :return: The type of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmployeeStatutoryLeaveSummary.

        The category of statutory leave  # noqa: E501

        :param type: The type of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Sick",
            "Adoption",
            "Maternity",
            "Paternity",
            "Sharedparental",
            "Bereavement",
            "NeonatalCare",
            "None",
        ]  # noqa: E501

        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                        type, allowed_values
                    )
                )

        self._type = type

    @property
    def start_date(self):
        """Gets the start_date of this EmployeeStatutoryLeaveSummary.  # noqa: E501

        The date when the leave starts  # noqa: E501

        :return: The start_date of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EmployeeStatutoryLeaveSummary.

        The date when the leave starts  # noqa: E501

        :param start_date: The start_date of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this EmployeeStatutoryLeaveSummary.  # noqa: E501

        The date when the leave ends  # noqa: E501

        :return: The end_date of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EmployeeStatutoryLeaveSummary.

        The date when the leave ends  # noqa: E501

        :param end_date: The end_date of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def is_entitled(self):
        """Gets the is_entitled of this EmployeeStatutoryLeaveSummary.  # noqa: E501

        Whether the leave was entitled to receive payment  # noqa: E501

        :return: The is_entitled of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :rtype: bool
        """
        return self._is_entitled

    @is_entitled.setter
    def is_entitled(self, is_entitled):
        """Sets the is_entitled of this EmployeeStatutoryLeaveSummary.

        Whether the leave was entitled to receive payment  # noqa: E501

        :param is_entitled: The is_entitled of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :type: bool
        """

        self._is_entitled = is_entitled

    @property
    def status(self):
        """Gets the status of this EmployeeStatutoryLeaveSummary.  # noqa: E501

        The status of the leave  # noqa: E501

        :return: The status of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EmployeeStatutoryLeaveSummary.

        The status of the leave  # noqa: E501

        :param status: The status of this EmployeeStatutoryLeaveSummary.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "In-Progress", "Completed", "None"]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status
