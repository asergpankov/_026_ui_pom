import os
import time

from pages.practice_form_page import StudentRegistrationForm


class TestForm:
    class TestStudentRegistrationForm:
        def test_reg_form(self, driver, tmp_file):
            f_name, f_path = tmp_file
            test_reg_form = StudentRegistrationForm(driver, "https://demoqa.com/automation-practice-form")
            test_reg_form.open()
            test_reg_form.fill_all_fields(f_name, f_path)
            time.sleep(10)
            # os.remove(f_path)