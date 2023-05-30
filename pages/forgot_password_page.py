from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, 'input#email')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button#form_submit')
    H1 = (By.CSS_SELECTOR, 'body h1')

    def retrieve_password(self):
        user = next(generated_person())
        e_mail = user.e_mail
        self.element_is_visible(self.EMAIL).send_keys(e_mail)
        self.element_is_visible(self.BUTTON_SUBMIT).click()
        result = self.element_is_visible(self.H1).text
        return result
