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
