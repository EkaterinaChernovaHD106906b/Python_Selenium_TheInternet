import random
import time

from pages.ab_page import ABPage
from pages.add_remove_page import AddRemoveElements
from pages.base_page import BasePage
from pages.basic_auth_page import BasicAuthorizationPage
from pages.checkboxes_page import CheckboxesPage
from pages.context_menu_page import ContextMenuPage
from pages.disappearing_elements_page import DisappearingElementsPage
from pages.drag_drop_page import DragDropPage
from pages.dropdown_page import DropDownPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.file_downloader_page import FileDownLoaderPage
from pages.floating_menu_page import FloatingMenuPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.iframe import IFramePage
from pages.login_page import LoginPage
from pages.modal_window_page import ModalWindowPage
from pages.notification_message_page import NotificationMessagePage


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

        def test_drag_drop(self, driver):
            drag_drop_page = DragDropPage(driver, 'https://the-internet.herokuapp.com/drag_and_drop')
            drag_drop_page.open()
            drag_drop_page.check_ab_haaders()
            time.sleep(5)

        def test_dropdown_list(self, driver):
            dropdown_page = DropDownPage(driver, 'https://the-internet.herokuapp.com/dropdown')
            dropdown_page.open()
            dropdown_page.check_options()
            time.sleep(5)

        def test_loading_page(self, driver):
            loading_page = DynamicLoadingPage(driver, 'https://the-internet.herokuapp.com/dynamic_loading')
            loading_page.open()
            text = loading_page.check_first_href('second')
            assert text == 'Hello World!'

        def test_modal_window(self, driver):
            modal_window_page = ModalWindowPage(driver, 'https://the-internet.herokuapp.com/entry_ad')
            modal_window_page.open()
            text_modal_window = modal_window_page.close_modal_window()
            time.sleep(5)
            assert text_modal_window == "It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something or disable their ad blocker)."

        def test_file_downloader(self, driver):
            file_downloader_page = FileDownLoaderPage(driver, 'https://the-internet.herokuapp.com/download')
            file_downloader_page.open()
            file_downloader_page.download_file()

        def test_upload_file(self, driver):
            upload_file_page = FileDownLoaderPage(driver, 'https://the-internet.herokuapp.com/upload')
            upload_file_page.open()
            upload_file_page.upload_file()
            time.sleep(5)

        def test_floating_menu(self, driver):
            floating_menu = FloatingMenuPage(driver, 'https://the-internet.herokuapp.com/floating_menu')
            floating_menu.open()
            floating_menu.check_floating_menu()
            time.sleep(5)

        def test_forgot_password(self, driver):
            forgot_password_page = ForgotPasswordPage(driver, 'https://the-internet.herokuapp.com/forgot_password')
            forgot_password_page.open()
            result = forgot_password_page.retrieve_password()
            time.sleep(5)
            assert result == 'Internal Server Error'

        def test_login_success(self, driver):
            login_page = LoginPage(driver, 'https://the-internet.herokuapp.com/login')
            login_page.open()
            result = login_page.login_success()
            time.sleep(5)
            assert result.replace('×', '').replace('\n', '') == 'You logged into a secure area!'

        def test_login_unsuccessful(self, driver):
            login_page = LoginPage(driver, 'https://the-internet.herokuapp.com/login')
            login_page.open()
            result = login_page.login_unsuccessful()
            time.sleep(5)
            assert result.replace('×', '').replace('\n', '') == 'Your username is invalid!'

        def test_iframe(self, driver):
            iframe_page = IFramePage(driver, 'https://the-internet.herokuapp.com/iframe')
            iframe_page.open()
            text = f'My text {random.randint(0, 100)}'
            my_text = iframe_page.input_text(f'{text}')
            time.sleep(5)
            assert my_text == text

        def test_notification_message(self, driver):
            notification_message_page = NotificationMessagePage(driver, 'https://the-internet.herokuapp.com/notification_message_rendered')
            notification_message_page.open()
            notification_message_page.check_notification_message()
            time.sleep(5)

