import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HoversPage(BasePage):
    LIST_OF_IMGS = (By.CSS_SELECTOR, 'div.figure img')
    IMG1 = (By.XPATH, '//div[@class="figure"][1]/img')
    IMG2 = (By.XPATH, '//div[@class="figure"][2]/img')
    IMG3 = (By.XPATH, '//div[@class="figure"][3]/img')
    USER_INF01 = (By.XPATH, '//div[@class="figure"][1]/div[@class="figcaption"][1]/h5')
    USER_HREF1 = (By.XPATH, '//div[@class="figure"][1]/div[@class="figcaption"][1]/a')
    USER_INF02 = (By.XPATH, '//div[@class="figure"][2]/div[@class="figcaption"][1]/h5')
    USER_HREF2 = (By.XPATH, '//div[@class="figure"][2]/div[@class="figcaption"][1]/a')
    USER_INF03 = (By.XPATH, '//div[@class="figure"][3]/div[@class="figcaption"][1]/h5')
    USER_HREF3 = (By.XPATH, '//div[@class="figure"][3]/div[@class="figcaption"][1]/a')

    def get_user_info(self, user):
        # list_img = self.elements_are_present(self.LIST_OF_IMGS)
        # list_img[random.randint(0, 2)].click()
        if user == 'user1':
            self.element_is_visible(self.IMG1).click()
            user_info1 = self.element_is_visible(self.USER_INF01).text
            print(user_info1)
            return user_info1
        if user == 'user2':
            self.element_is_visible(self.IMG2).click()
            user_info2 = self.element_is_visible(self.USER_INF02).text
            print(user_info2)
            return user_info2
        if user == 'user3':
            self.element_is_visible(self.IMG3).click()
            user_info3 = self.element_is_visible(self.USER_INF03).text
            return user_info3


