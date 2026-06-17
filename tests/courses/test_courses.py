import re

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)
        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        create_course_page.visit(AppRoute.CREATE_COURSES)
        create_course_page.image_upload_widget.check_visible(
            is_image_uploaded=False
        )
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(
            settings.test_data.image_png_file
        )
        create_course_page.image_upload_widget.check_visible(
            is_image_uploaded=True
        )

        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.course_view.check_visible(
            0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        created_course = {
            "title": "Playwright Edit",
            "estimated_time": "2 weeks",
            "description": "Playwright",
            "max_score": "100",
            "min_score": "10",
        }

        updated_course = {
            "title": "Python Edit",
            "estimated_time": "3 weeks",
            "description": "Python",
            "max_score": "90",
            "min_score": "20",
        }

        create_course_page.visit(AppRoute.CREATE_COURSES)
        create_course_page.page.wait_for_load_state("networkidle")

        create_course_page.image_upload_widget.check_visible(
            is_image_uploaded=False
        )
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(
            settings.test_data.image_png_file
        )
        create_course_page.image_upload_widget.check_visible(
            is_image_uploaded=True
        )

        create_course_page.create_course_form.fill(**created_course)
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.check_current_url(
            re.compile(r".*/#/courses")
        )
        courses_list_page.toolbar_view.check_visible()

        courses_list_page.course_view.check_visible(
            0,
            title=created_course["title"],
            estimated_time=created_course["estimated_time"],
            max_score=created_course["max_score"],
            min_score=created_course["min_score"],
        )

        courses_list_page.course_view_menu_component.click_edit(0)

        create_course_page.create_course_form.fill(**updated_course)

        create_course_page.create_course_form.check_visible(**updated_course)

        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.check_current_url(
            re.compile(r".*/#/courses")
        )
        courses_list_page.toolbar_view.check_visible()

        courses_list_page.course_view.check_visible(
            0,
            title=updated_course["title"],
            estimated_time=updated_course["estimated_time"],
            max_score=updated_course["max_score"],
            min_score=updated_course["min_score"],
        )

