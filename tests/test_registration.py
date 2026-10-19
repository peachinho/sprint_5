from data import (
    DEFAULT_PASSWORD,
    EXPECTED_USER_NAME,
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
        registration_page.wait_for_success()
        actual_result = (home_page.user_name(), home_page.avatar_is_visible())
        expected_result = (EXPECTED_USER_NAME, True)
        assert actual_result == expected_result

    def test_register_with_invalid_email(self, driver):
        home_page = HomePage(driver)
        registration_page = RegistrationPage(driver)
        home_page.open_registration()
        registration_page.submit_email_only(generate_invalid_email())
        registration_page.wait_for_error()
        actual_result = (
            registration_page.error_message(),
            registration_page.email_has_error(),
            registration_page.password_has_error(),
            registration_page.confirmation_has_error(),
        )
        expected_result = ("Ошибка", True, True, True)
        assert actual_result == expected_result
    def test_register_existing_user(self, driver, registered_user):
        home_page = HomePage(driver)
        registration_page = RegistrationPage(driver)
        home_page.open_registration()
        registration_page.register(
            registered_user["email"], registered_user["password"]
        )
        registration_page.wait_for_error()
        actual_result = (
            registration_page.error_message(),
            registration_page.email_has_error(),
            registration_page.password_has_error(),
            registration_page.confirmation_has_error(),
        )
        expected_result = ("Ошибка", True, True, True)
        assert actual_result == expected_result
