# coding: utf-8

"""
Xero Files API

These endpoints are specific to Xero Files API  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Files(BaseModel):
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
        "total_count": "int",
        "page": "int",
        "per_page": "int",
        "items": "list[FileObject]",
    }

    attribute_map = {
        "total_count": "TotalCount",
        "page": "Page",
        "per_page": "PerPage",
        "items": "Items",
    }

    def __init__(
        self, total_count=None, page=None, per_page=None, items=None
    ):  # noqa: E501
        """Files - a model defined in OpenAPI"""  # noqa: E501

        self._total_count = None
        self._page = None
        self._per_page = None
        self._items = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if items is not None:
            self.items = items

    @property
    def total_count(self):
        """Gets the total_count of this Files.  # noqa: E501


        :return: The total_count of this Files.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this Files.


        :param total_count: The total_count of this Files.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def page(self):
        """Gets the page of this Files.  # noqa: E501


        :return: The page of this Files.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this Files.


        :param page: The page of this Files.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this Files.  # noqa: E501


        :return: The per_page of this Files.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this Files.


        :param per_page: The per_page of this Files.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def items(self):
        """Gets the items of this Files.  # noqa: E501


        :return: The items of this Files.  # noqa: E501
        :rtype: list[FileObject]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Files.


        :param items: The items of this Files.  # noqa: E501
        :type: list[FileObject]
        """

        self._items = items
