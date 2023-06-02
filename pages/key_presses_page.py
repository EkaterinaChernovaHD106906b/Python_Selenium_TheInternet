from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class KeyPressesPage(BasePage):
    INPUT = (By.CSS_SELECTOR, 'input#target')
    RESULT = (By.CSS_SELECTOR, 'p#result')

    def input_keys(self):
        keys = ['u', 's', 'e', 'r']
        input_keys = []
        for key in keys:
            self.element_is_visible(self.INPUT).send_keys(key)
            input_key = self.element_is_visible(self.RESULT).text
            input_keys.append(input_key)
        return input_keys



