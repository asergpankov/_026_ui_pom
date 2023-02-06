from generator.generator import generate_person_data
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage
from time import sleep, monotonic
from random import choice


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_new_tab_opened(self):
        self.element_is_visible(self.locators.NEW_TAB_BTN).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_tab_text = self.element_is_visible(self.locators.TEXT_ON_NEW_PAGE).text
        window_handles = len(self.driver.window_handles)
        return new_tab_text, window_handles

    def check_new_window_opened(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BTN).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_window_text = self.element_is_present(self.locators.TEXT_ON_NEW_PAGE).text
        return new_window_text


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_alert_regular(self):
        self.element_is_visible(self.locators.ALRT_SEE_BTN).click()
        alert = self.driver.switch_to.alert
        return alert.text

    def check_alert_appears_after_5sec(self):
        start_time = monotonic()
        self.element_is_visible(self.locators.ALRT_AFTER_5SEC_BTN).click()
        sleep(5)
        alert_text = self.driver.switch_to.alert
        alert_time = monotonic() - start_time
        return alert_text.text, alert_time

    def check_alert_confirm(self):
        self.element_is_visible(self.locators.ALRT_CONFIRM_BTN).click()
        alert = self.driver.switch_to.alert
        way = choice(['accept', 'dismiss'])
        if way == 'accept':
            alert.accept()
            result_text = self.element_is_present(self.locators.ALRT_CONFIRM_RESULT).text
            return result_text
        if way == 'dismiss':
            alert.dismiss()
            result_text = self.element_is_present(self.locators.ALRT_CONFIRM_RESULT).text
            return result_text

    def check_alert_promt(self):
        person_info = next(generate_person_data())
        sentence = person_info.sentence
        self.element_is_visible(self.locators.ALRT_PROMT_BTN).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(sentence)
        alert.accept()
        result_text = self.element_is_present(self.locators.ALRT_PROMT_RESULT).text
        return sentence, result_text


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame_conditions(self):
        frame = self.element_is_visible(self.locators.FIRST_FRAME)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.element_is_visible(self.locators.SAMPLE_TEXT).text
        self.driver.switch_to.default_content()
        return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def get_nested_frame_text(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_small_and_large_btns_names(self):
        sm_btn_name = self.element_is_visible(self.locators.SMALL_MODAL_BTN).text
        lg_btn_name = self.element_is_visible(self.locators.LARGE_MODAL_BTN).text
        return sm_btn_name,  lg_btn_name

    def check_small_modal_btn(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BTN).click()
        sm_title = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        sm_text = self.element_is_visible(self.locators.SMALL_MODAL_BODY).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BTN).click()
        return sm_title, len(sm_text)

    def check_large_modal_btn(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BTN).click()
        lg_title = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        lg_text = self.element_is_visible(self.locators.LARGE_MODAL_BODY).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BTN).click()
        return lg_title, len(lg_text)

    def check_small_and_large_modals_close_with_x_sign(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BTN).click()
        sm_sign = self.element_is_visible(self.locators.SMALL_MODAL_X_SIGN).text
        self.element_is_visible(self.locators.SMALL_MODAL_X_BTN).click()

        self.element_is_visible(self.locators.LARGE_MODAL_BTN).click()
        lg_sign = self.element_is_visible(self.locators.LARGE_MODAL_X_SIGN).text
        self.element_is_visible(self.locators.LARGE_MODAL_X_BTN).click()
        return [sm_sign, lg_sign]


