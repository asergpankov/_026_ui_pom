from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_browser_new_tab(self, driver):
            new_tab = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab.open_browser()
            new_tab_text, window_handles = new_tab.check_new_tab_opened()
            assert new_tab_text == 'This is a sample page'
            assert window_handles == 2, "[WARN] -- expect only two opened tabs"

        def test_browser_new_window(self, driver):
            new_window = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_window.open_browser()
            new_window_text = new_window.check_new_window_opened()
            assert new_window_text == 'This is a sample page'

    class TestAlerts:
        def test_alerts(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open_browser()