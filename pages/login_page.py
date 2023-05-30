from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, 'input#username')
    PASSWORD = (By.CSS_SELECTOR, 'input#password')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')
    RESULT = (By.CSS_SELECTOR, 'div#flash')

    def login_success(self):
        user = 'tomsmith'
        password = 'SuperSecretPassword!'
        self.element_is_visible(self.USERNAME).send_keys(user)
        self.element_is_visible(self.PASSWORD).send_keys(password)
        self.element_is_visible(self.BUTTON_SUBMIT).click()
        result = self.element_is_visible(self.RESULT).text
        return result

    def login_unsuccessful(self):
        user = next(generated_person())
        user_name = user.first_name
        password = user.password
        self.element_is_visible(self.USERNAME).send_keys(user_name)
        self.element_is_visible(self.PASSWORD).send_keys(password)
        self.element_is_visible(self.BUTTON_SUBMIT).click()
        result = self.element_is_visible(self.RESULT).text
        return result



