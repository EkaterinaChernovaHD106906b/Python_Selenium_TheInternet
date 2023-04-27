from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContextMenuPage(BasePage):

    CONTEXT_MENU = (By.CSS_SELECTOR, '#hot-spot')

    def click_on_context_menu(self):
        menu = self.element_is_visible(self.CONTEXT_MENU)
        action = ActionChains(self.driver)
        action.context_click(menu).perform()
        alert = self.alert_is_present()
        text = alert.text
        alert.accept()
        return text

