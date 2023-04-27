import random
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    CHECKBOXES = (By.CSS_SELECTOR, 'div[class="row"] div[id="content"] form[id="checkboxes"] input')

    def click_checkbox(self):
        checkboxes = self.elements_are_visible(self.CHECKBOXES)
        count = 5
        while count != 0:
            checkbox = checkboxes[random.randint(0, 1)]
            if count > 0:
                self.go_to_element(checkbox)
                checkbox.click()
                count -= 1
            else:
                break
        time.sleep(5)
