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


class Payslips(BaseModel):
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
    openapi_types = {"payslips": "list[Payslip]"}

    attribute_map = {"payslips": "Payslips"}

    def __init__(self, payslips=None):  # noqa: E501
        """Payslips - a model defined in OpenAPI"""  # noqa: E501

        self._payslips = None
        self.discriminator = None

        if payslips is not None:
            self.payslips = payslips

    @property
    def payslips(self):
        """Gets the payslips of this Payslips.  # noqa: E501


        :return: The payslips of this Payslips.  # noqa: E501
        :rtype: list[Payslip]
        """
        return self._payslips

    @payslips.setter
    def payslips(self, payslips):
        """Sets the payslips of this Payslips.


        :param payslips: The payslips of this Payslips.  # noqa: E501
        :type: list[Payslip]
        """

        self._payslips = payslips
