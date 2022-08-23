import random
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_all_checkboxes(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        checkboxes_list = self.elements_are_visible(self.locators.CHECKBOXES_LIST)
        count = 21
        while count != 0:
            checkbox = checkboxes_list[random.randint(1, 16)]
            if count > 0:
                self.go_to_element(checkbox)
                checkbox.click()
                # print(checkbox.text)
                count -= 1
            else:
                break

    # def get_marked_checkboxes(self):
    #     marked_checkboxes_list = self.elements_are_present(self.locators.MARKED_CHECKBOXES)
    #     data = []
    #     for box in marked_checkboxes_list:
    #         # checkbox_title = box.find_element_by_xpath(self.locators.CHECKBOX_TITLE)
    #         checkbox_title = box.find_element_by_css_selector(self.locators.LABEL)
    #         data.append(checkbox_title.text)
    #     print(data)


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_radio_button(self, choice):
        choices = {
            'Yes': self.locators.YES_RADIOBUTTON,
            'Impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
            'No': self.locators.NO_RADIOBUTTON
        }
        self.element_is_visible(self, choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        count = 1
        # count = randint(1, 3) # for creating a few person for test_data_input
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_added_person(self):
        persons_lines = self.elements_are_present(self.locators.PERSON_LINE_IN_LIST)
        data = []
        for item in persons_lines:
            data.append(item.text.splitlines())
        return data

    def search_added_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        table_lines = self.element_is_present(self.locators.ROW_LINES_ALL)
        row = table_lines.find_element(self.locators.ROW_LINE_IN)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BTN).click()
        self.element_is_visible(self.locators.AGE_FIELD_INPUT).clear()
        self.element_is_visible(self.locators.AGE_FIELD_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BTN_UPDATE).click()
        sleep(2)
        return age

    def delete_person_info(self):
        person_info = next(generated_person())
        email = person_info.email
        self.element_is_visible(self.locators.DELETE_PERSON_INFO_BTN).click()
        sleep(2)
    def check_deleted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_DATA).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for num in count:
            count_row_button = self.go_to_element(self.element_is_visible.locators.COUNT_ROW_LIST))
            count_row_button.click()
            self.element_is_visible(By.CSS_SELECTOR, f"options[value={num}]").click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        rows_list = self.elements_are_present(self.locators.PERSON_LINE_IN_LIST)
        return len(rows_list)