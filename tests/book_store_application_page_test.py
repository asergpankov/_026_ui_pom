import pytest

from pages.book_store_application_page import LoginPage
from pages.elements_page import TextBoxPage
from src.global_enums.global_enums import LoginPageEnums
import os
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")


class TestBookStoreApplicationPage:
    @pytest.mark.login
    class TestLoginPage:
        def test_valid_user_creds(self, driver):
            login_page = LoginPage(driver, "https://demoqa.com/login")
            login_page.open_browser()
            main_header, login_name = login_page.insert_user_creds(USER_NAME, PASSWORD, 'valid')
            assert main_header == 'Profile', 'Creds are not correct'
            assert login_name == USER_NAME, 'Diff btw login_name and user_name'

        @pytest.mark.parametrize('auth', LoginPageEnums.CREDS.value)
        def test_invalid_user_creds(self, driver, auth):
            login_page = LoginPage(driver, "https://demoqa.com/login")
            login_page.open_browser()
            message = login_page.insert_user_creds(*auth)
            assert message == 'Invalid username or password!', 'Need to input correct user creds'

        @pytest.mark.skip(reason='need to bypass recaptcha')
        def test_add_new_user_data(self, driver):
            login_page = LoginPage(driver, "https://demoqa.com/login")
            login_page.open_browser()
            login_page.add_new_user_data()
            movie_page = TextBoxPage(login_page.driver, login_page.driver.current_url)
            full_name = movie_page.check_filled_form()
