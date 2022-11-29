from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class BasePage:
    title = (By.TAG_NAME, "title")

    def __init__(self, driver):
        self.driver = driver

    def get_title_page(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(self.title))
