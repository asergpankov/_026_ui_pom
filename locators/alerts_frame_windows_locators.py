from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BTN = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BTN = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    TEXT_ON_NEW_PAGE = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class AlertsPageLocators:
    pass
