from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WindowsPage(BasePage):
    CLICK_HERE = (By.CSS_SELECTOR, 'div.example a[target="_blank"]')
    NEW_WINDOW = (By.CSS_SELECTOR, 'div.example h3')

    def open_new_window(self):
        self.element_is_visible(self.CLICK_HERE).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_visible(self.NEW_WINDOW).text
        return text
