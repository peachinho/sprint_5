import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import DEFAULT_PASSWORD, generate_email
from pages import HomePage, RegistrationPage


def build_driver():
    options = Options()
    options.add_argument("--window-size=1440,1200")
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")
    return webdriver.Chrome(options=options)


@pytest.fixture
def driver():
    browser = build_driver()
    browser.get("https://qa-desk.education-services.ru/")
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def registered_user():
    browser = build_driver()
    email = generate_email()
    try:
        home_page = HomePage(browser)
        registration_page = RegistrationPage(browser)
        home_page.open()
        home_page.open_registration()
        registration_page.register(email, DEFAULT_PASSWORD)
        registration_page.wait_for_registration_form_to_close()
    finally:
        browser.quit()
    return {"email": email, "password": DEFAULT_PASSWORD}
