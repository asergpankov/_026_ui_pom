from generator.generator import generate_person_data
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators
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
        alert_text = self.driver.switch_to.alert
        return alert_text.text

    def check_alert_appears_after_5sec(self):
        start_time = monotonic()
        self.element_is_visible(self.locators.ALRT_AFTER_5SEC_BTN).click()
        sleep(5)
        alert_text = self.driver.switch_to.alert
        alert_time = monotonic() - start_time
        return alert_text.text, alert_time

    def check_alert_confirm(self):
        self.element_is_visible(self.locators.ALRT_CONFIRM_BTN).click()
        alert_text = self.driver.switch_to.alert
        way = choice(['accept', 'dismiss'])
        if way == 'accept':
            alert_text.accept()
            result_text = self.element_is_present(self.locators.ALRT_CONFIRM_RESULT).text
            return result_text
        if way == 'dismiss':
            alert_text.dismiss()
            result_text = self.element_is_present(self.locators.ALRT_CONFIRM_RESULT).text
            return result_text

    def check_alert_promt(self):
        person_info = next(generate_person_data())
        sentence = person_info.sentence
        self.element_is_visible(self.locators.ALRT_PROMT_BTN).click()
        alert_text = self.driver.switch_to.alert
        alert_text.send_keys(sentence)
        alert_text.accept()
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
