import pytest
from playwright.sync_api import Page, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка Заголовка Courses
    courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    # Проверка Иконки
    courses_empty_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(courses_empty_icon).to_be_visible()

    # Проверка заголовка
    courses_empty_title_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(courses_empty_title_text).to_be_visible()
    expect(courses_empty_title_text).to_have_text("There is no results")

    # Проверка текста
    courses_empty_description_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(courses_empty_description_text).to_be_visible()
    expect(courses_empty_description_text).to_have_text(
        "Results from the load test pipeline will be displayed here")
