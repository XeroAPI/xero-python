# coding: utf-8

"""
Xero Finance API

The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class ProblemType(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    NOTSET = "NotSet"
    BANK_ACCOUNT_NOT_FOUND = "bank-account-not-found"
    INTERNAL_ERROR = "internal-error"
    INVALID_APPLICATION = "invalid-application"
    INVALID_REQUEST = "invalid-request"
    ORGANISATION_NOT_FOUND = "organisation-not-found"
    ORGANISATION_OFFLINE = "organisation-offline"
    REQUEST_TIMEOUT = "request-timeout"
    SERVICE_UNAVAILABLE = "service-unavailable"
    UNAUTHORIZED = "unauthorized"
    RATE_LIMIT_ERROR = "rate-limit-error"
