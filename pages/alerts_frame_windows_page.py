from generator.generator import generate_person_data
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
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
