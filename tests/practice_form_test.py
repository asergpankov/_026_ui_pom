import os
import time

from pages.practice_form_page import StudentRegistrationForm


class TestForm:
    class TestStudentRegistrationForm:
        def test_registration_form(self, driver, tmp_file):
            f_name, f_path = tmp_file
            test_registration_table = StudentRegistrationForm(driver, "https://demoqa.com/automation-practice-form")
            test_registration_table.open()
            person = test_registration_table.fill_all_fields(f_name, f_path)
            result = test_registration_table.check_data_from_table_values()
            # print(person.first_name, person.last_name, person.email, person.mobile[:10], person.date_of_birth, person.current_address)
            assert f'{person.first_name} {person.last_name}' in result
            assert person.email in result
            assert person.mobile[:10] in result
            assert person.current_address in result
            os.remove(f_path)
            assert os.path.exists(f_path) is False
