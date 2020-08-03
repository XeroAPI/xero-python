# -*- coding: utf-8 -*-

from xero_python import exceptions


def translate_status_exception(error, api_instance, api_method):
    """
    Translate HTTPStatusException into proper Xero API status error
    :param error: HTTPStatusException
    :param api_instance: xero api instance exception occurred to
    :param api_method: xero api instance method name exception occurred to
    :return: HTTPStatusException
    """
    if error.status == 400:
        return exceptions.PayrollUkBadRequestException(http_resp=error.http_resp)
    return exceptions.translate_status_exception(error, api_instance, api_method)
