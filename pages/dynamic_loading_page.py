from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    FIRST_HREF = (By.CSS_SELECTOR, 'a[href="/dynamic_loading/1"]')
    SECOND_HREF = (By.CSS_SELECTOR, 'a[href="/dynamic_loading/2"]')
    START_BUTTON = (By.CSS_SELECTOR, 'div#start button')
    LOADING_IMG = (By.CSS_SELECTOR, 'img[src="/img/ajax-loader.gif"]')
    HELLO = (By.CSS_SELECTOR, 'div#finish h4')

    def check_first_href(self, href):
        if href == 'first':
            self.element_is_visible(self.FIRST_HREF).click()
            self.element_is_visible(self.START_BUTTON).click()
            self.element_is_visible(self.LOADING_IMG)
            text = self.element_is_visible(self.HELLO).text
            return text
        if href == 'second':
            self.element_is_visible(self.SECOND_HREF).click()
            self.element_is_visible(self.START_BUTTON).click()
            self.element_is_visible(self.LOADING_IMG)
            text = self.element_is_visible(self.HELLO).text
            return text
