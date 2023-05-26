from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DragDropPage(BasePage):
    A = (By.CSS_SELECTOR, 'div#columns div#column-a')
    B = (By.CSS_SELECTOR, 'div.column over#column-b')
    A_HEADER = (By.CSS_SELECTOR, 'div#column-a  header')
    B_HEADER = (By.CSS_SELECTOR, 'div#column-b  header')

    def check_ab_haaders(self):
        a = self.element_is_visible(self.A)
        b = self.element_is_visible(self.B)
        self.action_drag_and_drop(a, b)

        text = self.element_is_present(self.A_HEADER).text
        print(text)








