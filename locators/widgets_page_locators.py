from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_HEADER = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    SECOND_HEADER = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"]')

    THIRD_HEADER = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_OUTPUT = (By.CSS_SELECTOR, 'div[class*="auto-complete__multi-value__label"]')
    COLOR_REMOVE_X_BTN = (By.CSS_SELECTOR, 'div[class*="auto-complete__multi-value__remove"]')
    COLOR_REMOVE_MAIN_X_BTN = (By.CSS_SELECTOR, 'div[class*="css-1wy0on6"]')

    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_OUTPUT = (By.CSS_SELECTOR, 'div[class*="auto-complete__single-value"]')


class DatePickerPageLocators:
    SELECT_DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    MONTH_SELECT = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    YEAR_SELECT = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DAY_SELECT = (By.CSS_SELECTOR, 'div[class*="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DT_MONTH_BTN = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DT_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-dropdown"] div')
    DT_YEAR_BTN = (By.CSS_SELECTOR, 'span[class="react-datepicker__year-read-view--selected-year"]')
    DT_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-dropdown"] div')
    DT_DAY = (By.CSS_SELECTOR, 'div[class*="react-datepicker__day react-datepicker__day"]')
    DT_TIME_LIST = (By.CSS_SELECTOR, 'ul[class="react-datepicker__time-list"] li')
