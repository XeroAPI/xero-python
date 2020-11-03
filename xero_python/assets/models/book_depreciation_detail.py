# coding: utf-8

"""
    Xero Assets API

    This is the Xero Assets API  # noqa: E501

    OpenAPI spec version: 2.3.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BookDepreciationDetail(BaseModel):
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
        "current_capital_gain": "float",
        "current_gain_loss": "float",
        "depreciation_start_date": "date",
        "cost_limit": "float",
        "residual_value": "float",
        "prior_accum_depreciation_amount": "float",
        "current_accum_depreciation_amount": "float",
    }

    attribute_map = {
        "current_capital_gain": "currentCapitalGain",
        "current_gain_loss": "currentGainLoss",
        "depreciation_start_date": "depreciationStartDate",
        "cost_limit": "costLimit",
        "residual_value": "residualValue",
        "prior_accum_depreciation_amount": "priorAccumDepreciationAmount",
        "current_accum_depreciation_amount": "currentAccumDepreciationAmount",
    }

    def __init__(
        self,
        current_capital_gain=None,
        current_gain_loss=None,
        depreciation_start_date=None,
        cost_limit=None,
        residual_value=None,
        prior_accum_depreciation_amount=None,
        current_accum_depreciation_amount=None,
    ):  # noqa: E501
        """BookDepreciationDetail - a model defined in OpenAPI"""  # noqa: E501

        self._current_capital_gain = None
        self._current_gain_loss = None
        self._depreciation_start_date = None
        self._cost_limit = None
        self._residual_value = None
        self._prior_accum_depreciation_amount = None
        self._current_accum_depreciation_amount = None
        self.discriminator = None

        if current_capital_gain is not None:
            self.current_capital_gain = current_capital_gain
        if current_gain_loss is not None:
            self.current_gain_loss = current_gain_loss
        if depreciation_start_date is not None:
            self.depreciation_start_date = depreciation_start_date
        if cost_limit is not None:
            self.cost_limit = cost_limit
        if residual_value is not None:
            self.residual_value = residual_value
        if prior_accum_depreciation_amount is not None:
            self.prior_accum_depreciation_amount = prior_accum_depreciation_amount
        if current_accum_depreciation_amount is not None:
            self.current_accum_depreciation_amount = current_accum_depreciation_amount

    @property
    def current_capital_gain(self):
        """Gets the current_capital_gain of this BookDepreciationDetail.  # noqa: E501

        When an asset is disposed, this will be the sell price minus the purchase price if a profit was made.  # noqa: E501

        :return: The current_capital_gain of this BookDepreciationDetail.  # noqa: E501
        :rtype: float
        """
        return self._current_capital_gain

    @current_capital_gain.setter
    def current_capital_gain(self, current_capital_gain):
        """Sets the current_capital_gain of this BookDepreciationDetail.

        When an asset is disposed, this will be the sell price minus the purchase price if a profit was made.  # noqa: E501

        :param current_capital_gain: The current_capital_gain of this BookDepreciationDetail.  # noqa: E501
        :type: float
        """

        self._current_capital_gain = current_capital_gain

    @property
    def current_gain_loss(self):
        """Gets the current_gain_loss of this BookDepreciationDetail.  # noqa: E501

        When an asset is disposed, this will be the lowest one of sell price or purchase price, minus the current book value.  # noqa: E501

        :return: The current_gain_loss of this BookDepreciationDetail.  # noqa: E501
        :rtype: float
        """
        return self._current_gain_loss

    @current_gain_loss.setter
    def current_gain_loss(self, current_gain_loss):
        """Sets the current_gain_loss of this BookDepreciationDetail.

        When an asset is disposed, this will be the lowest one of sell price or purchase price, minus the current book value.  # noqa: E501

        :param current_gain_loss: The current_gain_loss of this BookDepreciationDetail.  # noqa: E501
        :type: float
        """

        self._current_gain_loss = current_gain_loss

    @property
    def depreciation_start_date(self):
        """Gets the depreciation_start_date of this BookDepreciationDetail.  # noqa: E501

        YYYY-MM-DD  # noqa: E501

        :return: The depreciation_start_date of this BookDepreciationDetail.  # noqa: E501
        :rtype: date
        """
        return self._depreciation_start_date

    @depreciation_start_date.setter
    def depreciation_start_date(self, depreciation_start_date):
        """Sets the depreciation_start_date of this BookDepreciationDetail.

        YYYY-MM-DD  # noqa: E501

        :param depreciation_start_date: The depreciation_start_date of this BookDepreciationDetail.  # noqa: E501
        :type: date
        """

        self._depreciation_start_date = depreciation_start_date

    @property
    def cost_limit(self):
        """Gets the cost_limit of this BookDepreciationDetail.  # noqa: E501

        The value of the asset you want to depreciate, if this is less than the cost of the asset.  # noqa: E501

        :return: The cost_limit of this BookDepreciationDetail.  # noqa: E501
        :rtype: float
        """
        return self._cost_limit

    @cost_limit.setter
    def cost_limit(self, cost_limit):
        """Sets the cost_limit of this BookDepreciationDetail.

        The value of the asset you want to depreciate, if this is less than the cost of the asset.  # noqa: E501

        :param cost_limit: The cost_limit of this BookDepreciationDetail.  # noqa: E501
        :type: float
        """

        self._cost_limit = cost_limit

    @property
    def residual_value(self):
        """Gets the residual_value of this BookDepreciationDetail.  # noqa: E501

        The value of the asset remaining when you've fully depreciated it.  # noqa: E501

        :return: The residual_value of this BookDepreciationDetail.  # noqa: E501
        :rtype: float
        """
        return self._residual_value

    @residual_value.setter
    def residual_value(self, residual_value):
        """Sets the residual_value of this BookDepreciationDetail.

        The value of the asset remaining when you've fully depreciated it.  # noqa: E501

        :param residual_value: The residual_value of this BookDepreciationDetail.  # noqa: E501
        :type: float
        """

        self._residual_value = residual_value

    @property
    def prior_accum_depreciation_amount(self):
        """Gets the prior_accum_depreciation_amount of this BookDepreciationDetail.  # noqa: E501

        All depreciation prior to the current financial year.  # noqa: E501

        :return: The prior_accum_depreciation_amount of this BookDepreciationDetail.  # noqa: E501
        :rtype: float
        """
        return self._prior_accum_depreciation_amount

    @prior_accum_depreciation_amount.setter
    def prior_accum_depreciation_amount(self, prior_accum_depreciation_amount):
        """Sets the prior_accum_depreciation_amount of this BookDepreciationDetail.

        All depreciation prior to the current financial year.  # noqa: E501

        :param prior_accum_depreciation_amount: The prior_accum_depreciation_amount of this BookDepreciationDetail.  # noqa: E501
        :type: float
        """

        self._prior_accum_depreciation_amount = prior_accum_depreciation_amount

    @property
    def current_accum_depreciation_amount(self):
        """Gets the current_accum_depreciation_amount of this BookDepreciationDetail.  # noqa: E501

        All depreciation occurring in the current financial year.  # noqa: E501

        :return: The current_accum_depreciation_amount of this BookDepreciationDetail.  # noqa: E501
        :rtype: float
        """
        return self._current_accum_depreciation_amount

    @current_accum_depreciation_amount.setter
    def current_accum_depreciation_amount(self, current_accum_depreciation_amount):
        """Sets the current_accum_depreciation_amount of this BookDepreciationDetail.

        All depreciation occurring in the current financial year.  # noqa: E501

        :param current_accum_depreciation_amount: The current_accum_depreciation_amount of this BookDepreciationDetail.  # noqa: E501
        :type: float
        """

        self._current_accum_depreciation_amount = current_accum_depreciation_amount
