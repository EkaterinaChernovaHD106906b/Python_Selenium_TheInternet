from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class IFramePage(BasePage):
    BODY = (By.CSS_SELECTOR, 'body#tinymce')
    TEXT = (By.CSS_SELECTOR, 'body#tinymce p')

    def input_text(self, text):
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'iframe#mce_0_ifr')
        self.driver.switch_to.frame(iframe)
        body = self.element_is_visible(self.BODY)
        body.clear()
        body.send_keys(text)
        my_text = self.element_is_visible(self.TEXT).text
        return my_text
