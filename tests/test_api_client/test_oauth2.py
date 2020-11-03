# -*- coding: utf-8 -*-
import datetime
import time

import pytest

from tests import FakeMethod, FakeClass
from tests.conftest import get_token_value
from xero_python.api_client import ApiClient
from xero_python.api_client.configuration import Configuration
from xero_python.api_client.oauth2 import TokenApi, OAuth2Token
from xero_python.exceptions import AccessTokenExpiredError


# from os.path import join, dirname


def test_access_token_configuration(oauth2_token):
    # given oauth2_token is oauthlib token dictionary
    assert isinstance(oauth2_token, dict)
    token = OAuth2Token()
    # When updating OAuth2Token configuration
    token.update_token(**oauth2_token)
    # Then expect token configuration created
    assert token.access_token == oauth2_token["access_token"]


class FakeOAuth2Token:
    def __init__(self, value):
        self.value = value

    def get_auth_settings(self):
        return self.value


def test_configuration_uses_oauth2_token():
    # Given properly configured ApiClient
    result = "auth configuration"
    configuration = Configuration()
    configuration.oauth2_token = FakeOAuth2Token(result)
    # When auth_settings settings created
    auth_settings = configuration.auth_settings("OAuth2")
    # Then auth_settings correct value
    assert auth_settings is result


def test_auth2_token_is_valid():
    # Given valid token
    expires_at = time.time() + 3
    oauth2_token = OAuth2Token(expiration_buffer=0)
    oauth2_token.expires_at = expires_at
    # Then check token is currently valid
    assert oauth2_token.is_access_token_valid()
    # and it will be valid at specific time
    assert oauth2_token.is_access_token_valid(at_time=expires_at - 1)


def test_auth2_token_is_invalid_expiration_buffer():
    # Given valid token
    expires_at = time.time() + OAuth2Token.EXPIRATION_BUFFER_DEFAULT - 1
    oauth2_token = OAuth2Token()
    oauth2_token.expires_at = expires_at
    # Then check token is currently invalid (expiration buffer applied)
    assert not oauth2_token.is_access_token_valid()
    # and it will be valid at specific time (expiration buffer not applied)
    assert oauth2_token.is_access_token_valid(at_time=expires_at - 1)


def test_auth2_token_is_valid_indefinitely():
    # Given indefinitely valid token
    far_future = datetime.datetime.today() + datetime.timedelta(days=365)
    oauth2_token = OAuth2Token()
    # Then check token is currently valid
    assert oauth2_token.is_access_token_valid()
    # and it will be valid in far future
    assert oauth2_token.is_access_token_valid(at_time=far_future.timestamp())


def test_auth2_get_valid_token():
    # given OAuth2Token with valid access_token
    token = "access token value"
    oauth2_token = OAuth2Token()
    oauth2_token.access_token = token
    # Then correct access token value expected
    assert oauth2_token.get_valid_access_token() == token


def test_auth2_get_invalid_token():
    # given OAuth2Token with invalid access_token
    token = "access token value"
    expires_at = time.time() - 4
    oauth2_token = OAuth2Token()
    oauth2_token.access_token = token
    oauth2_token.expires_at = expires_at
    # Then correct access token value expected
    with pytest.raises(AccessTokenExpiredError):
        oauth2_token.get_valid_access_token()
    with pytest.raises(AccessTokenExpiredError):
        oauth2_token.get_valid_access_token(at_time=expires_at + 1)


