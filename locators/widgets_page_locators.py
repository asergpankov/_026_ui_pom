from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_HEADER = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    SECOND_HEADER = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"]')

    THIRD_HEADER = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')

    # CARDS_HEADER = (By.CSS_SELECTOR, 'div[class="card-header"]')
    # CARDS_CONTENT = (By.CSS_SELECTOR, 'div[class="card-body"]')