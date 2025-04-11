# -*- coding: utf-8 -*-

from xero import exceptions


def translate_status_exception(error, api_instance, api_method):
    """
    Translate HTTPStatusException into proper Xero API status error
    :param error: HTTPStatusException
    :param api_instance: xero api instance exception occurred to
    :param api_method: xero api instance method name exception occurred to
    :return: HTTPStatusException
    """
    if error.status == 400:
        if error.http_resp.text == '{"error":"invalid_grant"}':
            return exceptions.OAuth2InvalidGrantError(http_resp=error.http_resp)
        return exceptions.BadRequestException(http_resp=error.http_resp)
    return exceptions.translate_status_exception(error, api_instance, api_method)
