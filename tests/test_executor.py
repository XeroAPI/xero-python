# -*- coding: utf-8 -*-
import pytest
import urllib3


def test_the_tests():
    """
    to test the tests configuration
    """

    assert True is True


@pytest.mark.vcr()
def test_vcr():
    """
    Test VCR.py records and plays http requests properly
    """
    http_manager = urllib3.PoolManager()
    response = http_manager.request(
        "GET", "https://developer.xero.com/documentation/oauth2/auth-flow"
    )
    assert response.status == 200
    assert "Xero is a multi-tenanted platform." in response.data.decode("utf-8")
