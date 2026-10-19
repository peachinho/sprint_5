from uuid import uuid4


BASE_URL = "https://qa-desk.education-services.ru/"
DEFAULT_PASSWORD = "12345678"
EXPECTED_USER_NAME = "User."


def generate_email() -> str:
    return f"autotest-{uuid4().hex}@mail.ru"


def generate_invalid_email() -> str:
    return f"invalid-{uuid4().hex}"


def generate_listing_title() -> str:
    return f"Autotest listing {uuid4().hex}"
