import time

import requests
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ABPage(BasePage):
    LINK = (By.CSS_SELECTOR, 'a[target="_blank"]')
    ELEMENTAL_SELENIUM = (By.CSS_SELECTOR, 'div[class="large-12 columns text-center"] h1')
    EMAIL = (By.CSS_SELECTOR, 'input[id="email"]')
    SELECT_LANGUAGE = (By.CSS_SELECTOR, 'select[class="language"]')
    CHECKBOX = (By.CSS_SELECTOR, 'label input[type="checkbox"]')

    def click_on_link(self):
        link = self.element_is_visible(self.LINK)
        link_href = link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def fill_all_fields(self):
        languages = ['csharp', 'java', 'javascript', 'python', 'ruby']
        email = self.element_is_visible(self.EMAIL)
        self.go_to_element(email)
        email.send_keys('user@mail.com')
        for x in languages:
            select_language = self.element_is_visible(self.SELECT_LANGUAGE).click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"')).click()
        self.element_is_visible(self.EMAIL).click()
        self.element_is_visible(self.CHECKBOX).click()



