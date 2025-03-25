# coding: utf-8

"""
Xero Payroll AU API

This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SuperannuationLine(BaseModel):
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
        "super_membership_id": "str",
        "contribution_type": "SuperannuationContributionType",
        "calculation_type": "SuperannuationCalculationType",
        "minimum_monthly_earnings": "float",
        "expense_account_code": "str",
        "liability_account_code": "str",
        "payment_date_for_this_period": "date[ms-format]",
        "percentage": "float",
        "amount": "float",
    }

    attribute_map = {
        "super_membership_id": "SuperMembershipID",
        "contribution_type": "ContributionType",
        "calculation_type": "CalculationType",
        "minimum_monthly_earnings": "MinimumMonthlyEarnings",
        "expense_account_code": "ExpenseAccountCode",
        "liability_account_code": "LiabilityAccountCode",
        "payment_date_for_this_period": "PaymentDateForThisPeriod",
        "percentage": "Percentage",
        "amount": "Amount",
    }

    def __init__(
        self,
        super_membership_id=None,
        contribution_type=None,
        calculation_type=None,
        minimum_monthly_earnings=None,
        expense_account_code=None,
        liability_account_code=None,
        payment_date_for_this_period=None,
        percentage=None,
        amount=None,
    ):  # noqa: E501
        """SuperannuationLine - a model defined in OpenAPI"""  # noqa: E501

        self._super_membership_id = None
        self._contribution_type = None
        self._calculation_type = None
        self._minimum_monthly_earnings = None
        self._expense_account_code = None
        self._liability_account_code = None
        self._payment_date_for_this_period = None
        self._percentage = None
        self._amount = None
        self.discriminator = None

        if super_membership_id is not None:
            self.super_membership_id = super_membership_id
        if contribution_type is not None:
            self.contribution_type = contribution_type
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if minimum_monthly_earnings is not None:
            self.minimum_monthly_earnings = minimum_monthly_earnings
        if expense_account_code is not None:
            self.expense_account_code = expense_account_code
        if liability_account_code is not None:
            self.liability_account_code = liability_account_code
        if payment_date_for_this_period is not None:
            self.payment_date_for_this_period = payment_date_for_this_period
        if percentage is not None:
            self.percentage = percentage
        if amount is not None:
            self.amount = amount

    @property
    def super_membership_id(self):
        """Gets the super_membership_id of this SuperannuationLine.  # noqa: E501

        Xero identifier for payroll super fund membership ID.  # noqa: E501

        :return: The super_membership_id of this SuperannuationLine.  # noqa: E501
        :rtype: str
        """
        return self._super_membership_id

    @super_membership_id.setter
    def super_membership_id(self, super_membership_id):
        """Sets the super_membership_id of this SuperannuationLine.

        Xero identifier for payroll super fund membership ID.  # noqa: E501

        :param super_membership_id: The super_membership_id of this SuperannuationLine.  # noqa: E501
        :type: str
        """

        self._super_membership_id = super_membership_id

    @property
    def contribution_type(self):
        """Gets the contribution_type of this SuperannuationLine.  # noqa: E501


        :return: The contribution_type of this SuperannuationLine.  # noqa: E501
        :rtype: SuperannuationContributionType
        """
        return self._contribution_type

    @contribution_type.setter
    def contribution_type(self, contribution_type):
        """Sets the contribution_type of this SuperannuationLine.


        :param contribution_type: The contribution_type of this SuperannuationLine.  # noqa: E501
        :type: SuperannuationContributionType
        """

        self._contribution_type = contribution_type

    @property
    def calculation_type(self):
        """Gets the calculation_type of this SuperannuationLine.  # noqa: E501


        :return: The calculation_type of this SuperannuationLine.  # noqa: E501
        :rtype: SuperannuationCalculationType
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this SuperannuationLine.


        :param calculation_type: The calculation_type of this SuperannuationLine.  # noqa: E501
        :type: SuperannuationCalculationType
        """

        self._calculation_type = calculation_type

    @property
    def minimum_monthly_earnings(self):
        """Gets the minimum_monthly_earnings of this SuperannuationLine.  # noqa: E501

        Superannuation minimum monthly earnings.  # noqa: E501

        :return: The minimum_monthly_earnings of this SuperannuationLine.  # noqa: E501
        :rtype: float
        """
        return self._minimum_monthly_earnings

    @minimum_monthly_earnings.setter
    def minimum_monthly_earnings(self, minimum_monthly_earnings):
        """Sets the minimum_monthly_earnings of this SuperannuationLine.

        Superannuation minimum monthly earnings.  # noqa: E501

        :param minimum_monthly_earnings: The minimum_monthly_earnings of this SuperannuationLine.  # noqa: E501
        :type: float
        """

        self._minimum_monthly_earnings = minimum_monthly_earnings

    @property
    def expense_account_code(self):
        """Gets the expense_account_code of this SuperannuationLine.  # noqa: E501

        Superannuation expense account code.  # noqa: E501

        :return: The expense_account_code of this SuperannuationLine.  # noqa: E501
        :rtype: str
        """
        return self._expense_account_code

    @expense_account_code.setter
    def expense_account_code(self, expense_account_code):
        """Sets the expense_account_code of this SuperannuationLine.

        Superannuation expense account code.  # noqa: E501

        :param expense_account_code: The expense_account_code of this SuperannuationLine.  # noqa: E501
        :type: str
        """

        self._expense_account_code = expense_account_code

    @property
    def liability_account_code(self):
        """Gets the liability_account_code of this SuperannuationLine.  # noqa: E501

        Superannuation liability account code  # noqa: E501

        :return: The liability_account_code of this SuperannuationLine.  # noqa: E501
        :rtype: str
        """
        return self._liability_account_code

    @liability_account_code.setter
    def liability_account_code(self, liability_account_code):
        """Sets the liability_account_code of this SuperannuationLine.

        Superannuation liability account code  # noqa: E501

        :param liability_account_code: The liability_account_code of this SuperannuationLine.  # noqa: E501
        :type: str
        """

        self._liability_account_code = liability_account_code

    @property
    def payment_date_for_this_period(self):
        """Gets the payment_date_for_this_period of this SuperannuationLine.  # noqa: E501

        Superannuation payment date for the current period (YYYY-MM-DD)  # noqa: E501

        :return: The payment_date_for_this_period of this SuperannuationLine.  # noqa: E501
        :rtype: date
        """
        return self._payment_date_for_this_period

    @payment_date_for_this_period.setter
    def payment_date_for_this_period(self, payment_date_for_this_period):
        """Sets the payment_date_for_this_period of this SuperannuationLine.

        Superannuation payment date for the current period (YYYY-MM-DD)  # noqa: E501

        :param payment_date_for_this_period: The payment_date_for_this_period of this SuperannuationLine.  # noqa: E501
        :type: date
        """

        self._payment_date_for_this_period = payment_date_for_this_period

    @property
    def percentage(self):
        """Gets the percentage of this SuperannuationLine.  # noqa: E501

        Superannuation percentage  # noqa: E501

        :return: The percentage of this SuperannuationLine.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this SuperannuationLine.

        Superannuation percentage  # noqa: E501

        :param percentage: The percentage of this SuperannuationLine.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def amount(self):
        """Gets the amount of this SuperannuationLine.  # noqa: E501

        Superannuation amount  # noqa: E501

        :return: The amount of this SuperannuationLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SuperannuationLine.

        Superannuation amount  # noqa: E501

        :param amount: The amount of this SuperannuationLine.  # noqa: E501
        :type: float
        """

        self._amount = amount
