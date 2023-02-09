from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import choice, sample, randint
from generator.generator import color_generator

from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
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

    def check_colors_in_multi_box(self):
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

    def remove_colors_from_multi_with_main_x(self):
        clrs_before_remove = len(self.elements_are_visible(self.locators.MULTI_OUTPUT))
        print(clrs_before_remove)
        self.element_is_clickable(self.locators.COLOR_REMOVE_MAIN_X_BTN).click()
        clrs_after_remove = len(self.elements_are_visible(self.locators.MULTI_OUTPUT))
        print(clrs_after_remove)