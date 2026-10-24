from data import (
    LISTING_DESCRIPTION,
    LISTING_PRICE,
    UNAUTHORIZED_LISTING_MESSAGE,
    generate_listing_title,
)
from pages import HomePage, ListingPage, LoginPage, ProfilePage


class TestListing:
    def test_unauthorized_user_cannot_create_listing(self, driver):
        home_page = HomePage(driver)
        listing_page = ListingPage(driver)
        home_page.open_new_listing()
        assert listing_page.unauthorized_message() == UNAUTHORIZED_LISTING_MESSAGE

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
            description=LISTING_DESCRIPTION,
            price=LISTING_PRICE,
        )
        home_page.open_profile()
        assert profile_page.listing_is_visible(listing_title) is True
