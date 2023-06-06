import random
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShiftingContentPage(BasePage):
    # Shifting content

    MENU_ELEMENT = (By.XPATH, '//div[@class="example"]//a[1]')
    AN_IMAGE = (By.XPATH, '//div[@class="example"]//a[2]')
    LIST = (By.XPATH, '//div[@class="example"]//a[3]')

    # Menu element

    FIRST_LINK = (By.XPATH, '//div[@class="example"]//p[2]//a')
    SECOND_LINK = (By.XPATH, '//div[@class="example"]//p[3]//a')
    THIRD_LINK = (By.XPATH, '//div[@class="example"]//p[4]//a')
    GALLERY = (By.XPATH, '//div[@class="example"]//ul//li[5]/a')

    # Image

    FIRST_LINK_IMG = (By.XPATH, '//div[@class="example"]//p[2]//a')
    SECOND_LINK_IMG = (By.XPATH, '//div[@class="example"]//p[3]//a')
    THIRD_LINK_IMG = (By.XPATH, '//div[@class="example"]//p[4]//a')
    FOURTH_LINK_IMG = (By.XPATH, '//div[@class="example"]//p[5]//a')
    IMAGE = (By.CSS_SELECTOR, 'img.shift')

    # List

    TEXT = (By.XPATH, '//div[@id="content"]//div[@class="large-6 columns large-centered"]')

    def use_shifting_content_menu(self):
        self.element_is_visible(self.MENU_ELEMENT).click()
        first_link = self.element_is_present(self.FIRST_LINK)
        second_link = self.element_is_present(self.SECOND_LINK)
        third_link = self.element_is_present(self.THIRD_LINK)
        links = [first_link, second_link, third_link]
        gallery_before = self.element_is_present(self.GALLERY)
        position_before = gallery_before.value_of_css_property('left')
        links[random.randint(0, 2)].click()
        gallery_after = self.element_is_present(self.GALLERY)
        position_after = gallery_after.value_of_css_property('left')
        return position_before, position_after

    def use_shifting_content_image_position(self):
        self.element_is_visible(self.AN_IMAGE).click()
        image_before = self.element_is_present(self.IMAGE)
        position_before = image_before.value_of_css_property('left')
        first_link = self.element_is_present(self.FIRST_LINK_IMG)
        second_link = self.element_is_present(self.SECOND_LINK_IMG)
        third_link = self.element_is_present(self.THIRD_LINK_IMG)
        links = [first_link, second_link, third_link]
        links[random.randint(0, 2)].click()
        image_after = self.element_is_present(self.IMAGE)
        position_after = image_after.value_of_css_property('left')
        return position_before, position_after

    def use_shifting_content_image_link(self):
        self.element_is_visible(self.AN_IMAGE).click()
        image_before = self.element_is_present(self.IMAGE)
        src_before = image_before.get_attribute('src')
        self.element_is_present(self.FOURTH_LINK_IMG).click()
        image_after = self.element_is_present(self.IMAGE)
        src_after = image_after.get_attribute('src')
        return src_before, src_after

    def use_shifting_content_list(self):
        text_before = self.element_is_present(self.TEXT).text
        self.driver.refresh()
        text_after = self.element_is_present(self.TEXT).text
        return text_before, text_after





