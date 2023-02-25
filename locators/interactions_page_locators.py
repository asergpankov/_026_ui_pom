from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEMS = (By.CSS_SELECTOR, 'div[class*="vertical-list-container"] > div')
    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEMS = (By.CSS_SELECTOR, 'div[class*="create-grid"] > div')


class SelectablePageLocators:
    LIST_TAB = (By.XPATH, '//a[@id="demo-tab-list"]')
    LIST_ITEMS = (By.XPATH, '//ul[@id="verticalListContainer"]/li')
    LIST_ITEMS_ACTIVE = (By.CSS_SELECTOR, 'ul[id="verticalListContainer"] li[class*="active"]')
    GRID_TAB = (By.XPATH, '//a[@id="demo-tab-grid"]')
    GRID_ITEMS = (By.XPATH, '//div[@id="demo-tabpane-grid"]//li')
    GRID_ITEMS_ACTIVE = (By.XPATH, '//div[@id="demo-tabpane-grid"]//li[contains(@class, "active")]')


class ResizablePageLocators:
    RESIZABLE_BOX = (By.XPATH, "//div[@id='resizableBoxWithRestriction']")
    RESIZABLE_BOX_HANDLE = (By.XPATH, "//div[@id='resizableBoxWithRestriction']//span")
    RESIZABLE = (By.XPATH, "//div[@id='resizable']")
    RESIZABLE_HANDLE = (By.XPATH, "//div[@class='resizable-nolimit mt-4']//span")
