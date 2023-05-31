import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NotificationMessagePage(BasePage):
    CLICK_HERE = (By.CSS_SELECTOR, 'p a')
    ALERT = (By.CSS_SELECTOR, 'div#flash')

    def check_notification_message(self):
        self.element_is_visible(self.CLICK_HERE).click()
        time.sleep(3)
        alert_text = self.element_is_visible(self.ALERT).text
        print(alert_text)
        return alert_text


