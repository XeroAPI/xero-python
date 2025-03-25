# coding: utf-8

"""
Xero Payroll UK

This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeeOpeningBalances(BaseModel):
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
        "statutory_adoption_pay": "float",
        "statutory_maternity_pay": "float",
        "statutory_paternity_pay": "float",
        "statutory_shared_parental_pay": "float",
        "statutory_sick_pay": "float",
        "prior_employee_number": "float",
    }

    attribute_map = {
        "statutory_adoption_pay": "statutoryAdoptionPay",
        "statutory_maternity_pay": "statutoryMaternityPay",
        "statutory_paternity_pay": "statutoryPaternityPay",
        "statutory_shared_parental_pay": "statutorySharedParentalPay",
        "statutory_sick_pay": "statutorySickPay",
        "prior_employee_number": "priorEmployeeNumber",
    }

    def __init__(
        self,
        statutory_adoption_pay=None,
        statutory_maternity_pay=None,
        statutory_paternity_pay=None,
        statutory_shared_parental_pay=None,
        statutory_sick_pay=None,
        prior_employee_number=None,
    ):  # noqa: E501
        """EmployeeOpeningBalances - a model defined in OpenAPI"""  # noqa: E501

        self._statutory_adoption_pay = None
        self._statutory_maternity_pay = None
        self._statutory_paternity_pay = None
        self._statutory_shared_parental_pay = None
        self._statutory_sick_pay = None
        self._prior_employee_number = None
        self.discriminator = None

        if statutory_adoption_pay is not None:
            self.statutory_adoption_pay = statutory_adoption_pay
        if statutory_maternity_pay is not None:
            self.statutory_maternity_pay = statutory_maternity_pay
        if statutory_paternity_pay is not None:
            self.statutory_paternity_pay = statutory_paternity_pay
        if statutory_shared_parental_pay is not None:
            self.statutory_shared_parental_pay = statutory_shared_parental_pay
        if statutory_sick_pay is not None:
            self.statutory_sick_pay = statutory_sick_pay
        if prior_employee_number is not None:
            self.prior_employee_number = prior_employee_number

    @property
    def statutory_adoption_pay(self):
        """Gets the statutory_adoption_pay of this EmployeeOpeningBalances.  # noqa: E501

        The total accumulated statutory adoption pay amount received by the employee for current fiscal year to date  # noqa: E501

        :return: The statutory_adoption_pay of this EmployeeOpeningBalances.  # noqa: E501
        :rtype: float
        """
        return self._statutory_adoption_pay

    @statutory_adoption_pay.setter
    def statutory_adoption_pay(self, statutory_adoption_pay):
        """Sets the statutory_adoption_pay of this EmployeeOpeningBalances.

        The total accumulated statutory adoption pay amount received by the employee for current fiscal year to date  # noqa: E501

        :param statutory_adoption_pay: The statutory_adoption_pay of this EmployeeOpeningBalances.  # noqa: E501
        :type: float
        """

        self._statutory_adoption_pay = statutory_adoption_pay

    @property
    def statutory_maternity_pay(self):
        """Gets the statutory_maternity_pay of this EmployeeOpeningBalances.  # noqa: E501

        The total accumulated statutory maternity pay amount received by the employee for current fiscal year to date  # noqa: E501

        :return: The statutory_maternity_pay of this EmployeeOpeningBalances.  # noqa: E501
        :rtype: float
        """
        return self._statutory_maternity_pay

    @statutory_maternity_pay.setter
    def statutory_maternity_pay(self, statutory_maternity_pay):
        """Sets the statutory_maternity_pay of this EmployeeOpeningBalances.

        The total accumulated statutory maternity pay amount received by the employee for current fiscal year to date  # noqa: E501

        :param statutory_maternity_pay: The statutory_maternity_pay of this EmployeeOpeningBalances.  # noqa: E501
        :type: float
        """

        self._statutory_maternity_pay = statutory_maternity_pay

    @property
    def statutory_paternity_pay(self):
        """Gets the statutory_paternity_pay of this EmployeeOpeningBalances.  # noqa: E501

        The total accumulated statutory paternity pay amount received by the employee for current fiscal year to date  # noqa: E501

        :return: The statutory_paternity_pay of this EmployeeOpeningBalances.  # noqa: E501
        :rtype: float
        """
        return self._statutory_paternity_pay

    @statutory_paternity_pay.setter
    def statutory_paternity_pay(self, statutory_paternity_pay):
        """Sets the statutory_paternity_pay of this EmployeeOpeningBalances.

        The total accumulated statutory paternity pay amount received by the employee for current fiscal year to date  # noqa: E501

        :param statutory_paternity_pay: The statutory_paternity_pay of this EmployeeOpeningBalances.  # noqa: E501
        :type: float
        """

        self._statutory_paternity_pay = statutory_paternity_pay

    @property
    def statutory_shared_parental_pay(self):
        """Gets the statutory_shared_parental_pay of this EmployeeOpeningBalances.  # noqa: E501

        The total accumulated statutory shared parental pay amount received by the employee for current fiscal year to date  # noqa: E501

        :return: The statutory_shared_parental_pay of this EmployeeOpeningBalances.  # noqa: E501
        :rtype: float
        """
        return self._statutory_shared_parental_pay

    @statutory_shared_parental_pay.setter
    def statutory_shared_parental_pay(self, statutory_shared_parental_pay):
        """Sets the statutory_shared_parental_pay of this EmployeeOpeningBalances.

        The total accumulated statutory shared parental pay amount received by the employee for current fiscal year to date  # noqa: E501

        :param statutory_shared_parental_pay: The statutory_shared_parental_pay of this EmployeeOpeningBalances.  # noqa: E501
        :type: float
        """

        self._statutory_shared_parental_pay = statutory_shared_parental_pay

    @property
    def statutory_sick_pay(self):
        """Gets the statutory_sick_pay of this EmployeeOpeningBalances.  # noqa: E501

        The total accumulated statutory sick pay amount received by the employee for current fiscal year to date  # noqa: E501

        :return: The statutory_sick_pay of this EmployeeOpeningBalances.  # noqa: E501
        :rtype: float
        """
        return self._statutory_sick_pay

    @statutory_sick_pay.setter
    def statutory_sick_pay(self, statutory_sick_pay):
        """Sets the statutory_sick_pay of this EmployeeOpeningBalances.

        The total accumulated statutory sick pay amount received by the employee for current fiscal year to date  # noqa: E501

        :param statutory_sick_pay: The statutory_sick_pay of this EmployeeOpeningBalances.  # noqa: E501
        :type: float
        """

        self._statutory_sick_pay = statutory_sick_pay

    @property
    def prior_employee_number(self):
        """Gets the prior_employee_number of this EmployeeOpeningBalances.  # noqa: E501

        The unique employee number issued by the employee's former employer  # noqa: E501

        :return: The prior_employee_number of this EmployeeOpeningBalances.  # noqa: E501
        :rtype: float
        """
        return self._prior_employee_number

    @prior_employee_number.setter
    def prior_employee_number(self, prior_employee_number):
        """Sets the prior_employee_number of this EmployeeOpeningBalances.

        The unique employee number issued by the employee's former employer  # noqa: E501

        :param prior_employee_number: The prior_employee_number of this EmployeeOpeningBalances.  # noqa: E501
        :type: float
        """

        self._prior_employee_number = prior_employee_number
