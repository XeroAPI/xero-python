# -*- coding: utf-8 -*-
import json
from decimal import Decimal
from string import capwords

from . import ApiException, OAuth2Error
from ..utils import getvalue


def translate_status_exception(error, api_instance, api_method):
    """Translate HTTPStatusException into proper Xero API status error
    :param error: HTTPStatusException
    :param api_instance: xero api instance exception occurred to
    :param api_method: xero api instance method name exception occurred to
    :return: HTTPStatusException
    """
    if error.status == 429:
        return RateLimitException(http_resp=error.http_resp)
    if error.status == 404:
        return NotFoundException(http_resp=error.http_resp)
    if error.status == 400:
        return BadRequestException(http_resp=error.http_resp)
    return error


class HTTPStatusException(ApiException):
    """Exception for http status != 2xx"""


class RateLimitException(HTTPStatusException):
    """Exception if Xero API rate limit reached"""

    @property
    def rate_limit(self):
        try:
            return self.headers.get("x-rate-limit-problem")
        except Exception:
            return None

    @property
    def error_message(self):
        return "You've exceeded the per {} rate limit".format(self.rate_limit)


class NotFoundException(HTTPStatusException):
    """Exception if Xero API resource not found"""

    @property
    def error_message(self):
        return "The resource you're looking for cannot be found"


class BadRequestException(HTTPStatusException):
    """Exception if Xero API received bad request"""

    @property
    def error_data(self):
        return json.loads(getattr(self.http_resp, "text", ""), parse_float=Decimal)


class AccountingBadRequestException(BadRequestException):
    """Exception if Xero Accounting API received bad request"""

    @property
    def status(self):
        return getattr(self.error_data, "Message", None) or super().status

    @property
    def reason(self):
        return (
            getvalue(self.error_data, "Elements.0.ValidationErrors.0.Message", None)
            or super().reason
        )


class PayrollUkBadRequestException(BadRequestException):
    """Exception if Xero Accounting API received bad request"""

    @property
    def status(self):
        return getattr(self.error_data, "Message", None) or super().status

    @property
    def reason(self):
        return getvalue(self.error_data, "problem", None) or super().reason


class OAuth2InvalidGrantError(BadRequestException, OAuth2Error):
    """Exception if Xero Identity API received bad oauth2 grant token request"""

    @property
    def reason(self):
        value = getvalue(self.error_data, "error", "")
        if value:
            return capwords(value.replace("_", " "))

        return super().reason
