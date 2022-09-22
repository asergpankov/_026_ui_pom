from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_browser_new_tab(self, driver):
            browser_new_tab = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_new_tab.open()
            result = browser_new_tab.check_opened_new_tab()
            assert result == 'This is a sample page'

        def test_browser_new_window(self, driver):
            browser_new_window = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_new_window.open()
            result = browser_new_window.check_opened_new_window()
            assert result == 'This is a sample page'
