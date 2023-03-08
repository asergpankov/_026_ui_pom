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


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogsPageLocators:
    SMALL_MODAL_BTN = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BTN = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    SMALL_MODAL_X_SIGN = (By.CSS_SELECTOR, 'span[class="sr-only"]')
    SMALL_MODAL_X_BTN = (By.CSS_SELECTOR, 'button[class="close"')
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')
    SMALL_MODAL_BODY = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    LARGE_MODAL_BTN = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_CLOSE_BTN = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
    LARGE_MODAL_X_SIGN = (By.CSS_SELECTOR, 'span[class="sr-only"]')
    LARGE_MODAL_X_BTN = (By.CSS_SELECTOR, 'button[class="close"]')
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')
    LARGE_MODAL_BODY = (By.CSS_SELECTOR, 'p[class]')
