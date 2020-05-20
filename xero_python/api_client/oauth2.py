# -*- coding: utf-8 -*-
import json
import time

from xero_python.exceptions import AccessTokenExpiredError


class TokenApi:
    """
    Api class handles interactions with xero token API endpoints
    """

    refresh_token_url = "https://identity.xero.com/connect/token"

    def __init__(self, api_client, client_id, client_secret):
        self.api_client = api_client
        self.client_id = client_id
        self.client_secret = client_secret

    def refresh_token(self, refresh_token, scope):
        """
        Call xero identity API to refresh auth2 access token using refresh token
        :param refresh_token: str auth2 refresh token
        :param scope: list of auth2 scopes
        :return: dictionary with new auth2 token
        """
        post_data = {
            "grant_type": "refresh_token",
            "scope": " ".join(scope),
            "refresh_token": refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response, status, headers = self.api_client.call_api(
            self.refresh_token_url,
            "POST",
            header_params={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            post_params=post_data,
            auth_settings=None,  # important to prevent infinite recursive loop
            _preload_content=False,
        )
        if status != 200:
            # todo improve error handling
            raise Exception(
                "refresh token status {} {} {!r}".format(status, response, headers)
            )
        # todo validate response is json
        return self.parse_token_response(response)

    def parse_token_response(self, response):
        """
        Parse token data from http response
        :param response: refresh token response
        :return: parsed json data as token dictionary
        """
        # todo decode based on codeset in response content type
        data = response.data.decode("utf-8")
        return json.loads(data)


class OAuth2Token:
    """
    Class to handle oauth2 access and refresh token
    * provides auth header for all `ApiClient` calls
    * implements oauth2 token refresh flow to fetch new valid oauth2 token.
    todo add hooks/signals to:
        * export new refreshed token
        * import new token from outside code
    """

    # refresh access token 60 seconds before it expires
    EXPIRATION_BUFFER_DEFAULT = 60

    def __init__(
        self,
        # rest needed to be able to refresh access_token
        client_id=None,
        client_secret=None,
        expiration_buffer=EXPIRATION_BUFFER_DEFAULT,
    ):
        """
        OAuth2Token constructor,
        client_id and client_server needed to be able to refresh access_token
        :param str client_id: oauth2 client id
        :param str client_secret: oauth2 client secret
        :param int expiration_buffer: refresh access token x seconds prior to expiration
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.expiration_buffer = expiration_buffer

        # initialize oauth2 token attributes.
        # use self.update_token(...) to set those attributes
        self.token_type = "Bearer"
        self.access_token = self.id_token = self.refresh_token = self.scope = None
        self.expires_at = self.expires_in = None

    def get_auth_settings(self):
        """
        Get auth method ( a callable ) providing dynamic authentication settings
        """
        # return create_auth_settings for api_client to execute
        return self.create_auth_settings

    def create_auth_settings(self, api_client):
        """
        Prepare authorization header for HTTP request
        :param api_client: ApiClient instance used to perform refresh token API call.
        :return: dictionary with authorisation details
        """
        self.update_token(**api_client.get_oauth2_token())
        access_token = self.get_valid_access_token(api_client)
        return {
            "type": "oauth2",
            "in": "header",
            "key": "Authorization",
            "value": "{type} {token}".format(type=self.token_type, token=access_token),
        }

    def is_access_token_valid(self, at_time=None):
        """
        Check current access token valid
        :param at_time: float - timestamp at which token consider valid
        :return: bool token valid ad given time
        """
        at_time = at_time or time.time() + self.expiration_buffer
        if self.expires_at is None:
            return True  # tokens without expiration considered always valid
        return self.expires_at > at_time

    def get_valid_access_token(self, api_client=None, at_time=None):
        """
        Get valid access token (check it's valid and refresh it if needed)
        :param api_client: ApiClient instance used to perform refresh token API call.
        :param at_time: float - timestamp at which token consider valid
        :return: valid auth2 access token string
        :raise: AccessTokenExpiredError
        """
        if not self.is_access_token_valid(at_time):
            if not self.refresh_access_token(api_client):
                raise AccessTokenExpiredError("Access Token has expired")
        return self.access_token

    def can_refresh_access_token(self):
        """
        Check current instance has all data required to perform refresh token API call.
        :return: bool
        """
        return (
            self.refresh_token
            and isinstance(self.scope, (list, tuple))
            and self.client_id
            and self.client_secret
        )

    def refresh_access_token(self, api_client):
        """
        Perform auth2 refresh token call.
        :param api_client:  ApiClient instance used to perform refresh token API call.
        :return: bool - True if success
        :raise: http request related errors
        """
        if not self.can_refresh_access_token():
            return False
        token_api = TokenApi(api_client, self.client_id, self.client_secret)
        new_token = self.fetch_access_token(token_api)
        self.update_token(**new_token)
        api_client.set_oauth2_token(new_token)
        return True

    def update_token(
        self,
        access_token,
        refresh_token,
        scope,
        expires_at,
        expires_in,
        token_type,
        id_token,
    ):
        """
        Set new auth2 token details
        :param access_token: str
        :param refresh_token: str
        :param scope: list of strings
        :param expires_at: float timestamp
        :param expires_in: number
        :param token_type: str
        :param id_token: str
        """
        self.access_token = access_token
        self.expires_at = expires_at
        self.expires_in = expires_in
        self.id_token = id_token
        self.refresh_token = refresh_token
        self.scope = scope
        self.token_type = token_type

    def fetch_access_token(self, token_api, token_valid_from=None):
        """
        Fetch new auth2 token and convert it into auth2 token structure
        :param token_api: TokenApi instance to perform API call.
        :param token_valid_from: float timestamp token expires_in counts from
        :return: dictionary new auth2 token
        """
        token = self.call_refresh_token_api(token_api)
        token_valid_from = token_valid_from or time.time()
        # parse new scope
        new_scope = token.get("scope")
        if new_scope:
            new_scope = str(new_scope).split()
            token["scope"] = new_scope
        # set expires_at
        expires_in = token.get("expires_in")
        if expires_in and "expires_at" not in token:
            token["expires_at"] = token_valid_from + expires_in

        return token

    def call_refresh_token_api(self, token_api):
        """
        Get a new auth2 token using current refresh token
        :param token_api: TokenApi instance
        :return: auth2 token dictionary as received from API.
        """
        return token_api.refresh_token(self.refresh_token, self.scope)
