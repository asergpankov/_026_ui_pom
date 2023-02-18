import pytest

from pages.Interactions_page import SortablePage, SelectablePage


class TestInteractionsPage:
    class TestSortablePage:
        def test_change_item_order_position(self, driver):
            sortable = SortablePage(driver, "https://demoqa.com/sortable")
            sortable.open_browser()
            list_items_order_before, list_items_order_after = sortable.change_item_order_position('list')
            assert list_items_order_before != list_items_order_after, 'items order in LIST_tab were broken'
            grid_items_order_before, grid_items_order_after = sortable.change_item_order_position('grid')
            assert grid_items_order_before != grid_items_order_after, 'items order in GRID_tab were broken'

    class TestSelectablePage:
        def test_check_elements_on_page(self, driver):
            selectable = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable.open_browser()
            elements_names, elements_on_page = selectable.check_elements_on_page()
            assert elements_names == ['Cras justo odio', 'Dapibus ac facilisis in', 'Morbi leo risus',
                                      'Porta ac consectetur ac'], 'names were changed'
            assert len(elements_names) == elements_on_page, 'number of elements is not equal current names'
            rand_item_text, active_items_after = selectable.check_selectable_item()
            assert rand_item_text == active_items_after, 'diffs btw an active and a nonactive element'
