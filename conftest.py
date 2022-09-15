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
    # driver.set_window_size(1400, 1000)
    yield driver
    driver.quit()

@pytest.fixture()
def create_file(tmp_path):
    f = tmp_path / 'test_filename.txt'
    f.write_text('test_content_inside')
    return f
    # assert os.path.exists(f) is False