from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DisappearingElementsPage(BasePage):
    HOME = (By.CSS_SELECTOR, 'a[href="/"]')
    ABOUT = (By.CSS_SELECTOR, 'a[href="/about/"]')
    CONTACT_US = (By.CSS_SELECTOR, 'a[href="/contact-us/"]')
    PORTFOLIO = (By.CSS_SELECTOR, 'a[href="/portfolio/"]')
    GALLERY = (By.CSS_SELECTOR, 'a[href="/gallery/"]')
    TEXT = (By.CSS_SELECTOR, 'h1')

    def click_different_button(self, type_click):
        if type_click == 'home':
            self.element_is_visible(self.HOME).click()
            return self.element_is_not_visible(self.HOME)
        if type_click == 'about':
            self.element_is_visible(self.ABOUT).click()
            text = self.element_is_visible(self.TEXT).text
            return self.element_is_not_visible(self.ABOUT), self.element_is_visible(self.TEXT)
        if type_click == 'contact us':
            self.element_is_visible(self.CONTACT_US).click()
            return self.element_is_not_visible(self.CONTACT_US), self.element_is_visible(self.TEXT)
        if type_click == 'portfolio':
            self.element_is_visible(self.PORTFOLIO).click()
            return self.element_is_not_visible(self.PORTFOLIO), self.element_is_visible(self.TEXT)
        if type_click == 'gallery':
            self.element_is_visible(self.GALLERY).click()
            return self.element_is_not_visible(self.GALLERY), self.element_is_visible(self.TEXT)



