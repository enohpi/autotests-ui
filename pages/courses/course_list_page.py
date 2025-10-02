from dataclasses import dataclass

from playwright.sync_api import Page, expect

from pages.base_page import BasePage

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import (
    CoursesListToolbarViewComponent,
)
from components.views.empty_view_component import EmptyViewComponent


@dataclass
class CheckVisibleCourseCardParams:
    index: int  # Индекс карточки в списке курсов
    title: str  # Ожидаемый заголовок курса
    max_score: str  # Ожидаемый максимальный балл
    min_score: str  # Ожидаемый минимальный балл
    estimated_time: str  # Ожидаемое время прохождения


class CoursesListPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.course_view = CourseViewComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)
        self.empty_view = EmptyViewComponent(page, "courses-list")

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here",
        )
