from pages.widgets_page import AccordianPage


class TestWidgetsPage:

    class TestAccordianPage:
        def test_accordian_structure(self, driver):
            accordian = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian.open_browser()
            first_title, first_content = accordian.check_accordian_structure('first')
            second_title, second_content = accordian.check_accordian_structure('second')
            third_title, third_content = accordian.check_accordian_structure('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 11
            assert second_title == 'Where does it come from?' and second_content > 11
            assert third_title == 'Why do we use it?' and third_content > 222
