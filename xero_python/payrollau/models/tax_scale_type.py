# coding: utf-8

"""
Xero Payroll AU API

This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class TaxScaleType(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    REGULAR = "REGULAR"
    ACTORSARTISTSENTERTAINERS = "ACTORSARTISTSENTERTAINERS"
    HORTICULTURISTORSHEARER = "HORTICULTURISTORSHEARER"
    SENIORORPENSIONER = "SENIORORPENSIONER"
    WORKINGHOLIDAYMAKER = "WORKINGHOLIDAYMAKER"
    FOREIGN = "FOREIGN"
