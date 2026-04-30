import pytest
import requests

# Integration Testing - is_valid_email integrated with the /api/email-test endpoint.

@pytest.fixture
def base_url():
    return "http://127.0.0.1:8000"


def test_email_valid(base_url):
    r = requests.get(
        f"{base_url}/api/email-test/",
        params={"email": "test@example.com"}
    )
    assert r.status_code == 200
    assert r.json()["valid"] is True


def test_email_invalid(base_url):
    r = requests.get(
        f"{base_url}/api/email-test/",
        params={"email": "bad-email"}
    )
    assert r.status_code == 200
    assert r.json()["valid"] is False


def test_email_missing(base_url):
    r = requests.get(f"{base_url}/api/email-test/")
    assert r.status_code == 400
