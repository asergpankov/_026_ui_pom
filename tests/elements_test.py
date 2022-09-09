from random import randint
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage


class TestElements:
    class TestTextBox:
        def test_text_boxes(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_full_name
            assert email == output_email
            assert current_address == output_current_address
            assert permanent_address == output_permanent_address
            # assert input_data == output_data, "[WARN] -- data has not been inputed correctly"

    class TestCheckBox:
        def test_checkbox_page(self, driver):
            checkbox_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            checkbox_page.open()
            checkbox_page.expand_all_checkboxes()
            checkbox_page.click_random_checkbox()
            input_data = checkbox_page.get_marked_checkboxes()
            output_data = checkbox_page.get_output_result()
            assert input_data == output_data, "[WARN] -- checkboxes have not been selected"

    class TestRadioButton:
        @pytest.mark.skip(reason='postponed for some reasons')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            # radio_button_page.click_on_radio_button('Yes')
            # output_yes = radio_button_page.get_output_result()
            # radio_button_page.click_on_radio_button('Impressive')
            # output_impressive = radio_button_page.get_output_result()
            # radio_button_page.click_on_radio_button('No')
            # output_no = radio_button_page.get_output_result()
            # assert output_yes == 'Yes'
            # assert output_impressive == 'Impressive'
            # assert output_no == 'No'
            sleep(2)

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_added_person()
            assert new_person in table_result, "[WARN] -- 'person_data' not in table"
            sleep(2)

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[randint(0, 5)]
            web_table_page.search_added_person(key_word)
            table_line_data = web_table_page.check_added_person()
            assert key_word in table_line_data[0], "[WARN] -- 'key_word' NOT in person data"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_added_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_added_person()
            assert age in row[0], "[WARN] -- 'age' has not been changed"

        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_added_person(email)
            web_table_page.delete_person_info()
            no_rows_text = web_table_page.check_deleted_person()
            assert no_rows_text == "No rows found"

        @pytest.mark.skip(reason="BUGS in the length's view of the persons list")
        def test_web_table_change_rows_count(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.iterate_rows()
            assert count == [5, 10, 20, 25, 50, 100], "[WARN] -- the numbers of rows appear incorrectly"

    class TestButtonsPage:
        def test_different_click_on_the_buttons(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            double = buttons_page.click_on_different_buttons("double")
            right = buttons_page.click_on_different_buttons("right")
            click = buttons_page.click_on_different_buttons("click")
            assert double == "You have done a double click", "DoubleClick button was not press correctly"
            assert right == "You have done a right click", "RightClick button was not press correctly"
            assert click == "You have done a dynamic click", "ClickMe  button was not press correctly"

    class TestLinks:
        def test_check_home_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            link_href, current_url = links_page.check_new_tab_home_link()
            assert link_href == current_url, "[WARN] -- broken link or incorrect url"

        def test_check_bad_request_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.check_new_tab_bad_request_link("https://demoqa.com/bad-request")
            assert response_code == 400

