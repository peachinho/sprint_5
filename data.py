from uuid import uuid4


BASE_URL = "https://qa-desk.education-services.ru/"
DEFAULT_PASSWORD = "12345678"
EXPECTED_USER_NAME = "User."
EXPECTED_AUTHORIZED_USER_STATE = (EXPECTED_USER_NAME, True)
EXPECTED_LOGOUT_STATE = (True, True, True)
REGISTRATION_ERROR_MESSAGE = "Ошибка"
EXPECTED_REGISTRATION_ERROR_STATE = (
    REGISTRATION_ERROR_MESSAGE,
    True,
    True,
    True,
)
LISTING_DESCRIPTION = "Объявление создано автоматизированным тестом"
LISTING_PRICE = "1500"
UNAUTHORIZED_LISTING_MESSAGE = "Чтобы разместить объявление, авторизуйтесь"


def generate_email() -> str:
    return f"autotest-{uuid4().hex}@mail.ru"


def generate_invalid_email() -> str:
    return f"invalid-{uuid4().hex}"


def generate_listing_title() -> str:
    return f"Autotest listing {uuid4().hex}"
