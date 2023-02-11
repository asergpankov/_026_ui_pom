from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
from random import choice, sample, randint
from generator.generator import color_generator, date_and_time_generator

from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian_structure(self, accordian_num):
        self.element_is_visible(self.locators.FIRST_HEADER).click()
        accordian = {
            'first': {
                'title': self.locators.FIRST_HEADER,
                'content': self.locators.FIRST_CONTENT
            },
            'second': {
                'title': self.locators.SECOND_HEADER,
                'content': self.locators.SECOND_CONTENT
            },
            'third': {
                'title': self.locators.THIRD_HEADER,
                'content': self.locators.THIRD_CONTENT
            },
        }
        self.element_is_visible(accordian[accordian_num]['title']).click()
        title = self.element_is_visible(accordian[accordian_num]['title']).text
        content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [title, len(content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_colors_multiply_input(self):
        colors_list = next(color_generator()).colors_list
        colors = sample(colors_list, k=randint(2, len(colors_list)))
        for color in colors:
            multy_input = self.element_is_clickable(self.locators.MULTI_INPUT)
            multy_input.send_keys(color)
            multy_input.send_keys(Keys.ENTER)
        colors_in = [color.capitalize() for color in colors]
        return colors_in

    def check_colors_multiply_input(self):
        colors_in_box = self.elements_are_visible(self.locators.MULTI_OUTPUT)
        colors_res = []
        for color in colors_in_box:
            colors_res.append(color.text)
        return colors_res

    def remove_color_from_multiply_with_x(self):
        num_of_colors_before_remove = len(self.elements_are_visible(self.locators.MULTI_OUTPUT))
        remove_btn = self.elements_are_visible(self.locators.COLOR_REMOVE_X_BTN)
        for x in remove_btn:
            x.click()
            break
        num_of_colors_after_remove = len(self.elements_are_visible(self.locators.MULTI_OUTPUT))
        return num_of_colors_before_remove, num_of_colors_after_remove

    def remove_color_from_multiply_with_backspace(self):
        clrs_before_remove = len(self.elements_are_visible(self.locators.MULTI_OUTPUT))
        remove_x_btn = self.elements_are_visible(self.locators.COLOR_REMOVE_X_BTN)
        count = len(remove_x_btn)
        while count > 1:
            self.element_is_visible(self.locators.MULTI_INPUT).click()
            self.element_is_visible(self.locators.MULTI_INPUT).send_keys(Keys.BACKSPACE)
            count -= 1
        clrs_after_remove = len(self.elements_are_visible(self.locators.MULTI_OUTPUT))
        return clrs_before_remove, clrs_after_remove

    def remove_all_colors_from_multi_with_main_x(self):
        clrs_before_remove = len(self.elements_are_visible(self.locators.MULTI_OUTPUT))
        self.element_is_clickable(self.locators.COLOR_REMOVE_MAIN_X_BTN).click()
        try:
            clrs_after_remove = self.element_is_visible(self.locators.MULTI_OUTPUT, 2)
        except TimeoutException:
            clrs_after_remove = 0
        return clrs_before_remove, clrs_after_remove

    def fill_color_single_input(self):
        color = choice(next(color_generator()).colors_list)
        single_input = self.element_is_visible(self.locators.SINGLE_INPUT)
        single_input.send_keys(color)
        single_input.send_keys(Keys.ENTER)
        return color.capitalize()

    def check_color_single_input(self):
        color_in_box = self.element_is_visible(self.locators.SINGLE_OUTPUT).text
        return color_in_box


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def set_date_on_calendar(self):
        date_gen = next(date_and_time_generator())
        date_in_box = self.element_is_visible(self.locators.SELECT_DATE_INPUT)
        date_in_box.click()
        get_date_before = date_in_box.get_attribute('value')
        self.select_option_by_text(self.locators.MONTH_SELECT, date_gen.month)
        self.select_option_by_text(self.locators.YEAR_SELECT, date_gen.year)
        self.set_number_on_calendar(self.locators.DAY_SELECT, '10')  # TODO // check wrong day setup with date lt 10
        sleep(3)
        get_date_after = date_in_box.get_attribute('value')
        sleep(3)
        # print(get_date_before, get_date_after)

        return get_date_before, get_date_after

    def set_date_and_time_on_calendar(self):
        date_gen = next(date_and_time_generator())
        date_in_box = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        get_date_before = date_in_box.get_attribute('value')
        date_in_box.click()
        self.element_is_visible(self.locators.DT_YEAR_BTN).click()
        self.set_number_on_calendar(self.locators.DT_YEAR_LIST, '2019')  # TODO / need to setup a random year
        self.element_is_visible(self.locators.DT_MONTH_BTN).click()
        self.set_number_on_calendar(self.locators.DT_MONTH_LIST, date_gen.month)
        self.set_number_on_calendar(self.locators.DT_DAY, date_gen.day)
        self.set_number_on_calendar(self.locators.DT_TIME_LIST, date_gen.time)
        get_date_after = date_in_box.get_attribute('value')
        print(date_gen)
        print(get_date_before, get_date_after)
        return get_date_before, get_date_after

    def set_number_on_calendar(self, elements, value):
        calendar = self.elements_are_present(elements)
        for num in calendar:
            if num.text == value:
                num.click()
                break
