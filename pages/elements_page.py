import base64
from random import randint
import time

import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from generator.generator import person_data_generator
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadLocators, DynamicPropertiesLocators
from pages.base_page import BasePage
from time import sleep


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_text_boxes(self):
        person_info = next(person_data_generator())
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
        full_name = self.element_is_present(self.locators.OUTPUT_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.OUTPUT_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def expand_all_checkboxes(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        checkboxes_list = self.elements_are_visible(self.locators.CHECKBOXES_LIST)
        count = len(checkboxes_list) + 5
        while count > 0:
            checkbox = checkboxes_list[randint(1, len(checkboxes_list))]
            self.go_to_element(checkbox)
            checkbox.click()
            count -= 1

    def get_marked_checkboxes(self):
        marked_boxes_list = self.elements_are_present(self.locators.CHECK_STATUS_BOXES)
        res = []
        for box in marked_boxes_list:
            box_title = box.find_element(By.XPATH, self.locators.CHECKBOX_TITLE)
            res.append(box_title.text)
        # res = [title.find_element(By.XPATH, self.locators.CHECKBOX_TITLE).text for title in marked_boxes_list]
        return str(res).replace('.doc', '').replace(' ', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        res = []
        for item in result_list:
            res.append(item.text)
        # res = [item.text for item in result_list if len(item.text) > 0]
        return str(res).replace(' ', '').replace('F', 'f')


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_radio_button(self, choice):
        options = {
            'yes': self.locators.YES_RADIOBUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
            'no': self.locators.NO_RADIOBUTTON
        }
        self.element_is_visible(options[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        count = 1  # create a few persons
        while count > 0:
            person_info = next(person_data_generator())
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
        data = [item.text.splitlines() for item in persons_lines]
        return data

    def search_box_input(self, key_word):
        self.element_is_visible(self.locators.SEARCH_BOX_INPUT).send_keys(key_word)

    def update_person_info_age(self):
        person_info = next(person_data_generator())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BTN).click()
        self.element_is_visible(self.locators.AGE_FIELD_INPUT).clear()
        self.element_is_visible(self.locators.AGE_FIELD_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BTN_UPDATE).click()
        return str(age)

    def update_person_info_email(self):
        person_info = next(person_data_generator())
        email = person_info.email
        self.element_is_visible(self.locators.UPDATE_BTN).click()
        self.element_is_visible(self.locators.EMAIL_FIELD_INPUT).clear()
        self.element_is_visible(self.locators.EMAIL_FIELD_INPUT).send_keys(email)
        self.element_is_visible(self.locators.SUBMIT_BTN_UPDATE).click()
        return email

    def delete_person_info_btn(self):
        self.element_is_visible(self.locators.DELETE_PERSON_INFO_BTN).click()

    def check_deleted_person_message(self):
        return self.element_is_present(self.locators.NO_ROWS_DATA).text

    def iterate_on_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for num in count:
            position = self.element_is_present(self.locators.ROW_PER_PAGE_BTN)
            self.go_to_element(position)
            position.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{num}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        count_rows_list = self.elements_are_present(self.locators.PERSON_LINE_IN_LIST)
        return len(count_rows_list)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_buttons(self, click_type):
        if click_type == "double_left":
            self.double_click_action(self.element_is_visible(self.locators.DOUBLE_CLICK_BTN))
            return self.check_click_on_different_buttons(self.locators.SUCCESS_DOUBLE)
        if click_type == "right":
            self.right_click_action(self.element_is_visible(self.locators.RIGHT_CLICK_BTN))
            return self.check_click_on_different_buttons(self.locators.SUCCESS_RIGHT)
        if click_type == "click":
            self.element_is_visible(self.locators.ORDINARY_CLICK_BTN).click()
            return self.check_click_on_different_buttons(self.locators.SUCCESS_CLICK_ME)

    def check_click_on_different_buttons(self, element):
        return self.element_is_visible(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_home_link(self):
        home_link = self.element_is_visible(self.locators.HOME_LINK)
        href = home_link.get_attribute('href')
        request = requests.get(href)
        if request.status_code == 200:
            home_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return href, url
        else:
            return href, request.status_code

    def check_bad_request(self, bad_request):
        bad_req_link = self.element_is_present(self.locators.BAD_REQUEST_LINK)
        bad_req_link.click()
        href = bad_req_link.get_attribute('href')
        r = requests.get(bad_request)
        return r.status_code if href == "javascript:void(0)" and r.status_code == 400 else r.status_code


class UploadAndDownload(BasePage):
    locators = UploadAndDownloadLocators()

    def upload_file(self, path):
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        get_result_path = self.element_is_visible(self.locators.UPLOADED_RESULT).text
        return get_result_path.split('\\')[-1]  # get name only

    def download_file(self):
        link = self.element_is_visible(self.locators.DOWNLOAD_FILE).get_attribute('href').split(',')
        print(link)
        link_decoded = base64.b64decode(link[1])
        try:
            response = requests.get(link_decoded, allow_redirects=True)
            with open('test_decoded.jpg', 'wb') as file:
                file.write(response.content)
        except Exception as ex:
            return 'Check url is correct'


class DynamicProperties(BasePage):
    locators = DynamicPropertiesLocators()

    def check_btn_is_enable(self):
        try:
            self.element_is_clickable(self.locators.WILL_ENABLE_BTN)
        except TimeoutError:
            return False
        return True

    def check_color_changed(self):
        get_clr = self.element_is_visible(self.locators.COLOR_CHANGE_BTN)
        clr_before = get_clr.value_of_css_property('color')
        sleep(5)
        clr_after = get_clr.value_of_css_property('color')
        return clr_before, clr_after

    def check_btn_visibility(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_5_SEC_BTN)
        except TimeoutError:
            return False
        return True
