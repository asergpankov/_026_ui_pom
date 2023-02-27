from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
from random import choice, sample, randint
from generator.generator import color_generator, date_and_time_generator, group_option_generator
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
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

    def check_elements_on_page(self, tab_name):
        tabs = {
            'list': {
                'tab': self.locators.LIST_TAB,
                'items': self.locators.LIST_ITEMS
            },
            'grid': {
                'tab': self.locators.GRID_TAB,
                'items': self.locators.GRID_ITEMS
            }
        }
        self.element_is_visible(tabs[tab_name]['tab']).click()
        elements_names, elements_on_page = self.get_elements_text(tabs[tab_name]['items'])
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
        [item.click() for item in nonactive_items]
        active_items = self.elements_are_visible(active_items)
        [item.click() for item in active_items]
        nonactive_items_after = self.elements_are_visible(items)
        [item.click() for item in nonactive_items_after]
        return len(nonactive_items), len(active_items), len(nonactive_items_after)


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def change_resizable_box_size(self, width, height):
        box_handle = self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE)
        self.drag_and_drop_by_offset(box_handle, width, height)
        element = self.element_is_visible(self.locators.RESIZABLE_BOX)
        get_position = element.get_attribute('style')
        return get_position

    def change_resizable_size(self, width, height):
        box_handle = self.element_is_present(self.locators.RESIZABLE_HANDLE)
        self.drag_and_drop_by_offset(box_handle, width, height)
        element = self.element_is_present(self.locators.RESIZABLE)
        get_position = element.get_attribute('style')
        return get_position


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_in_or_through_area(self, method, drag_elem, drop_elem):
        text_before = drop_elem.text
        color_before = drop_elem.value_of_css_property("background-color")
        if method == 'through':
            self.drag_and_drop_by_offset(drag_elem, 500, randint(-30, 30))
        else:
            self.drag_and_drop_to_element(drag_elem, drop_elem)
        text_after = drop_elem.text
        color_after = drop_elem.value_of_css_property("background-color")
        return text_before, text_after, color_before, color_after

    # TODO need an unification of drop funks
    def simple_drop(self, method):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_elem = self.element_is_visible(self.locators.SIMPLE_DRAGGABLE)
        drop_elem = self.element_is_visible(self.locators.SIMPLE_DROPPABLE)
        text_before, text_after, color_before, color_after = self.drop_in_or_through_area(method, drag_elem, drop_elem)
        self.drag_and_drop_by_offset(drag_elem, randint(-300, 300), randint(-200, 200))
        return text_before, text_after, color_before, color_after

    def not_accept_drop(self, method):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_elem = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_elem = self.element_is_visible(self.locators.ACCEPT_DROPPABLE)
        text_before, text_after, color_before, color_after = self.drop_in_or_through_area(method, drag_elem, drop_elem)
        self.drag_and_drop_by_offset(drag_elem, randint(-300, 300), randint(-200, 200))
        return text_before, text_after, color_before, color_after

    def accept_drop(self, method):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_elem = self.element_is_visible(self.locators.ACCEPTABLE)
        drop_elem = self.element_is_visible(self.locators.ACCEPT_DROPPABLE)
        text_before, text_after, color_before, color_after = self.drop_in_or_through_area(method, drag_elem, drop_elem)
        self.drag_and_drop_by_offset(drag_elem, randint(-300, 300), randint(-200, 200))
        return text_before, text_after, color_before, color_after

    def inner_not_greedy_drop_in_area(self, method):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_elem = self.element_is_visible(self.locators.DRAG_ME)
        drop_elem = self.element_is_visible(self.locators.INNER_DROP_NOT_GREEDY)
        text_before, text_after, color_before, color_after = self.drop_in_or_through_area(method, drag_elem, drop_elem)
        self.drag_and_drop_by_offset(drag_elem, randint(-300, 300), randint(-200, 200))
        outer_text = self.element_is_visible(self.locators.OUTER_DROP_NOT_GREEDY).text
        outer_color = self.element_is_visible(self.locators.OUTER_DROP_NOT_GREEDY).value_of_css_property(
            "background-color")
        return text_before, text_after, color_before, color_after, outer_text, outer_color

    def outer_not_greedy_drop_in_area(self, method):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_elem = self.element_is_visible(self.locators.DRAG_ME)
        drop_elem = self.element_is_visible(self.locators.OUTER_DROP_NOT_GREEDY)
        inner_text_before = self.element_is_visible(self.locators.INNER_DROP_NOT_GREEDY).text
        text_before, text_after, color_before, color_after = self.drop_in_or_through_area(method, drag_elem, drop_elem)
        self.drag_and_drop_by_offset(drag_elem, randint(-300, 300), randint(-200, 200))
        inner_text_after = self.element_is_visible(self.locators.INNER_DROP_NOT_GREEDY).text
        return text_before, text_after, inner_text_before, inner_text_after
