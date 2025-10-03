import pytest
from playwright.sync_api import Playwright, Page, expect

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:  # noqa
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()  # noqa
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
    registration_page.click_registration_button()

    # Сохраняем данные авторизации в файл
    context.storage_state(path="browser_state.json")
    browser.close()


@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:  # noqa
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser_state.json")
    yield context.new_page()  # noqa
    browser.close()
