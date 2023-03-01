import pytest

from pages.Interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage
from src.enums.global_enums import SelectablePageEnums


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
            elements_names, elements_on_page = selectable.check_elements_on_page('list')
            assert elements_names == SelectablePageEnums.LIST_NAMES.value, 'items names were changed'
            assert len(elements_names) == elements_on_page, 'number of elements is not equal current names'

        def test_check_names_and_numbers_on_grid_tab(self, driver):
            selectable = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable.open_browser()
            elements_names, elements_on_page = selectable.check_elements_on_page('grid')
            assert elements_names == SelectablePageEnums.GRID_NAMES.value, 'items names were changed'
            assert len(elements_names) == elements_on_page, 'number of elements is not equal current names'

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

    class TestResizablePage:

        def test_resizable_box_oversize_500x_300(self, driver):
            resizable = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable.open_browser()
            position = resizable.change_resizable_box_size(600, 400)
            assert position == 'width: 500px; height: 300px;'

        def test_resizable_box_drop_under_150x_150(self, driver):
            resizable = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable.open_browser()
            position = resizable.change_resizable_box_size(-300, -300)
            assert position == 'width: 150px; height: 150px;'

        # @pytest.mark.skip(reason='flaky. success depends from window size')
        def test_resizable_oversize_500x_300(self, driver):
            resizable = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable.open_browser()
            position = resizable.change_resizable_size(900, 500)
            assert position == 'width: 20px; height: 20px;'

        def test_resizable_drop_under_20x_20(self, driver):
            resizable = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable.open_browser()
            position = resizable.change_resizable_size(-300, -300)
            assert position == 'width: 20px; height: 20px;'

    class TestDroppablePage:

        def test_simple_drop_in_area(self, driver):
            droppable = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable.open_browser()
            text_before, text_after, color_before, color_after = droppable.regular_drop('simple', 'in')
            assert text_before == 'Drop here'
            assert text_after == 'Dropped!'
            assert color_before == 'rgba(0, 0, 0, 0)'
            assert color_after == 'rgba(70, 130, 180, 1)'

        def test_simple_drop_through_area(self, driver):
            droppable = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable.open_browser()
            text_before, text_after, color_before, color_after = droppable.regular_drop('simple', 'through')
            assert text_before == text_after
            assert color_before == color_after

        def test_not_acceptable_drop_in_area(self, driver):
            droppable = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable.open_browser()
            text_before, text_after, color_before, color_after = droppable.regular_drop('not accept', 'in')
            assert text_before == text_after
            assert color_before == color_after

        def test_not_acceptable_drop_through_area(self, driver):
            droppable = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable.open_browser()
            text_before, text_after, color_before, color_after = droppable.regular_drop('not accept', 'through')
            assert text_before == text_after
            assert color_before == color_after

        # @pytest.mark.skip(reason='flaky. success depends from window size')
        # TODO make intermediate test on green color before click down
        def test_acceptable_drop_in_area(self, driver):
            droppable = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable.open_browser()
            text_before, text_after, color_before, color_after = droppable.regular_drop('accept', 'in')
            assert text_before == 'Drop here'
            assert text_after == 'Dropped!'
            assert color_before == 'rgba(0, 0, 0, 0)'
            assert color_after == 'rgba(70, 130, 180, 1)'

        def test_inner_not_greedy_drop_in_area(self, driver):
            droppable = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable.open_browser()
            text_before, text_after, color_before, color_after, outer_text, outer_color = droppable.inner_not_greedy_drop_in_area(
                'in')
            assert text_before == 'Inner droppable (not greedy)'
            assert text_after == 'Dropped!'
            assert color_before == 'rgba(0, 0, 0, 0)'
            # assert color_after == 'rgba(70, 130, 180, 1)' # TODO find out whats wrong with color
            assert outer_text == 'Dropped!'
            # assert outer_color == 'rgba(70, 130, 180, 1)'

        def test_outer_not_greedy_drop_in_area(self, driver):
            droppable = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable.open_browser()
            text_before, text_after, inner_text_before, inner_text_after = droppable.outer_not_greedy_drop_in_area('in')
            assert text_before == 'Outer droppable'
            assert text_after == 'Dropped!'
            assert inner_text_before == inner_text_after and inner_text_after == 'Inner droppable (not greedy)'
