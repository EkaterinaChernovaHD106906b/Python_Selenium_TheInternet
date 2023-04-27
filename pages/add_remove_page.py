from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddRemoveElements(BasePage):

    BUTTON_ADD_ELEMENT = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    BUTTON_DELETE_ELEMENT = (By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')

    def add_element(self):
        button_add = self.element_is_visible(self.BUTTON_ADD_ELEMENT).click()

    def check_element_was_added(self):
        button_delete = self.element_is_visible(self.BUTTON_DELETE_ELEMENT)

    def delete_element(self):
        button_delete = self.element_is_visible(self.BUTTON_DELETE_ELEMENT).click()

    def check_element_was_deleted(self):
        button_delete = self.element_is_not_visible(self.BUTTON_DELETE_ELEMENT)
