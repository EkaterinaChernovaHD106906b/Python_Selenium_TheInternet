import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BasicAuthorizationPage(BasePage):
    BASIC_AUTH = (By.CSS_SELECTOR, 'div[id="content"] div h3 ')
    SUCCESS_AUTH = (By.CSS_SELECTOR, 'div[id="content"] p')

    def check_basic_auto(self):
        self.element_is_visible(self.BASIC_AUTH)
        success_auth = self.element_is_visible(self.SUCCESS_AUTH).text
        return success_auth
