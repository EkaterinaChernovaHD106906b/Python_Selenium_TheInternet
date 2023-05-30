import random
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FloatingMenuPage(BasePage):
    MENU_LIST = (By.CSS_SELECTOR, 'div#menu ul li')
    HOME = (By.XPATH, '//div[@id="menu"]/ul/li[1]')
    NEWS = (By.XPATH, '//div[@id="menu"]/ul/li[2]')
    CONTACT = (By.XPATH, '//div[@id="menu"]/ul/li[3]')
    ABOUT = (By.XPATH, '//div[@id="menu"]/ul/li[4]')

    def check_floating_menu(self):
        menu_list = self.elements_are_visible(self.MENU_LIST)
        menu_list[random.randint(0, 3)].click()
        time.sleep(3)
        self.scroll_by(800)
        menu_list[random.randint(0, 3)].click()




