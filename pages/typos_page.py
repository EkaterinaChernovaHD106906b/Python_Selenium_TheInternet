from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TyposPage(BasePage):
    TEXT = (By.XPATH, '//div[@class="example"]//p[2]')

    def check_typo(self):
        text_before = self.element_is_visible(self.TEXT).text
        list_text_before = text_before.split()
        typo = list_text_before[8]
        count = 2
        while count != 0:
            self.driver.refresh()
            count -= 1

        text_after = self.element_is_visible(self.TEXT).text
        list_text_after = text_after.split()
        typo2 = list_text_after[8]
        return typo, typo2



