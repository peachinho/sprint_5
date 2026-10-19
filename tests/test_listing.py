from data import generate_listing_title
from pages import HomePage, ListingPage, LoginPage, ProfilePage


class TestListing:
    def test_unauthorized_user_cannot_create_listing(self, driver):
        home_page = HomePage(driver)
        listing_page = ListingPage(driver)
        home_page.open_new_listing()
        actual_result = listing_page.unauthorized_message()
        expected_result = "Чтобы разместить объявление, авторизуйтесь"
        assert actual_result == expected_result

    def test_authorized_user_creates_listing(self, driver, registered_user):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        listing_page = ListingPage(driver)
        profile_page = ProfilePage(driver)
        listing_title = generate_listing_title()
        home_page.open_login()
        login_page.login(registered_user["email"], registered_user["password"])
        home_page.open_new_listing()
        listing_page.create_listing(
            title=listing_title,
            description="Объявление создано автоматизированным тестом",
            price="1500",
        )
        home_page.open_profile()
        actual_result = profile_page.listing_is_visible(listing_title)
        expected_result = True
        assert actual_result == expected_result
