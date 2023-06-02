import random
import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AlertPage(BasePage):
    BUTTON_JS_ALERT = (By.CSS_SELECTOR, 'button[onclick="jsAlert()"')
    BUTTON_JS_CONFIRM = (By.CSS_SELECTOR, 'button[onclick="jsConfirm()"')
    BUTTON_JS_PROMPT = (By.CSS_SELECTOR, 'button[onclick="jsPrompt()"')
    ALERT_RESULT = (By.CSS_SELECTOR, 'p#result')

    def work_with_alerts(self):
        self.element_is_visible(self.BUTTON_JS_ALERT).click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        alert_result = self.element_is_visible(self.ALERT_RESULT).text
        print(alert_result)
        self.element_is_visible(self.BUTTON_JS_CONFIRM).click()
        time.sleep(2)
        alert_confirm = self.driver.switch_to.alert
        alert_confirm.accept()
        alert_confirm_result = self.element_is_visible(self.ALERT_RESULT).text
        print(alert_confirm_result)
        self.element_is_visible(self.BUTTON_JS_PROMPT).click()
        time.sleep(3)
        alert_prompt = self.driver.switch_to.alert
        prompt = f'User {random.randint(0, 100)}'
        alert_prompt.send_keys(prompt)
        alert_prompt.accept()
        alert_prompt_result = self.element_is_visible(self.ALERT_RESULT).text
        print(alert_prompt_result)
        return alert_result, alert_confirm_result, alert_prompt_result





