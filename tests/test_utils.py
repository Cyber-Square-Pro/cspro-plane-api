import pytest
from utils.email import is_valid_email

# Unit Testing - is_valid_email for valid emails
@pytest.mark.parametrize("email", [
    "test@example.com",
    "user.name@domain.co",
    "user_name123@sub.domain.org",
    "email+tag@gmail.com",
])
def test_valid_emails(email):
    assert is_valid_email(email)

# Unit Testing - is_valid_email for invalid emails
@pytest.mark.parametrize("email", [
    "plainaddress",
    "@missingusername.com",
    "user@.com",
    "user@com",
    "user@domain,com",
])
def test_invalid_emails(email):
    assert not is_valid_email(email)