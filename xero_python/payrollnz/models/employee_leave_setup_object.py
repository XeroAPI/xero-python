# coding: utf-8

"""
Xero Payroll NZ

This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeeLeaveSetupObject(BaseModel):
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
        "pagination": "Pagination",
        "problem": "Problem",
        "leave_setup": "EmployeeLeaveSetup",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "leave_setup": "leaveSetup",
    }

    def __init__(self, pagination=None, problem=None, leave_setup=None):  # noqa: E501
        """EmployeeLeaveSetupObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._leave_setup = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave_setup is not None:
            self.leave_setup = leave_setup

    @property
    def pagination(self):
        """Gets the pagination of this EmployeeLeaveSetupObject.  # noqa: E501


        :return: The pagination of this EmployeeLeaveSetupObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeeLeaveSetupObject.


        :param pagination: The pagination of this EmployeeLeaveSetupObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EmployeeLeaveSetupObject.  # noqa: E501


        :return: The problem of this EmployeeLeaveSetupObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeeLeaveSetupObject.


        :param problem: The problem of this EmployeeLeaveSetupObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def leave_setup(self):
        """Gets the leave_setup of this EmployeeLeaveSetupObject.  # noqa: E501


        :return: The leave_setup of this EmployeeLeaveSetupObject.  # noqa: E501
        :rtype: EmployeeLeaveSetup
        """
        return self._leave_setup

    @leave_setup.setter
    def leave_setup(self, leave_setup):
        """Sets the leave_setup of this EmployeeLeaveSetupObject.


        :param leave_setup: The leave_setup of this EmployeeLeaveSetupObject.  # noqa: E501
        :type: EmployeeLeaveSetup
        """

        self._leave_setup = leave_setup
