from selenium.webdriver.common.by import By
from random import randint

class StudentRegistrationFormLocators:
    FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="First Name"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
    GENDER_RADIO_BTNS = (By.CSS_SELECTOR, f'label[for="gender-radio-{randint(1, 3)}"]')
    EMAIL = (By.CSS_SELECTOR, 'input[placeholder="name@example.com"]')
    MOBILE_NMB = (By.CSS_SELECTOR, 'input[placeholder="Mobile Number"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'div[class*="input-container"] input[id="dateOfBirthInput"]')
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES = (By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{randint(1, 3)}"]')
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')

    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[placeholder="Current Address"]')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    SELECT_STATE_INP = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    SELECT_CITY_INP = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'button[class*="btn btn-primary"]')

    # RESULT_TABLE = (By.CSS_SELECTOR, 'table[class*="table-bordered table-hover"]')
    RESULT_TABLE_VALUES = (By.XPATH, '//div[@class="table-responsive"]//td[2]')