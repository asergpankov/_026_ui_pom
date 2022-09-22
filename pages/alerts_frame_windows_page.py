from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BTN).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_on_new_tab = self.element_is_present(self.locators.TEXT_ON_NEW_PAGE).text
        return title_on_new_tab

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BTN).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_on_new_window = self.element_is_present(self.locators.TEXT_ON_NEW_PAGE).text
        return title_on_new_window
