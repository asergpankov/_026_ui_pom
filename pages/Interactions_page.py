from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
from random import choice, sample, randint
from generator.generator import color_generator, date_and_time_generator, group_option_generator
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from typing import Literal, List
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


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def check_elements_on_page(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        elements_names, elements_on_page = self.get_elements_text(self.locators.LIST_ITEMS)
        return elements_names, elements_on_page

    def clicking_on_random_items(self, tab_name):
        if tab_name == 'list':
            tab = self.locators.LIST_TAB
            items = self.locators.LIST_ITEMS
        elif tab_name == 'grid':
            tab = self.locators.GRID_TAB
            items = self.locators.GRID_ITEMS
        else:
            tab = self.locators.GRID_TAB
            items = self.locators.GRID_ITEMS

        self.element_is_visible(tab).click()
        clicked_items = []
        nonactive_items = self.elements_are_visible(items)
        rand_items = sample(nonactive_items, k=randint(1, len(nonactive_items)))
        for item in rand_items:
            item.click()
            clicked_items.append(item.text)
        print(clicked_items)
        return clicked_items

    def get_active_items(self, tab_name):
        if tab_name == 'list':
            items = self.locators.LIST_ITEMS_ACTIVE
        elif tab_name == 'grid':
            items = self.locators.GRID_ITEMS_ACTIVE
        else:
            items = self.locators.GRID_ITEMS_ACTIVE

        active_items = self.elements_are_visible(items)
        active_items_list = [item.text for item in active_items]
        print(active_items_list)
        return active_items_list

    def choose_and_cancellation_all_items(self, tab_name):
        if tab_name == 'list':
            tab = self.locators.LIST_TAB
            items = self.locators.LIST_ITEMS
            active_items = self.locators.LIST_ITEMS_ACTIVE
        elif tab_name == 'grid':
            tab = self.locators.GRID_TAB
            items = self.locators.GRID_ITEMS
            active_items = self.locators.GRID_ITEMS_ACTIVE
        else:
            tab = self.locators.GRID_TAB
            items = self.locators.GRID_ITEMS
            active_items = self.locators.GRID_ITEMS_ACTIVE

        self.element_is_visible(tab).click()
        nonactive_items = self.elements_are_visible(items)
        [item.click()for item in nonactive_items]
        active_items = self.elements_are_visible(active_items)
        [item.click()for item in active_items]
        nonactive_items_after = self.elements_are_visible(items)
        [item.click()for item in nonactive_items_after]
        return len(nonactive_items), len(active_items), len(nonactive_items_after)