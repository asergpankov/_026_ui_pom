from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage
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

    class TestNestedFrames:
        def test_nested_frame_text(self, driver):
            nested_frame = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frame.open_browser()
            parent_text, child_text = nested_frame.get_nested_frame_text()
            assert parent_text == 'Parent frame', "[WARN] -- smth went wrong with getting a parent frame text"
            assert child_text == 'Child Iframe', "[WARN] -- smth went wrong with getting a child iframe text"

    class TestModalDialogs:
        def test_small_and_large_btns_names(self, driver):
            small_modal = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            small_modal.open_browser()
            sm_btn_name, lg_btn_name = small_modal.check_small_and_large_btns_names()
            assert sm_btn_name == 'Small modal'
            assert lg_btn_name == 'Large modal'

        def test_small_modal_btn(self, driver):
            small_modal = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            small_modal.open_browser()
            sm_title, sm_text_len = small_modal.check_small_modal_btn()
            assert sm_title == 'Small Modal', "[WARN] -- sm_modal_title was changed"
            assert 0 < sm_text_len < 50, "[WARN] -- length of sm_modal_text was changed"

        def test_large_modal_btn(self, driver):
            large_modal = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            large_modal.open_browser()
            lg_title, lg_text_len = large_modal.check_large_modal_btn()
            assert lg_title == 'Large Modal', "[WARN] -- lg_modal_title was changed"
            assert 0 < lg_text_len < 600, "[WARN] -- length of lg_modal_text was changed"

        def test_small_and_large_modals_close_with_x_sign(self, driver):
            mb = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            mb.open_browser()
            result = mb.check_small_and_large_modals_close_with_x_sign()
            assert result == ['Close', 'Close'], "[WARN] -- x sign does not close as needed"
