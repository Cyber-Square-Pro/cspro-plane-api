import re

EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

# is_valid_email checks an email string against a regular expression.
def is_valid_email(email: str) -> bool:
    return EMAIL_REGEX.match(email) is not None