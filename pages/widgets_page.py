from selenium.webdriver.common.by import By

from locators.widgets_page_locators import AccordianPageLocators
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
