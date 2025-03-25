# coding: utf-8

"""
Xero Accounting API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class CISOrgSetting(BaseModel):
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
        "cis_contractor_enabled": "bool",
        "cis_sub_contractor_enabled": "bool",
        "rate": "float",
    }

    attribute_map = {
        "cis_contractor_enabled": "CISContractorEnabled",
        "cis_sub_contractor_enabled": "CISSubContractorEnabled",
        "rate": "Rate",
    }

    def __init__(
        self, cis_contractor_enabled=None, cis_sub_contractor_enabled=None, rate=None
    ):  # noqa: E501
        """CISOrgSetting - a model defined in OpenAPI"""  # noqa: E501

        self._cis_contractor_enabled = None
        self._cis_sub_contractor_enabled = None
        self._rate = None
        self.discriminator = None

        if cis_contractor_enabled is not None:
            self.cis_contractor_enabled = cis_contractor_enabled
        if cis_sub_contractor_enabled is not None:
            self.cis_sub_contractor_enabled = cis_sub_contractor_enabled
        if rate is not None:
            self.rate = rate

    @property
    def cis_contractor_enabled(self):
        """Gets the cis_contractor_enabled of this CISOrgSetting.  # noqa: E501

        true or false - Boolean that describes if the organisation is a CIS Contractor  # noqa: E501

        :return: The cis_contractor_enabled of this CISOrgSetting.  # noqa: E501
        :rtype: bool
        """
        return self._cis_contractor_enabled

    @cis_contractor_enabled.setter
    def cis_contractor_enabled(self, cis_contractor_enabled):
        """Sets the cis_contractor_enabled of this CISOrgSetting.

        true or false - Boolean that describes if the organisation is a CIS Contractor  # noqa: E501

        :param cis_contractor_enabled: The cis_contractor_enabled of this CISOrgSetting.  # noqa: E501
        :type: bool
        """

        self._cis_contractor_enabled = cis_contractor_enabled

    @property
    def cis_sub_contractor_enabled(self):
        """Gets the cis_sub_contractor_enabled of this CISOrgSetting.  # noqa: E501

        true or false - Boolean that describes if the organisation is a CIS SubContractor  # noqa: E501

        :return: The cis_sub_contractor_enabled of this CISOrgSetting.  # noqa: E501
        :rtype: bool
        """
        return self._cis_sub_contractor_enabled

    @cis_sub_contractor_enabled.setter
    def cis_sub_contractor_enabled(self, cis_sub_contractor_enabled):
        """Sets the cis_sub_contractor_enabled of this CISOrgSetting.

        true or false - Boolean that describes if the organisation is a CIS SubContractor  # noqa: E501

        :param cis_sub_contractor_enabled: The cis_sub_contractor_enabled of this CISOrgSetting.  # noqa: E501
        :type: bool
        """

        self._cis_sub_contractor_enabled = cis_sub_contractor_enabled

    @property
    def rate(self):
        """Gets the rate of this CISOrgSetting.  # noqa: E501

        CIS Deduction rate for the organisation  # noqa: E501

        :return: The rate of this CISOrgSetting.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this CISOrgSetting.

        CIS Deduction rate for the organisation  # noqa: E501

        :param rate: The rate of this CISOrgSetting.  # noqa: E501
        :type: float
        """

        self._rate = rate
