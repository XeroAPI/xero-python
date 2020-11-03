# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.3.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ContactGroups(BaseModel):
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
    openapi_types = {"contact_groups": "list[ContactGroup]"}

    attribute_map = {"contact_groups": "ContactGroups"}

    def __init__(self, contact_groups=None):  # noqa: E501
        """ContactGroups - a model defined in OpenAPI"""  # noqa: E501

        self._contact_groups = None
        self.discriminator = None

        if contact_groups is not None:
            self.contact_groups = contact_groups

    @property
    def contact_groups(self):
        """Gets the contact_groups of this ContactGroups.  # noqa: E501


        :return: The contact_groups of this ContactGroups.  # noqa: E501
        :rtype: list[ContactGroup]
        """
        return self._contact_groups

    @contact_groups.setter
    def contact_groups(self, contact_groups):
        """Sets the contact_groups of this ContactGroups.


        :param contact_groups: The contact_groups of this ContactGroups.  # noqa: E501
        :type: list[ContactGroup]
        """

        self._contact_groups = contact_groups
