import os.path
import random

from selenium.webdriver.common.by import By

from generator.generator import generated_file
from pages.base_page import BasePage


class FileDownLoaderPage(BasePage):
    FILE_HREF = (By.XPATH, '//a[text()="some-file.txt"]')
    UPLOAD_PATH = (By.CSS_SELECTOR, 'input#file-upload')

    def download_file(self):
        link = self.element_is_present(self.FILE_HREF).get_attribute('href')
        path_name_file = rf'C:\Users\user\PycharmProjects\pythonProject2\filetest{random.randint(1, 100)}.txt'
        with open(path_name_file, 'w+') as f:
            f.write(link)
            check_file = os.path.exists(path_name_file)
            f.close()
        return check_file

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.UPLOAD_PATH).send_keys(path)
        return file_name





