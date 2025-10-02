from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )

    # Заполняем поле Email
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    expect(email_input).to_be_visible()
    email_input.fill("user.name@gmail.com")

    # Заполняем поле Username
    username_input = page.get_by_test_id("registration-form-username-input").locator(
        "input"
    )
    expect(username_input).to_be_visible()
    username_input.fill("username")

    # Заполняем поле Password
    password_input = page.get_by_test_id("registration-form-password-input").locator(
        "input"
    )
    expect(password_input).to_be_visible()
    password_input.fill("password")

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_visible()
    registration_button.click()

    # Проверяем наличие заголовка Dashboard
    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")
