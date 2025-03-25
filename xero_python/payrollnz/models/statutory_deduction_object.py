# coding: utf-8

"""
Xero Payroll NZ

This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class StatutoryDeductionObject(BaseModel):
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
        "statutory_deduction": "StatutoryDeduction",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "statutory_deduction": "statutoryDeduction",
    }

    def __init__(
        self, pagination=None, problem=None, statutory_deduction=None
    ):  # noqa: E501
        """StatutoryDeductionObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._statutory_deduction = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if statutory_deduction is not None:
            self.statutory_deduction = statutory_deduction

    @property
    def pagination(self):
        """Gets the pagination of this StatutoryDeductionObject.  # noqa: E501


        :return: The pagination of this StatutoryDeductionObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this StatutoryDeductionObject.


        :param pagination: The pagination of this StatutoryDeductionObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this StatutoryDeductionObject.  # noqa: E501


        :return: The problem of this StatutoryDeductionObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this StatutoryDeductionObject.


        :param problem: The problem of this StatutoryDeductionObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def statutory_deduction(self):
        """Gets the statutory_deduction of this StatutoryDeductionObject.  # noqa: E501


        :return: The statutory_deduction of this StatutoryDeductionObject.  # noqa: E501
        :rtype: StatutoryDeduction
        """
        return self._statutory_deduction

    @statutory_deduction.setter
    def statutory_deduction(self, statutory_deduction):
        """Sets the statutory_deduction of this StatutoryDeductionObject.


        :param statutory_deduction: The statutory_deduction of this StatutoryDeductionObject.  # noqa: E501
        :type: StatutoryDeduction
        """

        self._statutory_deduction = statutory_deduction
