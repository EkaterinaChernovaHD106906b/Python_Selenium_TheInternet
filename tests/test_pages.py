import time

from pages.ab_page import ABPage
from pages.add_remove_page import AddRemoveElements
from pages.base_page import BasePage
from pages.basic_auth_page import BasicAuthorizationPage
from pages.checkboxes_page import CheckboxesPage
from pages.context_menu_page import ContextMenuPage
from pages.disappearing_elements_page import DisappearingElementsPage


class TestPages:
    class TestABPage:

        def test_ab_page(self, driver):
            web_ab_page = ABPage(driver, 'https://the-internet.herokuapp.com/abtest')
            web_ab_page.open()
            web_ab_page.click_on_link()
            web_ab_page.fill_all_fields()
            time.sleep(5)

    class TestAddRemovePage:

        def test_add_remove_page(self, driver):
            add_remove_page = AddRemoveElements(driver, 'https://the-internet.herokuapp.com/add_remove_elements/')
            add_remove_page.open()
            add_remove_page.add_element()
            add_remove_page.check_element_was_added()
            add_remove_page.delete_element()
            add_remove_page.check_element_was_deleted()

    class TestBasicAuthPage:

        def test_basic_auth_page(self, driver):
            base_auth_page = BasicAuthorizationPage(driver, 'https://admin:admin@the-internet.herokuapp.com/basic_auth')
            base_auth_page.open()
            check = base_auth_page.check_basic_auto()
            success_auth = 'Congratulations! You must have the proper credentials.'
            assert check == success_auth, 'Authentication failed'

    class TestCheckboxesPage:

        def test_click_checkbox(self, driver):
            checkboxes_page = CheckboxesPage(driver, 'https://the-internet.herokuapp.com/checkboxes')
            checkboxes_page.open()
            checkboxes_page.click_checkbox()

    class TestContextMenuPage:

        def test_context_menu_page(self, driver):
            context_menu_page = ContextMenuPage(driver, 'https://the-internet.herokuapp.com/context_menu')
            context_menu_page.open()
            alert_text = context_menu_page.click_on_context_menu()
            assert alert_text == 'You selected a context menu'

        def test_disappearing_elements(self, driver):
            dis_elements_page = DisappearingElementsPage(driver, 'https://the-internet.herokuapp.com'
                                                                 '/disappearing_elements')
            dis_elements_page.open()
            dis_elements_page.click_different_button('gallery')
            time.sleep(5)

