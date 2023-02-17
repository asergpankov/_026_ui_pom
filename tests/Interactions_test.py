import pytest

from pages.Interactions_page import SortablePage


class TestInteractionsPage:
    class TestSortablePage:
        def test_change_item_order_position(self, driver):
            sortable = SortablePage(driver, "https://demoqa.com/sortable")
            sortable.open_browser()
            list_items_order_before, list_items_order_after = sortable.change_item_order_position('list')
            assert list_items_order_before != list_items_order_after
            grid_items_order_before, grid_items_order_after = sortable.change_item_order_position('grid')
            assert grid_items_order_before != grid_items_order_after
