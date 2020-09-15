# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.2.14
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LeavePeriods(BaseModel):
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
        "periods": "list[LeavePeriod]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "periods": "periods",
    }

    def __init__(self, pagination=None, problem=None, periods=None):  # noqa: E501
        """LeavePeriods - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._periods = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if periods is not None:
            self.periods = periods

    @property
    def pagination(self):
        """Gets the pagination of this LeavePeriods.  # noqa: E501


        :return: The pagination of this LeavePeriods.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this LeavePeriods.


        :param pagination: The pagination of this LeavePeriods.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this LeavePeriods.  # noqa: E501


        :return: The problem of this LeavePeriods.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this LeavePeriods.


        :param problem: The problem of this LeavePeriods.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def periods(self):
        """Gets the periods of this LeavePeriods.  # noqa: E501


        :return: The periods of this LeavePeriods.  # noqa: E501
        :rtype: list[LeavePeriod]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this LeavePeriods.


        :param periods: The periods of this LeavePeriods.  # noqa: E501
        :type: list[LeavePeriod]
        """

        self._periods = periods