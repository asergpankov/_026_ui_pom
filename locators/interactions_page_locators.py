from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEMS = (By.CSS_SELECTOR, 'div[class*="vertical-list-container"] > div')
    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEMS = (By.CSS_SELECTOR, 'div[class*="create-grid"] > div')
