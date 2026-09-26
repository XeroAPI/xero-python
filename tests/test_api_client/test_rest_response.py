from xero_python.rest import RESTResponse


class DummyResponse:
    def __init__(self):
        self.status = 200
        self.reason = "OK"
        self.data = b"{}"
        self.headers = {
            "Content-Disposition": "attachment; filename=test.json",
            "X-Trace-Id": "abc123",
        }


def test_rest_response_reads_headers_without_deprecated_urllib3_helpers():
    response = RESTResponse(DummyResponse())

    assert response.getheaders() == {
        "Content-Disposition": "attachment; filename=test.json",
        "X-Trace-Id": "abc123",
    }
    assert response.getheader("Content-Disposition") == "attachment; filename=test.json"
    assert response.getheader("Missing", "fallback") == "fallback"
