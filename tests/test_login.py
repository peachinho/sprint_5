from data import EXPECTED_USER_NAME
from pages import HomePage, LoginPage


class TestLogin:
    def test_login_user(self, driver, registered_user):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.open_login()
        login_page.login(registered_user["email"], registered_user["password"])
        actual_result = (home_page.user_name(), home_page.avatar_is_visible())
        expected_result = (EXPECTED_USER_NAME, True)
        assert actual_result == expected_result
