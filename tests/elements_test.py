from pages.elements_page import TextBoxPage


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
            # assert input_data == output_data