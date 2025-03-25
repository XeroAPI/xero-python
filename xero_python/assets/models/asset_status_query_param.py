# coding: utf-8

"""
Xero Assets API

The Assets API exposes fixed asset related functions of the Xero Accounting application and can be used for a variety of purposes such as creating assets, retrieving asset valuations etc.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class AssetStatusQueryParam(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    DRAFT = "DRAFT"
    REGISTERED = "REGISTERED"
    DISPOSED = "DISPOSED"
