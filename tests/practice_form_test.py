import os
import time
from random import choice

from pages.practice_form_page import StudentRegistrationForm


class TestForm:
    class TestStudentRegistrationForm:
        def test_registration_form(self, driver, tmp_file):
            f_name, f_path = tmp_file
            test_registration_table = StudentRegistrationForm(driver, "https://demoqa.com/automation-practice-form")
            test_registration_table.open_browser()
            state_list = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
            person_data = test_registration_table.fill_all_fields(f_name, f_path, choice(state_list))
            result_table = test_registration_table.check_data_from_table_values()
            # print(person_data.first_name, person_data.last_name, person_data.email, person_data.mobile[:10], person_data.date_of_birth, person_data.current_address)
            assert f'{person_data.first_name} {person_data.last_name}' in result_table
            assert person_data.email in result_table
            assert person_data.mobile[:10] in result_table
            assert person_data.current_address in result_table
            os.remove(f_path)
            assert os.path.exists(f_path) is False

