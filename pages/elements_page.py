import base64
from random import randint
import time

import allure
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from data.data import UserData as ud
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadLocators, DynamicPropertiesLocators
from pages.base_page import BasePage
from time import sleep


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step('fill all text boxes _step')
    def fill_all_text_boxes(self):
        data = ud.generate_data()
        full_name = data.full_name
        email = data.email
        current_address = data.current_address
        permanent_address = data.permanent_address

        with allure.step('generate data _step'):
            self.set_value(self.locators.FULL_NAME, full_name)
            self.set_value(self.locators.EMAIL, email)
            self.set_value(self.locators.CURRENT_ADDRESS, current_address)
            self.set_value(self.locators.PERMANENT_ADDRESS, permanent_address)
        with allure.step('click on submit button _step'):
            self.left_click_on_element(self.locators.SUBMIT)
        return full_name, email, current_address, permanent_address

    @allure.step('filled form check _step')
    def check_filled_form(self):
        full_name = self.get_element_text(self.locators.OUTPUT_FULL_NAME).split(":")[1]
        email = self.get_element_text(self.locators.OUTPUT_EMAIL).split(":")[1]
        current_address = self.get_element_text(self.locators.OUTPUT_CURRENT_ADDRESS).split(":")[1]
        permanent_address = self.get_element_text(self.locators.OUTPUT_PERMANENT_ADDRESS).split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step('expand all boxes _step')
    def expand_all_checkboxes(self):
        self.left_click_on_element(self.locators.EXPAND_ALL_BUTTON)

    @allure.step('click random boxes _step')
    def click_random_checkboxes(self):
        checkboxes_list = self.elements_are_visible(self.locators.CHECKBOXES_LIST)
        count = len(checkboxes_list) + randint(2, 6)
        while count > 0:
            checkbox = checkboxes_list[randint(1, len(checkboxes_list))]
            self.go_to_element(checkbox)
            checkbox.click()
            count -= 1

    @allure.step('get marked box _step')
    def get_marked_checkboxes(self):
        marked_boxes_list = self.elements_are_present(self.locators.CHECK_STATUS_BOXES)
        res = []
        for box in marked_boxes_list:
            box_title = box.find_element(By.XPATH, self.locators.CHECKBOX_TITLE)
            res.append(box_title.text)
        return str(res).replace('.doc', '').replace(' ', '').lower()

    @allure.step('get output result _step')
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        res = []
        for item in result_list:
            res.append(item.text)
        return str(res).replace(' ', '').replace('F', 'f')


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('radio button click _step')
    def click_radio_button(self, choice):
        options = {
            'yes': self.locators.YES_RADIOBUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
            'no': self.locators.NO_RADIOBUTTON
        }
        self.left_click_on_element(options[choice])

    @allure.step('get output result _step')
    def get_output_result(self):
        return self.get_element_text(self.locators.OUTPUT_RESULT)


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step('add new person _step')
    def add_new_person(self):
        count = 1  # create a few persons
        while count > 0:
            data = ud.generate_data()
            with allure.step('generate data'):
                self.left_click_on_element(self.locators.ADD_BUTTON)
                self.set_value(self.locators.FIRSTNAME_INPUT, data.first_name)
                self.set_value(self.locators.LASTNAME_INPUT,data.last_name)
                self.set_value(self.locators.EMAIL_INPUT, data.email)
                self.set_value(self.locators.AGE_INPUT, data.age)
                self.set_value(self.locators.SALARY_INPUT, data.salary)
                self.set_value(self.locators.DEPARTMENT_INPUT, data.department)
            with allure.step('submit button click'):
                self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [data.first_name, data.last_name, str(data.age), data.email, str(data.salary), data.department]

    @allure.step('added person check _step')
    def check_added_person(self):
        persons_lines = self.get_elements_text(self.locators.PERSON_LINE_IN_LIST)
        data = [item.splitlines() for item in persons_lines]
        return data

    @allure.step('search box input _step')
    def search_box_input(self, key_word):
        self.set_value(self.locators.SEARCH_BOX_INPUT, key_word)

    @allure.step('update person info age _step')
    def update_person_info_age(self):
        data = ud.generate_data()
        with allure.step('send keys and click update'):
            self.left_click_on_element(self.locators.UPDATE_BTN)
            self.set_value(self.locators.AGE_FIELD_INPUT, data.age)
            self.left_click_on_element(self.locators.SUBMIT_BTN_UPDATE)
        return str(data.age)

    @allure.step('update person info email _step')
    def update_person_info_email(self):
        data =ud.generate_data()
        with allure.step('send keys and click update'):
            self.left_click_on_element(self.locators.UPDATE_BTN)
            self.set_value(self.locators.EMAIL_FIELD_INPUT, data.email)
            self.left_click_on_element(self.locators.SUBMIT_BTN_UPDATE)
        return data.email

    @allure.step('delete person info _step')
    def delete_person_info_btn(self):
        self.left_click_on_element(self.locators.DELETE_PERSON_INFO_BTN)

    @allure.step('delete info message _step')
    def check_deleted_person_message(self):
        return self.get_element_text(self.locators.NO_ROWS_DATA)

    @allure.step('iterate on rows _step')
    def iterate_on_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for num in count:
            position = self.element_is_present(self.locators.ROW_PER_PAGE_BTN)
            self.go_to_element(position)
            position.click()
            self.left_click_on_element((By.CSS_SELECTOR, f'option[value="{num}"]'))
            data.append(self.check_count_rows())
        return data

    @allure.step('count rows _step')
    def check_count_rows(self):
        count_rows_list = self.elements_are_present(self.locators.PERSON_LINE_IN_LIST)
        return len(count_rows_list)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step('click on different buttons _step')
    def click_on_different_buttons(self, click_type):
        if click_type == "double_left":
            self.double_click_action(self.element_is_visible(self.locators.DOUBLE_CLICK_BTN))
            return self.check_click_on_different_buttons(self.locators.SUCCESS_DOUBLE)
        if click_type == "right":
            self.right_click_action(self.element_is_visible(self.locators.RIGHT_CLICK_BTN))
            return self.check_click_on_different_buttons(self.locators.SUCCESS_RIGHT)
        if click_type == "click":
            self.left_click_on_element(self.locators.ORDINARY_CLICK_BTN)
            return self.check_click_on_different_buttons(self.locators.SUCCESS_CLICK_ME)

    def check_click_on_different_buttons(self, element):
        return self.get_element_text(element)


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step('new tab home link check _step')
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
        return r.status_code if href == "javascript:void(0)" and r.status_code == 400 \
            else r.status_code


class UploadAndDownload(BasePage):
    locators = UploadAndDownloadLocators()

    def upload_file(self, path):
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        get_result_path = self.get_element_text(self.locators.UPLOADED_RESULT)
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
