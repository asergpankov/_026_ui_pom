from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from random import choice


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_browser(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.visibility_of_element_located(locator),
                                                message=f"[WARN]-- Can't find element by locator {locator}")

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.presence_of_element_located(locator),
                                                message=f"[WARN]-- Can't find element by locator {locator}")

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(ec.element_to_be_clickable(locator),
                                                message=f"[WARN]-- Can't find element by locator {locator}")

    def element_attribute_to_include(self, locator, attribute, timeout=13):
        return wait(self.driver, timeout).until(ec.element_attribute_to_include(locator, attribute_=attribute))

    def staleness_of(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.staleness_of(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def double_click_on(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def right_click_on(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def remove_footer(self):
        self.driver.execute_script('document.getElementsByTagName("footer")[0].remove();')
        self.driver.execute_script('document.getElementById("close-fixedban").remove();')

    def select_option_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_randon_year_month_day_from_list(self, elements):
        calendar = self.elements_are_present(elements)
        item = choice(calendar)
        item.click()

    def drag_and_drop_by_offset(self, element, x_offset, y_offset):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_offset, y_offset)
        action.perform()

    def drag_and_drop_to_element(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target)
        action.perform()

    def set_value(self, element, value):
        self.element_is_visible(element).clear()
        self.element_is_visible(element).send_keys(value)

    def left_click_on_element(self, element):
        self.element_is_visible(element)
        self.element_is_clickable(element).click()

    def get_element_text(self, element):
        element_text = self.element_is_visible(element).text
        return element_text

    def get_elements_text(self, elements):
        elements_on_page = self.elements_are_visible(elements)
        elements_names = [name.text for name in elements_on_page]
        return elements_names, len(elements_on_page)

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
