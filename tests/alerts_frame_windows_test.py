from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage
import pytest


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
        def test_alert_regular(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open_browser()
            alert_text = alerts_page.check_alert_regular()
            assert alert_text == 'You clicked a button', "[WARN] -- regular alert does not work as expected"

        @pytest.mark.flaky(reruns=2)
        def test_alert_appears_after_5sec(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open_browser()
            alert_text, alert_time = alerts_page.check_alert_appears_after_5sec()
            assert alert_text == 'This alert appeared after 5 seconds', "[WARN] -- 5 sec. alert does not work as expected"
            assert alert_time >= 5, f"alert appear time is {alert_time}"

        def test_alert_confirm(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open_browser()
            result_text = alerts_page.check_alert_confirm()
            assert result_text == 'You selected Ok' or result_text == 'You selected Cancel', f"[WARN] -- res is: {result_text}"

        def test_alert_promt(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open_browser()
            sentence, result_text = alerts_page.check_alert_promt()
            assert result_text == f"You entered {sentence}", f"[WARN] -- sentence does not correspond with {result_text}"

    class TestFrames:
        def test_frame_conditions(self, driver):
            frame_cond = FramesPage(driver, "https://demoqa.com/frames")
            frame_cond.open_browser()
            result_frame = frame_cond.check_frame_conditions()
            assert result_frame == ['This is a sample page', '500px', '350px'], "[WARN] -- frame condition were broken"
