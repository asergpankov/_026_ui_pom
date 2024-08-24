from time import sleep
from src.data_provider import person_data_generator

from locators.book_store_application_page_locators import BookStoreApplicationPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = BookStoreApplicationPageLocators()

    def insert_user_creds(self, user_name, password, valid=False):
        # if not len(user_name) > 3:
        #     return 'user_name len too short'
        self.element_is_clickable(self.locators.LOGIN_BTN).click()
        self.element_is_visible(self.locators.USER_NAME_FIELD).send_keys(user_name)
        self.element_is_clickable(self.locators.LOGIN_BTN).click()
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(password)
        self.element_is_clickable(self.locators.LOGIN_BTN).click()

        if valid:
            main_header = self.element_is_visible(self.locators.MAIN_HEADER).text
            login_name = self.element_is_visible(self.locators.LOGIN_NAME).text
            return main_header, login_name
        else:
            message = self.element_is_visible(self.locators.INVALID_USERNAME_PASSWORD).text
            return message

    def add_new_user_data(self):
        person_data = next(person_data_generator())
        first_name = person_data.first_name
        last_name = person_data.last_name
        user_name = person_data.email
        password = person_data.password
        self.element_is_clickable(self.locators.NEW_USER_BTN).click()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
        self.element_is_visible(self.locators.USER_NAME_INPUT).send_keys(user_name)
        self.element_is_visible(self.locators.PASSWORD_INPUT).send_keys(password)
        # self.element_is_visible(self.locators.RECAPTCHA_BOX).click() # TODO need to bypass recaptcha
        print(first_name, last_name, user_name, password)
        sleep(3)