def test_auth2_refresh_access_token():
    # given OAuth2Token with expired access_token
    api_client = FakeClass()
    api_client.set_oauth2_token = FakeMethod()
    refresh_token = "refresh-token-value"
    scope = [
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
    new_token = {
        "id_token": "new-id-token-value",
        "access_token": "new-access-token-value",
        "expires_in": 1800,
        "expires_at": time.time() + 1800,
        "token_type": "Bearer",
        "refresh_token": "new-refresh-token-value",
        "scope": scope,
    }
    oauth2_token = OAuth2Token(client_id="client_id", client_secret="client_secret")
    oauth2_token.refresh_token = refresh_token
    oauth2_token.scope = scope
    oauth2_token.fetch_access_token = FakeMethod(return_value=new_token)
    # When refreshing access_token
    assert oauth2_token.refresh_access_token(api_client=api_client)
    # Then expected set new token function called
    assert len(oauth2_token.fetch_access_token.calls) == 1
    assert len(api_client.set_oauth2_token.calls) == 1
    call_args, call_kwargs = api_client.set_oauth2_token.calls[0]
    assert call_args == (new_token,)
    assert call_kwargs == {}
    # Then expected new valid access and refresh tokens set on oauth2_token
    assert oauth2_token.expires_at == new_token["expires_at"]
    assert oauth2_token.is_access_token_valid()
    assert oauth2_token.id_token == new_token["id_token"]
    assert oauth2_token.expires_in == new_token["expires_in"]
    assert oauth2_token.token_type == new_token["token_type"]
    assert oauth2_token.scope == new_token["scope"]
    assert oauth2_token.access_token == new_token["access_token"]
    assert oauth2_token.refresh_token == new_token["refresh_token"]


def test_auth2_fetch_access_token():
    # Given OAuth2Token with valid refresh_token
    oauth2_token = OAuth2Token()
    token_valid_from = time.time()
    scope = (
        "email profile openid accounting.reports.read "
        "accounting.attachments.read accounting.settings "
        "accounting.settings.read accounting.attachments "
        "accounting.transactions accounting.journals.read "
        "accounting.transactions.read accounting.contacts "
        "accounting.contacts.read offline_access"
    )
    new_token = {
        "id_token": "new-id-token-value",
        "access_token": "new-access-token-value",
        "expires_in": 1800,
        "token_type": "Bearer",
        "refresh_token": "new-refresh-token-value",
        "scope": scope,
    }
    oauth2_token.call_refresh_token_api = FakeMethod(return_value=new_token.copy())
    token_api = None
    # When we fetch new oauth2 token
    received_token = oauth2_token.fetch_access_token(
        token_api=token_api, token_valid_from=token_valid_from
    )
    # Then new token valid token to be received
    assert len(oauth2_token.call_refresh_token_api.calls) == 1
    assert received_token["id_token"] == new_token["id_token"]
    assert received_token["access_token"] == new_token["access_token"]
    assert received_token["expires_in"] == new_token["expires_in"]
    assert received_token["token_type"] == new_token["token_type"]
    assert received_token["refresh_token"] == new_token["refresh_token"]
    assert received_token["scope"] == scope.split()
    assert received_token["expires_at"] == token_valid_from + new_token["expires_in"]


def test_auth2_call_refresh_token_api(oauth2_refresh_token):
    # Given valid refresh token and client credentials
    oauth2_token = OAuth2Token()
    oauth2_token.update_token(**oauth2_refresh_token)
    token = {}
    token_api = FakeClass()
    token_api.refresh_token = FakeMethod(return_value=token)
    # When refresh token API endpoint called
    new_token = oauth2_token.call_refresh_token_api(token_api)
    # Then new oauth2 token received
    assert len(token_api.refresh_token.calls) == 1
    call_args, call_kwargs = token_api.refresh_token.calls[0]
    assert call_args == (oauth2_token.refresh_token, oauth2_token.scope)
    assert call_kwargs == {}
    assert new_token is token

def test_auth2_call_refresh_token_api_without_id_token(oauth2_token_without_id_token):
    # Given valid refresh token and client credentials without using OpenID scope (id_token absent)
    oauth2_token = OAuth2Token()
    oauth2_token.update_token(**oauth2_token_without_id_token)
    token = {}
    token_api = FakeClass()
    token_api.refresh_token = FakeMethod(return_value=token)
    # When refresh token API endpoint called
    new_token = oauth2_token.call_refresh_token_api(token_api)
    # Then new oauth2 token received
    assert len(token_api.refresh_token.calls) == 1
    call_args, call_kwargs = token_api.refresh_token.calls[0]
    assert call_args == (oauth2_token.refresh_token, oauth2_token.scope)
    assert call_kwargs == {}
    assert new_token is token


def test_token_api_refresh_token(
    xero_client_id, xero_client_secret, xero_scope, vcr, vcr_cassette_name
):
    # Given all oauth2 credential and refresh token
    api_client = ApiClient(pool_threads=1)
    token_api = TokenApi(api_client, xero_client_id, xero_client_secret)
    refresh_token = get_token_value("test_refresh_token") or "test-refresh-token"
    # When getting new token
    with vcr.use_cassette(vcr_cassette_name, record_mode="none") as cassette:
        token = token_api.refresh_token(refresh_token, xero_scope)
        assert cassette.all_played
    # uncomment to save new token for next run use
    # with open(join(dirname(__file__), "oauth2_token.py"), "w") as token_file:
    #     token_file.write("token = {!r}".format(token))
    # Then new oauth2 token received
    assert isinstance(token, dict)
    assert token.get("refresh_token")
    assert token["refresh_token"] != refresh_token
    assert token.get("access_token")
    assert token.get("expires_in")
    assert token.get("id_token")
    assert token.get("token_type")
    assert token.get("scope")
    assert token["scope"].split() == xero_scope
