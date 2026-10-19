from pages import HomePage, LoginPage


class TestLogout:
    def test_logout_user(self, driver, registered_user):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.open_login()
        login_page.login(registered_user["email"], registered_user["password"])
        home_page.logout()
        actual_result = (
            home_page.login_button_is_visible(),
            home_page.avatar_is_absent(),
            home_page.user_name_is_absent(),
        )
        expected_result = (True, True, True)
        assert actual_result == expected_result
