# coding: utf-8

"""
Xero Payroll AU API

This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LeaveType(BaseModel):
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
        "name": "str",
        "type_of_units": "str",
        "leave_type_id": "str",
        "normal_entitlement": "float",
        "leave_loading_rate": "float",
        "updated_date_utc": "datetime[ms-format]",
        "is_paid_leave": "bool",
        "show_on_payslip": "bool",
        "current_record": "bool",
        "leave_category_code": "LeaveCategoryCode",
        "sgc_exempt": "bool",
    }

    attribute_map = {
        "name": "Name",
        "type_of_units": "TypeOfUnits",
        "leave_type_id": "LeaveTypeID",
        "normal_entitlement": "NormalEntitlement",
        "leave_loading_rate": "LeaveLoadingRate",
        "updated_date_utc": "UpdatedDateUTC",
        "is_paid_leave": "IsPaidLeave",
        "show_on_payslip": "ShowOnPayslip",
        "current_record": "CurrentRecord",
        "leave_category_code": "LeaveCategoryCode",
        "sgc_exempt": "SGCExempt",
    }

    def __init__(
        self,
        name=None,
        type_of_units=None,
        leave_type_id=None,
        normal_entitlement=None,
        leave_loading_rate=None,
        updated_date_utc=None,
        is_paid_leave=None,
        show_on_payslip=None,
        current_record=None,
        leave_category_code=None,
        sgc_exempt=None,
    ):  # noqa: E501
        """LeaveType - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._type_of_units = None
        self._leave_type_id = None
        self._normal_entitlement = None
        self._leave_loading_rate = None
        self._updated_date_utc = None
        self._is_paid_leave = None
        self._show_on_payslip = None
        self._current_record = None
        self._leave_category_code = None
        self._sgc_exempt = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type_of_units is not None:
            self.type_of_units = type_of_units
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if normal_entitlement is not None:
            self.normal_entitlement = normal_entitlement
        if leave_loading_rate is not None:
            self.leave_loading_rate = leave_loading_rate
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if is_paid_leave is not None:
            self.is_paid_leave = is_paid_leave
        if show_on_payslip is not None:
            self.show_on_payslip = show_on_payslip
        if current_record is not None:
            self.current_record = current_record
        if leave_category_code is not None:
            self.leave_category_code = leave_category_code
        if sgc_exempt is not None:
            self.sgc_exempt = sgc_exempt

    @property
    def name(self):
        """Gets the name of this LeaveType.  # noqa: E501

        Name of the earnings rate (max length = 100)  # noqa: E501

        :return: The name of this LeaveType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LeaveType.

        Name of the earnings rate (max length = 100)  # noqa: E501

        :param name: The name of this LeaveType.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, "
                "length must be less than or equal to `100`"
            )  # noqa: E501

        self._name = name

    @property
    def type_of_units(self):
        """Gets the type_of_units of this LeaveType.  # noqa: E501

        The type of units by which leave entitlements are normally tracked. These are typically the same as the type of units used for the employee’s ordinary earnings rate  # noqa: E501

        :return: The type_of_units of this LeaveType.  # noqa: E501
        :rtype: str
        """
        return self._type_of_units

    @type_of_units.setter
    def type_of_units(self, type_of_units):
        """Sets the type_of_units of this LeaveType.

        The type of units by which leave entitlements are normally tracked. These are typically the same as the type of units used for the employee’s ordinary earnings rate  # noqa: E501

        :param type_of_units: The type_of_units of this LeaveType.  # noqa: E501
        :type: str
        """

        self._type_of_units = type_of_units

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this LeaveType.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The leave_type_id of this LeaveType.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this LeaveType.

        Xero identifier  # noqa: E501

        :param leave_type_id: The leave_type_id of this LeaveType.  # noqa: E501
        :type: str
        """

        self._leave_type_id = leave_type_id

    @property
    def normal_entitlement(self):
        """Gets the normal_entitlement of this LeaveType.  # noqa: E501

        The number of units the employee is entitled to each year  # noqa: E501

        :return: The normal_entitlement of this LeaveType.  # noqa: E501
        :rtype: float
        """
        return self._normal_entitlement

    @normal_entitlement.setter
    def normal_entitlement(self, normal_entitlement):
        """Sets the normal_entitlement of this LeaveType.

        The number of units the employee is entitled to each year  # noqa: E501

        :param normal_entitlement: The normal_entitlement of this LeaveType.  # noqa: E501
        :type: float
        """

        self._normal_entitlement = normal_entitlement

    @property
    def leave_loading_rate(self):
        """Gets the leave_loading_rate of this LeaveType.  # noqa: E501

        Enter an amount here if your organisation pays an additional percentage on top of ordinary earnings when your employees take leave (typically 17.5%)  # noqa: E501

        :return: The leave_loading_rate of this LeaveType.  # noqa: E501
        :rtype: float
        """
        return self._leave_loading_rate

    @leave_loading_rate.setter
    def leave_loading_rate(self, leave_loading_rate):
        """Sets the leave_loading_rate of this LeaveType.

        Enter an amount here if your organisation pays an additional percentage on top of ordinary earnings when your employees take leave (typically 17.5%)  # noqa: E501

        :param leave_loading_rate: The leave_loading_rate of this LeaveType.  # noqa: E501
        :type: float
        """

        self._leave_loading_rate = leave_loading_rate

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this LeaveType.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The updated_date_utc of this LeaveType.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this LeaveType.

        Last modified timestamp  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this LeaveType.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def is_paid_leave(self):
        """Gets the is_paid_leave of this LeaveType.  # noqa: E501

        Set this to indicate that an employee will be paid when taking this type of leave  # noqa: E501

        :return: The is_paid_leave of this LeaveType.  # noqa: E501
        :rtype: bool
        """
        return self._is_paid_leave

    @is_paid_leave.setter
    def is_paid_leave(self, is_paid_leave):
        """Sets the is_paid_leave of this LeaveType.

        Set this to indicate that an employee will be paid when taking this type of leave  # noqa: E501

        :param is_paid_leave: The is_paid_leave of this LeaveType.  # noqa: E501
        :type: bool
        """

        self._is_paid_leave = is_paid_leave

    @property
    def show_on_payslip(self):
        """Gets the show_on_payslip of this LeaveType.  # noqa: E501

        Set this if you want a balance for this leave type to be shown on your employee’s payslips  # noqa: E501

        :return: The show_on_payslip of this LeaveType.  # noqa: E501
        :rtype: bool
        """
        return self._show_on_payslip

    @show_on_payslip.setter
    def show_on_payslip(self, show_on_payslip):
        """Sets the show_on_payslip of this LeaveType.

        Set this if you want a balance for this leave type to be shown on your employee’s payslips  # noqa: E501

        :param show_on_payslip: The show_on_payslip of this LeaveType.  # noqa: E501
        :type: bool
        """

        self._show_on_payslip = show_on_payslip

    @property
    def current_record(self):
        """Gets the current_record of this LeaveType.  # noqa: E501

        Is the current record  # noqa: E501

        :return: The current_record of this LeaveType.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this LeaveType.

        Is the current record  # noqa: E501

        :param current_record: The current_record of this LeaveType.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record

    @property
    def leave_category_code(self):
        """Gets the leave_category_code of this LeaveType.  # noqa: E501


        :return: The leave_category_code of this LeaveType.  # noqa: E501
        :rtype: LeaveCategoryCode
        """
        return self._leave_category_code

    @leave_category_code.setter
    def leave_category_code(self, leave_category_code):
        """Sets the leave_category_code of this LeaveType.


        :param leave_category_code: The leave_category_code of this LeaveType.  # noqa: E501
        :type: LeaveCategoryCode
        """

        self._leave_category_code = leave_category_code

    @property
    def sgc_exempt(self):
        """Gets the sgc_exempt of this LeaveType.  # noqa: E501

        Set this to indicate that the leave type is exempt from superannuation guarantee contribution  # noqa: E501

        :return: The sgc_exempt of this LeaveType.  # noqa: E501
        :rtype: bool
        """
        return self._sgc_exempt

    @sgc_exempt.setter
    def sgc_exempt(self, sgc_exempt):
        """Sets the sgc_exempt of this LeaveType.

        Set this to indicate that the leave type is exempt from superannuation guarantee contribution  # noqa: E501

        :param sgc_exempt: The sgc_exempt of this LeaveType.  # noqa: E501
        :type: bool
        """

        self._sgc_exempt = sgc_exempt
