from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
from random import choice, sample, randint
from generator.generator import color_generator, date_and_time_generator

from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators
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
        self.select_option_by_text(self.locators.MONTH_SELECT, date_gen.month)  # select
        self.select_option_by_text(self.locators.YEAR_SELECT, date_gen.year)
        self.set_randon_year_month_day_from_list(self.locators.DAY_SELECT)
        get_date_after = date_in_box.get_attribute('value')
        return get_date_before, get_date_after

    def set_date_and_time_on_calendar(self):
        date_gen = next(date_and_time_generator())
        date_in_box = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        get_date_before = date_in_box.get_attribute('value')
        date_in_box.click()
        self.element_is_visible(self.locators.DT_YEAR_BTN).click()
        self.set_randon_year_month_day_from_list(self.locators.DT_YEAR_LIST)
        self.element_is_visible(self.locators.DT_MONTH_BTN).click()
        self.set_randon_year_month_day_from_list(self.locators.DT_MONTH_LIST)
        self.set_randon_year_month_day_from_list(self.locators.DT_DAY_LIST)
        self.set_number_on_calendar(self.locators.DT_TIME_LIST, date_gen.time)
        get_date_after = date_in_box.get_attribute('value')
        return get_date_before, get_date_after

    def set_number_on_calendar(self, elements, value):
        calendar = self.elements_are_present(elements)
        for num in calendar:
            if num.text == value:
                num.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_position(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_line = self.element_is_visible(self.locators.SLIDER_LINE)
        self.drag_and_drop_by_offset(slider_line, randint(10, 200), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return int(value_before), int(value_after)


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def partial_change_progressbar_position(self):
        value_before = self.element_is_present(self.locators.PR_BAR_VALUE).get_attribute('aria-valuenow')
        start_stop_btn = self.element_is_clickable(self.locators.START_STOP_BTN)
        start_stop_btn.click()
        sleep(randint(2, 7))
        start_stop_btn.click()
        value_after = self.element_is_present(self.locators.PR_BAR_VALUE).get_attribute('aria-valuenow')
        return int(value_before), int(value_after)

    def complete_change_progressbar_position(self):
        value_before = self.element_is_present(self.locators.PR_BAR_VALUE).get_attribute('aria-valuenow')
        start_stop_btn = self.element_is_clickable(self.locators.START_STOP_BTN)
        start_btn_name = start_stop_btn.text
        start_stop_btn.click()
        stop_btn_name = start_stop_btn.text
        self.element_is_present(self.locators.PR_BAR_SUCCESS_VALUE, 15)
        value_after = self.element_is_visible(self.locators.PR_BAR_SUCCESS_VALUE).get_attribute('aria-valuenow')
        reset_btn = self.element_is_clickable(self.locators.RESET_BTN)
        reset_btn_name = reset_btn.text
        reset_btn.click()
        value_after_reset = self.element_is_present(self.locators.PR_BAR_VALUE).get_attribute('aria-valuenow')
        return start_btn_name, stop_btn_name, reset_btn_name, value_before, value_after, value_after_reset
