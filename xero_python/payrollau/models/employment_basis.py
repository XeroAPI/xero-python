# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.3.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class EmploymentBasis(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    FULLTIME = "FULLTIME"
    PARTTIME = "PARTTIME"
    CASUAL = "CASUAL"
    LABOURHIRE = "LABOURHIRE"
    SUPERINCOMESTREAM = "SUPERINCOMESTREAM"
