from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from config.config import ConfigTests


class HomePage(BasePage):
    login_button = (By.CSS_SELECTOR,
                    "body.home:nth-child(2) div.container-fixed:nth-child(1) div.headerstrip.navbar.navbar-inverse "
                    "div.container-fluid div.navbar-collapse.collapse div.navbar-right.headerstrip_blocks div.block_2 "
                    "div.navbar ul.nav.navbar-nav.main_menu li:nth-child(1) > a:nth-child(1)")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ConfigTests.url_automation_test_store)

    def get_login_button(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(self.login_button))
