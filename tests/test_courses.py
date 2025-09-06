import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем поле Email
        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        expect(email_input).to_be_visible()
        email_input.fill("user.name@gmail.com")

        # Заполняем поле Username
        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        expect(username_input).to_be_visible()
        username_input.fill("username")

        # Заполняем поле Password
        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        expect(password_input).to_be_visible()
        password_input.fill("password")

        # Нажимаем на кнопку Registration
        registration_button = page.get_by_test_id("registration-page-registration-button")
        expect(registration_button).to_be_enabled()
        registration_button.click()

        # Сохраняем данные авторизации в файл
        context.storage_state(path="browser_state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser_state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверка Заголовка Courses
        courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        # Проверка Иконки
        courses_empty_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(courses_empty_icon).to_be_visible()

        # Проверка заголовка
        courses_empty_title_text = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(courses_empty_title_text).to_be_visible()
        expect(courses_empty_title_text).to_have_text("There is no results")

        # Проверка текста
        courses_empty_description_text = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(courses_empty_description_text).to_be_visible()
        expect(courses_empty_description_text).to_have_text(
            "Results from the load test pipeline will be displayed here")
