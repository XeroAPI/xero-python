# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.3.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class TimeZone(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    MOROCCOSTANDARDTIME = "MOROCCOSTANDARDTIME"
    UTC = "UTC"
    GMTSTANDARDTIME = "GMTSTANDARDTIME"
    GREENWICHSTANDARDTIME = "GREENWICHSTANDARDTIME"
    WEUROPESTANDARDTIME = "WEUROPESTANDARDTIME"
    CENTRALEUROPESTANDARDTIME = "CENTRALEUROPESTANDARDTIME"
    ROMANCESTANDARDTIME = "ROMANCESTANDARDTIME"
    CENTRALEUROPEANSTANDARDTIME = "CENTRALEUROPEANSTANDARDTIME"
    WCENTRALAFRICASTANDARDTIME = "WCENTRALAFRICASTANDARDTIME"
    NAMIBIASTANDARDTIME = "NAMIBIASTANDARDTIME"
    JORDANSTANDARDTIME = "JORDANSTANDARDTIME"
    GTBSTANDARDTIME = "GTBSTANDARDTIME"
    MIDDLEEASTSTANDARDTIME = "MIDDLEEASTSTANDARDTIME"
    EGYPTSTANDARDTIME = "EGYPTSTANDARDTIME"
    SYRIASTANDARDTIME = "SYRIASTANDARDTIME"
    EEUROPESTANDARDTIME = "EEUROPESTANDARDTIME"
    SOUTHAFRICASTANDARDTIME = "SOUTHAFRICASTANDARDTIME"
    FLESTANDARDTIME = "FLESTANDARDTIME"
    TURKEYSTANDARDTIME = "TURKEYSTANDARDTIME"
    ISRAELSTANDARDTIME = "ISRAELSTANDARDTIME"
    KALININGRADSTANDARDTIME = "KALININGRADSTANDARDTIME"
    LIBYASTANDARDTIME = "LIBYASTANDARDTIME"
    ARABICSTANDARDTIME = "ARABICSTANDARDTIME"
    ARABSTANDARDTIME = "ARABSTANDARDTIME"
    BELARUSSTANDARDTIME = "BELARUSSTANDARDTIME"
    RUSSIANSTANDARDTIME = "RUSSIANSTANDARDTIME"
    EAFRICASTANDARDTIME = "EAFRICASTANDARDTIME"
    IRANSTANDARDTIME = "IRANSTANDARDTIME"
    ARABIANSTANDARDTIME = "ARABIANSTANDARDTIME"
    AZERBAIJANSTANDARDTIME = "AZERBAIJANSTANDARDTIME"
    RUSSIATIMEZONE3 = "RUSSIATIMEZONE3"
    MAURITIUSSTANDARDTIME = "MAURITIUSSTANDARDTIME"
    GEORGIANSTANDARDTIME = "GEORGIANSTANDARDTIME"
    CAUCASUSSTANDARDTIME = "CAUCASUSSTANDARDTIME"
    AFGHANISTANSTANDARDTIME = "AFGHANISTANSTANDARDTIME"
    WESTASIASTANDARDTIME = "WESTASIASTANDARDTIME"
    EKATERINBURGSTANDARDTIME = "EKATERINBURGSTANDARDTIME"
    PAKISTANSTANDARDTIME = "PAKISTANSTANDARDTIME"
    INDIASTANDARDTIME = "INDIASTANDARDTIME"
    SRILANKASTANDARDTIME = "SRILANKASTANDARDTIME"
    NEPALSTANDARDTIME = "NEPALSTANDARDTIME"
    CENTRALASIASTANDARDTIME = "CENTRALASIASTANDARDTIME"
    BANGLADESHSTANDARDTIME = "BANGLADESHSTANDARDTIME"
    NCENTRALASIASTANDARDTIME = "NCENTRALASIASTANDARDTIME"
    MYANMARSTANDARDTIME = "MYANMARSTANDARDTIME"
    SEASIASTANDARDTIME = "SEASIASTANDARDTIME"
    NORTHASIASTANDARDTIME = "NORTHASIASTANDARDTIME"
    CHINASTANDARDTIME = "CHINASTANDARDTIME"
    NORTHASIAEASTSTANDARDTIME = "NORTHASIAEASTSTANDARDTIME"
    SINGAPORESTANDARDTIME = "SINGAPORESTANDARDTIME"
    WAUSTRALIASTANDARDTIME = "WAUSTRALIASTANDARDTIME"
    TAIPEISTANDARDTIME = "TAIPEISTANDARDTIME"
    ULAANBAATARSTANDARDTIME = "ULAANBAATARSTANDARDTIME"
    TOKYOSTANDARDTIME = "TOKYOSTANDARDTIME"
    KOREASTANDARDTIME = "KOREASTANDARDTIME"
    YAKUTSKSTANDARDTIME = "YAKUTSKSTANDARDTIME"
    CENAUSTRALIASTANDARDTIME = "CENAUSTRALIASTANDARDTIME"
    AUSCENTRALSTANDARDTIME = "AUSCENTRALSTANDARDTIME"
    EAUSTRALIASTANDARDTIME = "EAUSTRALIASTANDARDTIME"
    AUSEASTERNSTANDARDTIME = "AUSEASTERNSTANDARDTIME"
    WESTPACIFICSTANDARDTIME = "WESTPACIFICSTANDARDTIME"
    TASMANIASTANDARDTIME = "TASMANIASTANDARDTIME"
    MAGADANSTANDARDTIME = "MAGADANSTANDARDTIME"
    VLADIVOSTOKSTANDARDTIME = "VLADIVOSTOKSTANDARDTIME"
    RUSSIATIMEZONE10 = "RUSSIATIMEZONE10"
    CENTRALPACIFICSTANDARDTIME = "CENTRALPACIFICSTANDARDTIME"
    RUSSIATIMEZONE11 = "RUSSIATIMEZONE11"
    NEWZEALANDSTANDARDTIME = "NEWZEALANDSTANDARDTIME"
    UTC_12 = "UTC+12"
    UTC_13 = "UTC+13"
    FIJISTANDARDTIME = "FIJISTANDARDTIME"
    KAMCHATKASTANDARDTIME = "KAMCHATKASTANDARDTIME"
    TONGASTANDARDTIME = "TONGASTANDARDTIME"
    SAMOASTANDARDTIME = "SAMOASTANDARDTIME"
    LINEISLANDSSTANDARDTIME = "LINEISLANDSSTANDARDTIME"
    AZORESSTANDARDTIME = "AZORESSTANDARDTIME"
    CAPEVERDESTANDARDTIME = "CAPEVERDESTANDARDTIME"
    UTC02 = "UTC02"
    MIDATLANTICSTANDARDTIME = "MIDATLANTICSTANDARDTIME"
    ESOUTHAMERICASTANDARDTIME = "ESOUTHAMERICASTANDARDTIME"
    ARGENTINASTANDARDTIME = "ARGENTINASTANDARDTIME"
    SAEASTERNSTANDARDTIME = "SAEASTERNSTANDARDTIME"
    GREENLANDSTANDARDTIME = "GREENLANDSTANDARDTIME"
    MONTEVIDEOSTANDARDTIME = "MONTEVIDEOSTANDARDTIME"
    BAHIASTANDARDTIME = "BAHIASTANDARDTIME"
    NEWFOUNDLANDSTANDARDTIME = "NEWFOUNDLANDSTANDARDTIME"
    PARAGUAYSTANDARDTIME = "PARAGUAYSTANDARDTIME"
    ATLANTICSTANDARDTIME = "ATLANTICSTANDARDTIME"
    CENTRALBRAZILIANSTANDARDTIME = "CENTRALBRAZILIANSTANDARDTIME"
    SAWESTERNSTANDARDTIME = "SAWESTERNSTANDARDTIME"
    PACIFICSASTANDARDTIME = "PACIFICSASTANDARDTIME"
    VENEZUELASTANDARDTIME = "VENEZUELASTANDARDTIME"
    SAPACIFICSTANDARDTIME = "SAPACIFICSTANDARDTIME"
    EASTERNSTANDARDTIME = "EASTERNSTANDARDTIME"
    USEASTERNSTANDARDTIME = "USEASTERNSTANDARDTIME"
    CENTRALAMERICASTANDARDTIME = "CENTRALAMERICASTANDARDTIME"
    CENTRALSTANDARDTIME = "CENTRALSTANDARDTIME"
    CENTRALSTANDARDTIME_MEXICO_ = "CENTRALSTANDARDTIME(MEXICO)"
    CANADACENTRALSTANDARDTIME = "CANADACENTRALSTANDARDTIME"
    USMOUNTAINSTANDARDTIME = "USMOUNTAINSTANDARDTIME"
    MOUNTAINSTANDARDTIME_MEXICO_ = "MOUNTAINSTANDARDTIME(MEXICO)"
    MOUNTAINSTANDARDTIME = "MOUNTAINSTANDARDTIME"
    PACIFICSTANDARDTIME_MEXICO_ = "PACIFICSTANDARDTIME(MEXICO)"
    PACIFICSTANDARDTIME = "PACIFICSTANDARDTIME"
    ALASKANSTANDARDTIME = "ALASKANSTANDARDTIME"
    HAWAIIANSTANDARDTIME = "HAWAIIANSTANDARDTIME"
    UTC11 = "UTC11"
    DATELINESTANDARDTIME = "DATELINESTANDARDTIME"
