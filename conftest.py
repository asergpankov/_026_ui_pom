import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import warnings


@pytest.fixture(scope='function')
def driver():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver_service = Service(ChromeDriverManager().install())
    driver = Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()
