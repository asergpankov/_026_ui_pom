from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


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
