from selenium.webdriver.common.by import By


class BookStoreApplicationPageLocators:
    USER_NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="UserName"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Password"]')

    LOGIN_BTN = (By.CSS_SELECTOR, 'button[id="login"]')
    INVALID_USERNAME_PASSWORD = (By.CSS_SELECTOR, 'p#name')

    NEW_USER_BTN = (By.CSS_SELECTOR, 'button[id="newUser"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input#firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input#lastname')
    USER_NAME_INPUT = (By.CSS_SELECTOR, 'input#userName')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#password')
    RECAPTCHA_BOX = (By.CSS_SELECTOR, 'label#recaptcha-anchor-label')

    MAIN_HEADER = (By.XPATH, '//div[contains(text(), "Profile")]')
    LOGIN_NAME = (By.CSS_SELECTOR, 'label#userName-value')
