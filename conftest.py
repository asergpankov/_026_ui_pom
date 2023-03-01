import time

import allure
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import warnings


@pytest.fixture(scope='function')
def driver():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # driver = Chrome(executable_path="./chromedriver")
    driver_service = Service(ChromeDriverManager().install())
    driver = Chrome(service=driver_service)
    driver.set_window_size(1400, 1000)
    driver.maximize_window()
    attach = driver.get_screenshot_as_png()
    # allure.attach(attach, name=f'screenshot{driver.session_id}', attachment_type=allure.attachment_type.PNG)
    allure.attach(attach, name=f'screenshot{time.strftime("%Y-%m-%d-%H.%M")}', attachment_type=allure.attachment_type.PNG)
    yield driver
    driver.quit()


@pytest.fixture()
def tmp_file(tmp_path):
    fp = tmp_path / 'test_filename.txt'
    fp.write_text('text_content_inside_file')
    return fp.name, str(fp)
