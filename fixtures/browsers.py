import pytest
from _pytest.fixtures import SubRequest  # Импортируем класс SubRequest для аннотации
from playwright.sync_api import Playwright, Page

from config import settings
from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from tools.routes import AppRoute


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:  # noqa
    yield from initialize_playwright_page(playwright, test_name=request.node.name) # noqa


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        email="user.name@gmail.com",
        username="username",
        password="password"
    )
    registration_page.click_registration_button()

    # Сохраняем данные авторизации в файл
    context.storage_state(path=settings.browser_state_file)
    browser.close()


@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page: # noqa
    yield from initialize_playwright_page( # noqa
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file
    )