# -*- coding: utf-8 -*-

# from os.path import join, dirname

import pytest

from xero_python.accounting import models
from xero_python.api_client import ModelFinder


@pytest.mark.vcr()
def test_call_api_get_organisations(api_client, xero_tenant_id):
    # Given properly configured ApiClient
    # When calling organisations endpoint
    response = api_client.call_api(
        resource_path="https://api.xero.com/api.xro/2.0/Organisation",
        method="GET",
        path_params={},
        query_params=[],
        header_params={"xero-tenant-id": xero_tenant_id, "Accept": "application/json"},
        body=None,
        post_params=[],
        files={},
        response_type="Organisations",
        response_model_finder=ModelFinder(models),
        auth_settings=["OAuth2"],
        async_req=None,
        _return_http_data_only=True,
        collection_formats={},
        _preload_content=True,
        _request_timeout=None,
    )
    # Then expect getting list of one Organisation (Demo Company)
    assert isinstance(response, models.Organisations)
    organisations = response.organisations
    assert isinstance(organisations, list)
    assert len(organisations) == 1
    org = organisations[0]
    assert isinstance(org, models.Organisation)
    assert org.organisation_id
    assert org.is_demo_company
