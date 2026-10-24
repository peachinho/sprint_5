from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGIN_AND_REGISTRATION_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Вход и регистрация']",
    )
    CREATE_LISTING_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Разместить объявление']",
    )
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    AVATAR_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выйти']")


class LoginLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Нет аккаунта']")


class RegistrationLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    PASSWORD_CONFIRMATION_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Создать аккаунт']",
    )
    EMAIL_ERROR_CONTAINER = (By.XPATH, "//input[@name='email']/parent::*")
    PASSWORD_ERROR_CONTAINER = (By.XPATH, "//input[@name='password']/parent::*")
    PASSWORD_CONFIRMATION_ERROR_CONTAINER = (
        By.XPATH,
        "//input[@name='submitPassword']/parent::*",
    )
    EMAIL_ERROR_MESSAGE = (
        By.XPATH,
        "//span[normalize-space()='Ошибка']",
    )


class ListingLocators:
    UNAUTHORIZED_MESSAGE = (
        By.XPATH,
        "//h1[normalize-space()='Чтобы разместить объявление, авторизуйтесь']",
    )
    TITLE_INPUT = (By.CSS_SELECTOR, "input[name='name'][placeholder='Название']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price'][placeholder='Стоимость']")
    CATEGORY_DROPDOWN_BUTTON = (
        By.XPATH,
        "//input[@name='category']/following-sibling::button",
    )
    CATEGORY_BOOKS_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'options')]//button[.//span[normalize-space()='Книги']]",
    )
    CITY_DROPDOWN_BUTTON = (
        By.XPATH,
        "//input[@name='city']/following-sibling::button",
    )
    CITY_KAZAN_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'options')]//button[.//span[normalize-space()='Казань']]",
    )
    USED_CONDITION_RADIO = (
        By.CSS_SELECTOR,
        "input[name='condition'][value='Б/У']",
    )
    PUBLISH_BUTTON = (By.XPATH, "//button[normalize-space()='Опубликовать']")


class ProfileLocators:
    MY_LISTINGS_TITLE = (By.XPATH, "//*[normalize-space()='Мои объявления']")

    @staticmethod
    def listing_title(title: str) -> tuple[str, str]:
        return By.XPATH, f"//*[normalize-space()={title!r}]"
