import base64
import random
import time

import requests
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from generator.generator import generated_person
from locators.practice_form_page_locators import StudentRegistrationFormLocators
from pages.base_page import BasePage
from time import sleep


class StudentRegistrationForm(BasePage):
    locators = StudentRegistrationFormLocators()

    def fill_all_fields(self, f_name, f_path):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        mobile = person_info.mobile
        date_of_birth = person_info.date_of_birth
        # subject = person_info.subject
        current_address = person_info.current_address

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.GENDER_RADIO_BTNS).click()
        self.element_is_visible(self.locators.MOBILE_NMB).send_keys(mobile)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(date_of_birth)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.SUBJECT).send_keys('Math')  # TO DO // insert list of random subjects
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(f_path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        # self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.SELECT_STATE).send_keys("Rajasthan")
        self.element_is_visible(self.locators.SELECT_STATE).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.SELECT_CITY).send_keys("Jaipur")
        self.element_is_visible(self.locators.SELECT_CITY).send_keys(Keys.ENTER)
        submit_btn = self.element_is_present(self.locators.SUBMIT_BTN)
        self.go_to_element(submit_btn)
        submit_btn.click()
        return person_info

# def check_filled_form(self):
#     full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
#     email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
#     current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
#     permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
#     return full_name, email, current_address, permanent_address
