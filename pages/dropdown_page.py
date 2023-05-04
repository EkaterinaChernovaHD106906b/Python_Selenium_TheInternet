import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DropDownPage(BasePage):
    DROPDOWN = (By.CSS_SELECTOR, 'select#dropdown option')
    OPTION_ONE = (By.XPATH, '//select//option[2]')
    OPTION_TWO = (By.XPATH, '//select//option[3]')

    def check_options(self):
        options_list = self.elements_are_present(self.DROPDOWN)
        count = 5
        while count != 0:
            option = options_list[random.randint(1, 2)]
            if count > 0:
                option.click()
                print(option.text)
                count -= 1
            else:
                break

    # self.element_is_present(self.OPTION_ONE).click()
