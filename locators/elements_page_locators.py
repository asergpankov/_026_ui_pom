from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input#userName")
    EMAIL = (By.CSS_SELECTOR, "input#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea#permanentAddress")
    SUBMIT = (By.CSS_SELECTOR, "button#submit")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "p#name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "p#email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p#currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p#permanentAddress")
