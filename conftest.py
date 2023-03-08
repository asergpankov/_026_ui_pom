import time
import webdriver_manager.chrome

import allure
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import warnings
from fake_useragent import UserAgent
from random import random

user_agent = UserAgent()


@pytest.fixture(scope='function')
def driver():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # driver = Chrome(executable_path="./chromedriver")
    # driver_service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument(user_agent.random)
    # options.headless=True
    # options.add_argument('--remote-debugging-port=9222')
    # options.add_argument('--no-sandbox')

    driver = Chrome(service=Service(ChromeDriverManager().install()),
                    options=options)
    driver.set_window_size(1400, 1000)
    driver.maximize_window()
    # attach = driver.get_screenshot_as_png()
    # allure.attach(attach, name=f'screenshot{driver.session_id}', attachment_type=allure.attachment_type.PNG)
    # allure.attach(attach, name=f'screenshot{time.strftime("%Y-%m-%d-%H.%M")}', attachment_type=allure.attachment_type.PNG)
    yield driver
    driver.quit()


@pytest.fixture()
def tmp_file(tmp_path):
    fp = tmp_path / 'test_filename.txt'
    fp.write_text('text_content_inside_file')
    return fp.name, str(fp)

# @pytest.fixture(autouse=True)
# def configure(request):
#     env = request.config.getoption('--env')
#     ...
