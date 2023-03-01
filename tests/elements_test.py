import os
import time
from random import randint
from time import sleep

import allure
import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownload, DynamicProperties


@allure.suite('Elements suite')
class TestElements:
    @allure.feature('Text Box')
    class TestTextBox:
        @allure.title('data in TextBox')
        def test_all_data_in_text_boxes(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open_browser()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_text_boxes()
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_full_name
            assert email != output_email, "[WARN] -- email has not been inputed correctly"
            assert current_address == output_current_address
            assert permanent_address == output_permanent_address
            # assert input_data == output_data, "[WARN] -- data has not been inputed correctly"

    @allure.feature('Check Box')
    class TestCheckBox:
        @allure.title('Expand checkboxes on page')
        def test_checkbox_page(self, driver):
            checkbox_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            checkbox_page.open_browser()
            checkbox_page.expand_all_checkboxes()
            checkbox_page.click_random_checkbox()
            input_data = checkbox_page.get_marked_checkboxes()
            output_data = checkbox_page.get_output_result()
            assert input_data == output_data, "[WARN] -- checkboxes have not been selected"

    @allure.feature('Radio Buttons')
    class TestRadioButton:
        @allure.title('click on radio buttons')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open_browser()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            # radio_button_page.click_on_radio_button('no')
            # output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes'
            assert output_impressive == 'Impressive'
            # assert output_no == 'No', "[WARN! BUG is here] -- 'No' btn cannot be selected"
            # 'No' button has a bug during selection"

    @allure.feature('Webtable')
    class TestWebTable:
        @allure.title('webtable add person')
        def test_webtable_add_person(self, driver):
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            webtable_page.open_browser()
            new_person = webtable_page.add_new_person()
            table_result = webtable_page.check_added_person()
            assert new_person in table_result, "[WARN] -- 'person_data' not in table"

        @allure.title('webtable search person')
        def test_webtable_search_person(self, driver):
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            webtable_page.open_browser()
            key_word = webtable_page.add_new_person()[randint(0, 5)]
            webtable_page.search_box_input(key_word)
            table_line_data = webtable_page.check_added_person()
            assert key_word in table_line_data[0], "[WARN] -- 'key_word' NOT in the person data"

        @allure.title('webtable update person info age')
        def test_web_table_update_person_info_age(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open_browser()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_box_input(last_name)
            age = web_table_page.update_person_info_age()
            row = web_table_page.check_added_person()[0]
            assert age in row, "[WARN] -- 'age' has not been changed"

        @allure.title('webtable update person info email')
        def test_web_table_update_person_info_email(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open_browser()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_box_input(last_name)
            email = web_table_page.update_person_info_email()
            row = web_table_page.check_added_person()[0]
            assert email in row, "[WARN] -- 'email' has not been changed"

        @allure.title('webtable delete person info')
        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open_browser()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_box_input(email)
            web_table_page.delete_person_info_btn()
            no_rows_text = web_table_page.check_deleted_person_message()
            assert no_rows_text == "No rows found"

        # @pytest.mark.skip(reason="need to remove footer for interacting with '100 rows'")
        @allure.title('webtable rows count')
        def test_web_table_change_rows_count(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open_browser()
            web_table_page.remove_footer()
            count = web_table_page.iterate_on_rows()
            assert count == [5, 10, 20, 25, 50, 100], "[WARN] -- the numbers of rows appear incorrectly"

    @allure.feature('Buttons')
    class TestButtonsPage:
        @allure.title('different click on the buttons')
        def test_different_click_on_the_buttons(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open_browser()
            double = buttons_page.click_on_different_buttons("double_left")
            right = buttons_page.click_on_different_buttons("right")
            click = buttons_page.click_on_different_buttons("click")
            assert double == "You have done a double click", "[WARN] -- DoubleClick button was not press correctly"
            assert right == "You have done a right click", "[WARN] -- RightClick button was not press correctly"
            assert click == "You have done a dynamic click", "[WARN] -- ClickMe  button was not press correctly"

    @allure.feature('Links')
    class TestLinks:
        @allure.feature('home link check')
        def test_check_home_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open_browser()
            href_link, current_url = links_page.check_new_tab_home_link()
            assert href_link == current_url, "[WARN] -- broken link or incorrect url"

        @allure.feature('broken link check')
        def test_check_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open_browser()
            status_code = links_page.check_bad_request("https://demoqa.com/bad-request")
            assert status_code == 400, "[WARN] -- broken link suddenly works"

    @allure.feature('Upload and Download')
    class TestUploadAndDownload:
        @allure.title('upload file')
        def test_upload_file(self, driver, tmp_file):
            file_name, path = tmp_file
            upload_page = UploadAndDownload(driver, "https://demoqa.com/upload-download")
            upload_page.open_browser()
            get_file_name = upload_page.upload_file(path)
            assert get_file_name == file_name
            os.remove(path)
            assert os.path.exists(path) is False

        @pytest.mark.skip(reason='not ready yet. need correct decoding')
        @allure.title('download file')
        def test_download_file(self, driver):
            download_page = UploadAndDownload(driver, "https://demoqa.com/upload-download")
            download_page.open_browser()
            download_page.download_file()
            assert os.path.isfile() is True
            os.remove()

    @allure.feature('Dynamic Properties')
    class TestDynamicProperties:

        @allure.title('btn will be enable after 5 seconds')
        def test_btn_will_be_enable_after_5_seconds(self, driver):
            dynamic_properties = DynamicProperties(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties.open_browser()
            btn_is_enable = dynamic_properties.check_btn_is_enable()
            assert btn_is_enable is True, "[WARN] -- btn is not enable after 5 sec."

        @allure.title('btn color has changed')
        def test_btn_color_has_changed(self, driver):
            dynamic_properties = DynamicProperties(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties.open_browser()
            clr_before, clr_after = dynamic_properties.check_color_changed()
            assert clr_before != clr_after, "[WARN] -- btn color was not changed"

        @allure.title('btn is visible after 5 seconds')
        def test_btn_is_visible_after_5_seconds(self, driver):
            dynamic_properties = DynamicProperties(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties.open_browser()
            btn_is_visible = dynamic_properties.check_btn_visibility()
            assert btn_is_visible is True, "[WARN] -- btn is not visible after 5 sec."

# it was last test on Elements page
