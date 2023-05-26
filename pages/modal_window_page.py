from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ModalWindowPage(BasePage):
    LINK = (By.CSS_SELECTOR, 'a#restart-ad')
    CLOSE = (By.CSS_SELECTOR, 'div.modal-footer p')
    TEXT = (By.CSS_SELECTOR, 'div.modal-body p')

    def close_modal_window(self):
        self.element_is_visible(self.LINK).click()
        text_modal_window = self.element_is_visible(self.TEXT).text
        self.element_is_visible(self.CLOSE).click()
        return text_modal_window
