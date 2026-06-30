# -*- coding: utf-8 -*-
"""
Tests for xero_python.rest.RESTResponse header access.

Regression test for #195: RESTResponse must read response headers via
``HTTPResponse.headers`` instead of the deprecated ``getheaders()`` /
``getheader()`` accessors, which urllib3 schedules for removal.
"""
from urllib3.response import HTTPResponse

from xero_python.rest import RESTResponse


class _SpyResponse:
    """Stand-in for a urllib3 response whose deprecated header accessors
    raise if used, so the test pins RESTResponse to ``.headers``."""

    def __init__(self, headers):
        self.headers = headers
        self.status = 200
        self.reason = "OK"
        self.data = b"{}"

    def getheaders(self):  # pragma: no cover - must never be called
        raise AssertionError("RESTResponse must not call deprecated getheaders()")

    def getheader(self, name, default=None):  # pragma: no cover
        raise AssertionError("RESTResponse must not call deprecated getheader()")


def test_getheaders_returns_all_headers_without_deprecated_accessor():
    response = RESTResponse(_SpyResponse({"Content-Type": "application/json",
                                          "X-Custom": "value"}))
    headers = response.getheaders()
    assert headers["Content-Type"] == "application/json"
    assert headers["X-Custom"] == "value"


def test_getheader_returns_named_header_and_default_without_deprecated_accessor():
    response = RESTResponse(_SpyResponse({"X-Custom": "value"}))
    assert response.getheader("X-Custom") == "value"
    assert response.getheader("Missing") is None
    assert response.getheader("Missing", "fallback") == "fallback"


def test_works_against_real_urllib3_response():
    resp = HTTPResponse(
        body=b"{}",
        headers={"Content-Type": "application/json", "X-Custom": "value"},
        status=200,
        preload_content=False,
    )
    response = RESTResponse(resp)
    assert response.getheaders()["X-Custom"] == "value"
    assert response.getheader("X-Custom") == "value"
    assert response.getheader("Missing", "fallback") == "fallback"
