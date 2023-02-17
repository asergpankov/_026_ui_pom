from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
from random import choice, sample, randint
from generator.generator import color_generator, date_and_time_generator, group_option_generator
from locators.interactions_page_locators import SortablePageLocators
from typing import Literal
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    TAB_NAME = Literal["list", "grid"]

    def get_sortable_elements(self, elements):
        elements = self.elements_are_visible(elements)
        return [element.text for element in elements]

    def change_item_order_position(self, tab_name: TAB_NAME):
        if tab_name == "list":
            tab = self.locators.TAB_LIST
            items = self.locators.LIST_ITEMS
        else:
            tab = self.locators.TAB_GRID
            items = self.locators.GRID_ITEMS

        self.element_is_visible(tab).click()
        items_order_before = self.get_sortable_elements(items)
        random_items = sample(self.elements_are_visible(items), k=2)
        source_item = random_items[0]
        target_item = random_items[1]
        self.drag_and_drop_to_element(source_item, target_item)
        items_order_after = self.get_sortable_elements(items)
        return items_order_before, items_order_after
