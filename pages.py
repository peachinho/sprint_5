from selenium.common.exceptions import (
    ElementNotInteractableException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

from data import BASE_URL
from locators import (
    HeaderLocators,
    ListingLocators,
    LoginLocators,
    ProfileLocators,
    RegistrationLocators,
)


class BasePage:
    def __init__(self, driver, timeout: int = 20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        self.driver.get(BASE_URL)

    def click(self, locator) -> None:
        def click_element(driver):
            try:
                element = expected.element_to_be_clickable(locator)(driver)
                if not element:
                    return False
                element.click()
                return True
            except (ElementNotInteractableException, StaleElementReferenceException):
                return False

        self.wait.until(click_element)

    def fill(self, locator, value: str) -> None:
        def enter_value(driver):
            try:
                element = driver.find_element(*locator)
                if not element.is_displayed() or not element.is_enabled():
                    return False
                element.clear()
                element.send_keys(value)
                return True
            except (ElementNotInteractableException, StaleElementReferenceException):
                return False

        self.wait.until(enter_value)

    def text(self, locator) -> str:
        return self.wait.until(expected.visibility_of_element_located(locator)).text

    def is_visible(self, locator) -> bool:
        try:
            self.wait.until(expected.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_absent(self, locator) -> bool:
        try:
            self.wait.until(expected.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def class_name(self, locator) -> str:
        return self.wait.until(expected.presence_of_element_located(locator)).get_attribute(
            "class"
        )

    def select_hidden_radio(self, locator) -> None:
        element = self.wait.until(expected.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click()", element)
        self.wait.until(expected.element_located_to_be_selected(locator))


class HomePage(BasePage):
    def open_login(self) -> None:
        self.click(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)

    def open_registration(self) -> None:
        self.open_login()
        self.click(LoginLocators.NO_ACCOUNT_BUTTON)

    def open_new_listing(self) -> None:
        self.click(HeaderLocators.CREATE_LISTING_BUTTON)

    def open_profile(self) -> None:
        self.click(HeaderLocators.AVATAR_BUTTON)

    def logout(self) -> None:
        self.click(HeaderLocators.LOGOUT_BUTTON)

    def user_name(self) -> str:
        return self.text(HeaderLocators.USER_NAME)

    def avatar_is_visible(self) -> bool:
        return self.is_visible(HeaderLocators.AVATAR_BUTTON)

    def avatar_is_absent(self) -> bool:
        return self.is_absent(HeaderLocators.AVATAR_BUTTON)

    def login_button_is_visible(self) -> bool:
        return self.is_visible(HeaderLocators.LOGIN_AND_REGISTRATION_BUTTON)

    def user_name_is_absent(self) -> bool:
        return self.is_absent(HeaderLocators.USER_NAME)


class LoginPage(BasePage):
    def login(self, email: str, password: str) -> None:
        self.fill(LoginLocators.EMAIL_INPUT, email)
        self.fill(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)


class RegistrationPage(BasePage):
    def register(self, email: str, password: str) -> None:
        self.fill(RegistrationLocators.EMAIL_INPUT, email)
        self.fill(RegistrationLocators.PASSWORD_INPUT, password)
        self.fill(RegistrationLocators.PASSWORD_CONFIRMATION_INPUT, password)
        self.click(RegistrationLocators.CREATE_ACCOUNT_BUTTON)

    def submit_email_only(self, email: str) -> None:
        self.fill(RegistrationLocators.EMAIL_INPUT, email)
        self.click(RegistrationLocators.CREATE_ACCOUNT_BUTTON)

    def wait_for_registration_form_to_close(self) -> None:
        self.wait.until(
            expected.invisibility_of_element_located(
                RegistrationLocators.CREATE_ACCOUNT_BUTTON
            )
        )

    def error_message(self) -> str:
        return self.text(RegistrationLocators.EMAIL_ERROR_MESSAGE)

    def email_has_error(self) -> bool:
        return "inputError" in self.class_name(
            RegistrationLocators.EMAIL_ERROR_CONTAINER
        )

    def password_has_error(self) -> bool:
        return "inputError" in self.class_name(
            RegistrationLocators.PASSWORD_ERROR_CONTAINER
        )

    def confirmation_has_error(self) -> bool:
        return "inputError" in self.class_name(
            RegistrationLocators.PASSWORD_CONFIRMATION_ERROR_CONTAINER
        )


class ListingPage(BasePage):
    def unauthorized_message(self) -> str:
        return self.text(ListingLocators.UNAUTHORIZED_MESSAGE)

    def create_listing(
        self,
        title: str,
        description: str,
        price: str,
    ) -> None:
        self.fill(ListingLocators.TITLE_INPUT, title)
        self.fill(ListingLocators.DESCRIPTION_INPUT, description)
        self.fill(ListingLocators.PRICE_INPUT, price)
        self.click(ListingLocators.CATEGORY_DROPDOWN_BUTTON)
        self.click(ListingLocators.CATEGORY_BOOKS_OPTION)
        self.click(ListingLocators.CITY_DROPDOWN_BUTTON)
        self.click(ListingLocators.CITY_KAZAN_OPTION)
        self.select_hidden_radio(ListingLocators.USED_CONDITION_RADIO)
        self.click(ListingLocators.PUBLISH_BUTTON)
        self.wait.until(expected.url_to_be(BASE_URL))


class ProfilePage(BasePage):
    def listing_is_visible(self, title: str) -> bool:
        self.wait.until(
            expected.visibility_of_element_located(ProfileLocators.MY_LISTINGS_TITLE)
        )
        return self.is_visible(ProfileLocators.listing_title(title))
