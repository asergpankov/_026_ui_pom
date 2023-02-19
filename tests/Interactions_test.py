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

        def test_check_names_and_numbers_on_list_tab(self, driver):
            selectable = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable.open_browser()
            elements_names, elements_on_page = selectable.check_elements_on_page()
            assert elements_names == ['Cras justo odio', 'Dapibus ac facilisis in', 'Morbi leo risus',
                                      'Porta ac consectetur ac'], 'names were changed'
            assert len(elements_names) == elements_on_page, 'number of elements is not equal current names'

        @pytest.mark.skip('need to finish') #TODO need to finish test
        def test_check_names_and_numbers_on_grid_tab(self, driver):
            selectable = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable.open_browser()

        def test_check_selectable_item_on_list_tab(self, driver):
            selectable = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable.open_browser()
            clicked_items = selectable.clicking_on_random_items('list')
            active_items_list = selectable.get_active_items('list')
            assert all(e in clicked_items for e in active_items_list), 'diffs btw an active and a nonactive element'

        def test_check_selectable_item_on_grid_tab(self, driver):
            selectable = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable.open_browser()
            clicked_items = selectable.clicking_on_random_items('grid')
            active_items_list = selectable.get_active_items('grid')
            assert all(e in clicked_items for e in active_items_list), 'diffs btw an active and a nonactive element'

        def test_choose_and_cancellation_all_items_on_list_tab(self, driver):
            selectable = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable.open_browser()
            res1, res2, res3 = selectable.choose_and_cancellation_all_items('list')
            assert res1 == res2 == res3, 'wrong numbers of active and nonactive items after cancellation'

        def test_choose_and_cancellation_all_items_on_grid_tab(self, driver):
            selectable = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable.open_browser()
            res1, res2, res3 = selectable.choose_and_cancellation_all_items('grid')
            assert res1 == res2 == res3, 'wrong numbers of active and nonactive items after cancellation'
