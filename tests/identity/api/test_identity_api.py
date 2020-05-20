# -*- coding: utf-8 -*-
import pytest

from xero_python.api_client import ApiClient
from xero_python.identity import IdentityApi, models
from xero_python.rest import RESTClientObject


@pytest.fixture
def identity_api(api_client):
    return IdentityApi(api_client=api_client)


def test_identity_api_instance_configuration(identity_api):
    """
    Test IdentityApi() configured correctly
    """
    assert isinstance(identity_api, IdentityApi)
    assert isinstance(identity_api.api_client, ApiClient)
    assert isinstance(identity_api.api_client.rest_client, RESTClientObject)


@pytest.mark.vcr()
def test_get_connections(identity_api: IdentityApi):
    """
    Test IdentityApi.get_connections()
    """
    # Given correct api client and xero tenant id
    # When fetching connections
    response = identity_api.get_connections()
    # Then expect correct response with list of connections
    assert isinstance(response, list)
    assert len(response) == 1
    connection = response[0]
    assert isinstance(connection, models.Connection)
    assert connection.tenant_id
