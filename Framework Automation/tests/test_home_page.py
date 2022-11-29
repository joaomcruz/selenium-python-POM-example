from config.config import ConfigTests
from pages.home_page import HomePage
from pages.home_page import BasePage
from tests.test_base import BaseTest
import pytest
from selenium import webdriver


class TestHomePage(BaseTest):

    def test_assert_page_title(self):
        homepage_test = HomePage(self.driver)
        page_title = homepage_test.get_title_page()
        print(page_title)
        # assert page_title == ConfigTests.home_page_title

    def test_assert_login_working(self):
        homepage_test = HomePage(self.driver)
        login_button = homepage_test.get_login_button()
        login_button.click()
        # page_title = asserting_login.get_title()
        # assert page_title == ConfigTests.login_page_title
