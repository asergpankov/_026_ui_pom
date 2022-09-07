import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import warnings


@pytest.fixture(scope='session')
def driver():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # driver = Chrome(executable_path="./chromedriver")
    driver_service = Service(ChromeDriverManager().install())
    driver = Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()
