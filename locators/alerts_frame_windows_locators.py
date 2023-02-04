from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BTN = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BTN = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    TEXT_ON_NEW_PAGE = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class AlertsPageLocators:
    ALRT_SEE_BTN = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    ALRT_AFTER_5SEC_BTN = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    ALRT_CONFIRM_BTN = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    ALRT_CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    ALRT_PROMT_BTN = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    ALRT_PROMT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    SAMPLE_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
