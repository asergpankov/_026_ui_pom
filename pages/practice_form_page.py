import base64
import os
from random import randint, choice
import time

import requests
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from generator.generator import generate_person_data
from locators.practice_form_page_locators import StudentRegistrationFormLocators
from pages.base_page import BasePage
from time import sleep


class StudentRegistrationForm(BasePage):
    locators = StudentRegistrationFormLocators()

    def fill_all_fields(self, f_name, f_path, state):
        person_data = next(generate_person_data())
        first_name = person_data.first_name
        last_name = person_data.last_name
        email = person_data.email
        mobile = person_data.mobile
        date_of_birth = person_data.date_of_birth
        # subject = person_data.subject
        current_address = person_data.current_address
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.GENDER_RADIO_BTNS).click()
        self.element_is_visible(self.locators.MOBILE_NMB).send_keys(mobile)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(date_of_birth)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.RETURN)

        # SUBJECTS INPUT
        subjects_list = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
                         "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics", ]
        subj_count = randint(1, len(subjects_list))
        subj_used = []
        while subj_count > 0:
            subject = choice(subjects_list)
            if subject not in subj_used:
                self.element_is_visible(self.locators.SUBJECT).send_keys(subject)  # TO DO // take subjects from source/bundle.js
                sleep(0.7)
                self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.ENTER)
                subj_count -= 1
                subj_used.append(subject)
            else:
                subj_count -= 0
        # bug when attempt to delete single subject in line with 'x' or backspace

        # HOBBIES INPUT
        box_count = 5
        while box_count > 0:
            box = self.element_is_visible((By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{randint(1, 3)}"]'))
            sleep(0.3)
            box.click()
            box_count -= 1

        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(f_path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)

        # STATES and CITIES INPUT
        self.element_is_visible(self.locators.SELECT_STATE_INP).send_keys(state) # TO DO // def for mixing states and cities
        self.element_is_visible(self.locators.SELECT_STATE_INP).send_keys(Keys.ENTER)
        if state == "NCR":
            nrc_cities = ["Delhi", "Gurgaon", "Noida"]
            self.element_is_visible(self.locators.SELECT_CITY_INP).send_keys(f"{choice(nrc_cities)}")
        if state == "Uttar Pradesh":
            uttar_pradesh_cities = ["Agra", "Lucknow", "Merrut"]
            self.element_is_visible(self.locators.SELECT_CITY_INP).send_keys(f"{choice(uttar_pradesh_cities)}")
        if state == "Haryana":
            haryana_cities = ["Karnal", "Panipat"]
            self.element_is_visible(self.locators.SELECT_CITY_INP).send_keys(f"{choice(haryana_cities)}")

        self.element_is_visible(self.locators.SELECT_CITY_INP).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.SUBMIT_BTN).click()
        return person_data

    def check_data_from_table_values(self):
        res_values = self.elements_are_present(self.locators.RESULT_TABLE_VALUES)
        data = [item.text for item in res_values]
        return data
