import requests
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class StatusCodePage(BasePage):
    CODE200 = (By.XPATH, '//div[@class="example"]//ul/li[1]')
    CODE301 = (By.XPATH, '//div[@class="example"]//ul/li[2]')
    CODE404 = (By.XPATH, '//div[@class="example"]//ul/li[3]')
    CODE500 = (By.XPATH, '//div[@class="example"]//ul/li[4]')
    CODE200HREF = (By.XPATH, '//div[@class="example"]//ul/li[1]/a')
    CODE301HREF = (By.XPATH, '//div[@class="example"]//ul/li[2]/a')
    CODE404HREF = (By.XPATH, '//div[@class="example"]//ul/li[3]/a')
    CODE500HREF = (By.XPATH, '//div[@class="example"]//ul/li[4]/a')

    def get_status_code(self, link):
        links = {'200': self.CODE200,
                 '301': self.CODE301,
                 '404': self.CODE404,
                 '500': self.CODE500}
        self.element_is_visible(links[link]).click()
        if link == '200':
            link200 = self.element_is_present(self.CODE200HREF).get_attribute('href')
            request = requests.get(link200)
            status = request.status_code
            status_code = str(status)
            return status_code
        if link == '301':
            link301 = self.element_is_present(self.CODE301HREF).get_attribute('href')
            request = requests.get(link301)
            status = request.status_code
            status_code = str(status)
            return status_code
        if link == '404':
            link404 = self.element_is_present(self.CODE404HREF).get_attribute('href')
            request = requests.get(link404)
            status = request.status_code
            status_code = str(status)
            return status_code
        else:
            link500 = self.element_is_present(self.CODE500HREF).get_attribute('href')
            request = requests.get(link500)
            status = request.status_code
            status_code = str(status)
            return status_code
