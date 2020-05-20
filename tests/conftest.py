# -*- coding: utf-8 -*-
"""
    pytest global configuration file.
    Create your global fixtures in this file.
    and pytest shares those with all tests automatically.

    https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions
"""
import time

import pytest

from xero_python.api_client import ApiClient
from xero_python.api_client.configuration import Configuration
from xero_python.api_client.oauth2 import OAuth2Token


@pytest.fixture(scope="module")
def vcr_config():
    return {
        # Replace all sensitive data with "XXXXX" in cassettes
        "filter_headers": [("Authorization", "XXXXX"), ("xero-tenant-id", "XXXXX")],
        "filter_post_data_parameters": [
            ("refresh_token", "XXXXX"),
            ("client_id", "XXXXX"),
            ("client_secret", "XXXXX"),
        ],
    }


def get_token_value(key, default=None):
    try:
        from .oauth2_token import token
    except ImportError:
        return default
    else:
        return token.get(key, default)


def get_client_value(key, default=None):
    try:
        from .oauth2_client import client
    except ImportError:
        return default
    else:
        return client.get(key, default)


@pytest.fixture()
def xero_tenant_id():
    return get_client_value("tenant_id") or "xero-tenant-id"


@pytest.fixture()
def xero_client_id():
    return get_client_value("client_id") or "xero-client-id"


@pytest.fixture()
def xero_client_secret():
    return get_client_value("client_secret") or "xero-client-secret"


@pytest.fixture()
def xero_refresh_token():
    return get_token_value("refresh_token") or "xero-refresh-token"


@pytest.fixture()
def xero_id_token():
    return get_token_value("id_token") or "xero-id-token"


@pytest.fixture()
def xero_expires_in():
    return get_token_value("expires_in") or None


@pytest.fixture()
def xero_expires_at():
    return get_token_value("expires_at") or None


@pytest.fixture()
def xero_access_token():
    return (
        get_token_value("access_token") or "put-here-valid-token"
    )  # replace with valid token to re-run all API calls


@pytest.fixture()
def xero_scope():
    return [
        "email",
        "profile",
        "openid",
        "accounting.reports.read",
        "accounting.attachments.read",
        "accounting.settings",
        "accounting.settings.read",
        "accounting.attachments",
        "accounting.transactions",
        "accounting.journals.read",
        "accounting.transactions.read",
        "accounting.contacts",
        "accounting.contacts.read",
        "offline_access",
    ]


@pytest.fixture()
def oauth2_token(
    xero_access_token,
    xero_id_token,
    xero_refresh_token,
    xero_scope,
    xero_expires_in,
    xero_expires_at,
):
    return {
        "access_token": xero_access_token,
        "expires_at": xero_expires_at,
        "expires_in": xero_expires_in,
        "id_token": xero_id_token,
        "refresh_token": xero_refresh_token,
        "scope": xero_scope,
        "token_type": "Bearer",
    }


@pytest.fixture()
def oauth2_refresh_token(oauth2_token, xero_refresh_token):
    """
    similar to valid oauth2_token with expired access token
    """
    oauth2_refresh_token = dict(
        oauth2_token, expires_in=1800, expires_at=time.time() - 1
    )
    return oauth2_refresh_token


@pytest.fixture
def api_config(xero_client_id, xero_client_secret):
    config = Configuration()
    config.oauth2_token = OAuth2Token(
        client_id=xero_client_id, client_secret=xero_client_secret
    )
    return config


@pytest.fixture
def api_client(api_config, oauth2_token):
    def token_getter():
        return oauth2_token

    return ApiClient(
        configuration=api_config, pool_threads=1, oauth2_token_getter=token_getter
    )
