import os.path
import urllib.request

import requests
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class JQueryPage(BasePage):
    ENABLED_HREF = (By.XPATH, '//li[@id="ui-id-3"]/a')
    DOWNLOADS = (By.XPATH, '//li[@id="ui-id-4"]/a')
    PDF = (By.XPATH, '//li[@id="ui-id-5"]/a')
    CSV = (By.XPATH, '//li[@id="ui-id-6"]/a')
    XLS = (By.XPATH, '//li[@id="ui-id-7"]/a')

    def use_jquery(self):
        self.element_is_visible(self.ENABLED_HREF).click()
        self.element_is_visible(self.DOWNLOADS).click()
        link = self.element_is_present(self.CSV).get_attribute('href')
        file_name = 'test.csv'
        path_name_file = rf'C:\Users\user\PycharmProjects\pythonProject2\tests\{file_name}'
        urllib.request.urlretrieve(link, f'{file_name}')
        check_file_exists = os.path.exists(path_name_file)
        if check_file_exists:
            print(f'File {file_name} exists ')
        else:
            print(f'File {file_name} does not exist')
        os.remove(path_name_file)
        return check_file_exists


