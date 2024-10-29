import os
import warnings

import pytest
from selenium import webdriver

from src.data_provider import Group_Option


@pytest.fixture(scope='function')
def driver_remote():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    job_name = os.environ['CI_JOB_NAME']
    match job_name:
        case 'chrome tests':
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-gpu')
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--incognito')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Remote(command_executor='http://selenium__standalone-chrome:4444/wd/hub',
                                      options=options)
        case 'firefox tests':
            options = webdriver.FirefoxOptions()
            options.add_argument('--disable-gpu')
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--incognito')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Remote(command_executor='http://selenium__standalone-firefox:4444/wd/hub',
                                      options=options)

        # case _:
        #     raise NotImplementedError('Something went wrong')

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function', params=['chrome', 'firefox', 'edge'])
def driver(request):
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    if request.param == 'chrome':
        driver = webdriver.Chrome()
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    if request.param == 'edge':
        # options.add_argument('--headless=new')
        driver = webdriver.Edge(options=options)
    request.cls.driver = driver

    driver.maximize_window()
    # driver.set_window_size(1400, 1000)
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


@pytest.fixture()
def group_data():
    return Group_Option.generate_group_option()
