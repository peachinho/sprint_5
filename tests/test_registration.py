from data import (
    DEFAULT_PASSWORD,
    EXPECTED_AUTHORIZED_USER_STATE,
    EXPECTED_REGISTRATION_ERROR_STATE,
    generate_email,
    generate_invalid_email,
)
from pages import HomePage, RegistrationPage


class TestRegistration:
    def test_register_new_user(self, driver):
        home_page = HomePage(driver)
        registration_page = RegistrationPage(driver)
        home_page.open_registration()
        registration_page.register(generate_email(), DEFAULT_PASSWORD)
        assert (
            home_page.user_name(),
            home_page.avatar_is_visible(),
        ) == EXPECTED_AUTHORIZED_USER_STATE

    def test_register_with_invalid_email(self, driver):
        home_page = HomePage(driver)
        registration_page = RegistrationPage(driver)
        home_page.open_registration()
        registration_page.submit_email_only(generate_invalid_email())
        assert (
            registration_page.error_message(),
            registration_page.email_has_error(),
            registration_page.password_has_error(),
            registration_page.confirmation_has_error(),
        ) == EXPECTED_REGISTRATION_ERROR_STATE

    def test_register_existing_user(self, driver, registered_user):
        home_page = HomePage(driver)
        registration_page = RegistrationPage(driver)
        home_page.open_registration()
        registration_page.register(
            registered_user["email"], registered_user["password"]
        )
        assert (
            registration_page.error_message(),
            registration_page.email_has_error(),
            registration_page.password_has_error(),
            registration_page.confirmation_has_error(),
        ) == EXPECTED_REGISTRATION_ERROR_STATE
