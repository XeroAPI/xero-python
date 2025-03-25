# coding: utf-8

"""
Xero Accounting API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LineItemTracking(BaseModel):
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
        "tracking_category_id": "str",
        "tracking_option_id": "str",
        "name": "str",
        "option": "str",
    }

    attribute_map = {
        "tracking_category_id": "TrackingCategoryID",
        "tracking_option_id": "TrackingOptionID",
        "name": "Name",
        "option": "Option",
    }

    def __init__(
        self, tracking_category_id=None, tracking_option_id=None, name=None, option=None
    ):  # noqa: E501
        """LineItemTracking - a model defined in OpenAPI"""  # noqa: E501

        self._tracking_category_id = None
        self._tracking_option_id = None
        self._name = None
        self._option = None
        self.discriminator = None

        if tracking_category_id is not None:
            self.tracking_category_id = tracking_category_id
        if tracking_option_id is not None:
            self.tracking_option_id = tracking_option_id
        if name is not None:
            self.name = name
        if option is not None:
            self.option = option

    @property
    def tracking_category_id(self):
        """Gets the tracking_category_id of this LineItemTracking.  # noqa: E501

        The Xero identifier for a tracking category  # noqa: E501

        :return: The tracking_category_id of this LineItemTracking.  # noqa: E501
        :rtype: str
        """
        return self._tracking_category_id

    @tracking_category_id.setter
    def tracking_category_id(self, tracking_category_id):
        """Sets the tracking_category_id of this LineItemTracking.

        The Xero identifier for a tracking category  # noqa: E501

        :param tracking_category_id: The tracking_category_id of this LineItemTracking.  # noqa: E501
        :type: str
        """

        self._tracking_category_id = tracking_category_id

    @property
    def tracking_option_id(self):
        """Gets the tracking_option_id of this LineItemTracking.  # noqa: E501

        The Xero identifier for a tracking category option  # noqa: E501

        :return: The tracking_option_id of this LineItemTracking.  # noqa: E501
        :rtype: str
        """
        return self._tracking_option_id

    @tracking_option_id.setter
    def tracking_option_id(self, tracking_option_id):
        """Sets the tracking_option_id of this LineItemTracking.

        The Xero identifier for a tracking category option  # noqa: E501

        :param tracking_option_id: The tracking_option_id of this LineItemTracking.  # noqa: E501
        :type: str
        """

        self._tracking_option_id = tracking_option_id

    @property
    def name(self):
        """Gets the name of this LineItemTracking.  # noqa: E501

        The name of the tracking category  # noqa: E501

        :return: The name of this LineItemTracking.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LineItemTracking.

        The name of the tracking category  # noqa: E501

        :param name: The name of this LineItemTracking.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, "
                "length must be less than or equal to `100`"
            )  # noqa: E501

        self._name = name

    @property
    def option(self):
        """Gets the option of this LineItemTracking.  # noqa: E501

        See Tracking Options  # noqa: E501

        :return: The option of this LineItemTracking.  # noqa: E501
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this LineItemTracking.

        See Tracking Options  # noqa: E501

        :param option: The option of this LineItemTracking.  # noqa: E501
        :type: str
        """

        self._option = option
