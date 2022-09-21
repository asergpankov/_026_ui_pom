from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.visibility_of_element_located(locator),
                                                message=f"[WARN]-- Can't find element by locator {locator}")

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.presence_of_element_located(locator),
                                                message=f"[WARN]-- Can't find element by locator {locator}")

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.element_to_be_clickable(locator),
                                                message=f"[WARN]-- Can't find element by locator {locator}")

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def double_click_action(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def right_click_action(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def remove_footer(self):
        self.driver.execute_script('document.getElementsByTagName("footer")[0].remove();')
        self.driver.execute_script('document.getElementById("close-fixedban").remove();')