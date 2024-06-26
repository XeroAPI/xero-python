# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class GetPaymentsResponse(BaseModel):
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
        "id": "str",
        "status": "str",
        "provider_name": "str",
        "date_time_utc": "str",
        "page_info": "PageInfo",
        "payments": "list[Payments]",
    }

    attribute_map = {
        "id": "Id",
        "status": "Status",
        "provider_name": "ProviderName",
        "date_time_utc": "DateTimeUTC",
        "page_info": "PageInfo",
        "payments": "Payments",
    }

    def __init__(
        self,
        id=None,
        status=None,
        provider_name=None,
        date_time_utc=None,
        page_info=None,
        payments=None,
    ):  # noqa: E501
        """GetPaymentsResponse - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._status = None
        self._provider_name = None
        self._date_time_utc = None
        self._page_info = None
        self._payments = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if provider_name is not None:
            self.provider_name = provider_name
        if date_time_utc is not None:
            self.date_time_utc = date_time_utc
        if page_info is not None:
            self.page_info = page_info
        if payments is not None:
            self.payments = payments

    @property
    def id(self):
        """Gets the id of this GetPaymentsResponse.  # noqa: E501


        :return: The id of this GetPaymentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetPaymentsResponse.


        :param id: The id of this GetPaymentsResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this GetPaymentsResponse.  # noqa: E501


        :return: The status of this GetPaymentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetPaymentsResponse.


        :param status: The status of this GetPaymentsResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def provider_name(self):
        """Gets the provider_name of this GetPaymentsResponse.  # noqa: E501


        :return: The provider_name of this GetPaymentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this GetPaymentsResponse.


        :param provider_name: The provider_name of this GetPaymentsResponse.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def date_time_utc(self):
        """Gets the date_time_utc of this GetPaymentsResponse.  # noqa: E501


        :return: The date_time_utc of this GetPaymentsResponse.  # noqa: E501
        :rtype: str
        """
        return self._date_time_utc

    @date_time_utc.setter
    def date_time_utc(self, date_time_utc):
        """Sets the date_time_utc of this GetPaymentsResponse.


        :param date_time_utc: The date_time_utc of this GetPaymentsResponse.  # noqa: E501
        :type: str
        """

        self._date_time_utc = date_time_utc

    @property
    def page_info(self):
        """Gets the page_info of this GetPaymentsResponse.  # noqa: E501


        :return: The page_info of this GetPaymentsResponse.  # noqa: E501
        :rtype: PageInfo
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this GetPaymentsResponse.


        :param page_info: The page_info of this GetPaymentsResponse.  # noqa: E501
        :type: PageInfo
        """

        self._page_info = page_info

    @property
    def payments(self):
        """Gets the payments of this GetPaymentsResponse.  # noqa: E501


        :return: The payments of this GetPaymentsResponse.  # noqa: E501
        :rtype: list[Payments]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this GetPaymentsResponse.


        :param payments: The payments of this GetPaymentsResponse.  # noqa: E501
        :type: list[Payments]
        """

        self._payments = payments
