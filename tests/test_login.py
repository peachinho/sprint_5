from data import EXPECTED_AUTHORIZED_USER_STATE
from pages import HomePage, LoginPage


class TestLogin:
    def test_login_user(self, driver, registered_user):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.open_login()
        login_page.login(registered_user["email"], registered_user["password"])
        assert (
            home_page.user_name(),
            home_page.avatar_is_visible(),
        ) == EXPECTED_AUTHORIZED_USER_STATE
