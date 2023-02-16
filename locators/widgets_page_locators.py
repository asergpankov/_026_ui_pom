from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_HEADER = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    SECOND_HEADER = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"]')

    THIRD_HEADER = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_OUTPUT = (By.CSS_SELECTOR, 'div[class*="auto-complete__multi-value__label"]')
    COLOR_REMOVE_X_BTN = (By.CSS_SELECTOR, 'div[class*="auto-complete__multi-value__remove"]')
    COLOR_REMOVE_MAIN_X_BTN = (By.CSS_SELECTOR, 'div[class*="css-1wy0on6"]')

    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_OUTPUT = (By.CSS_SELECTOR, 'div[class*="auto-complete__single-value"]')


class DatePickerPageLocators:
    SELECT_DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    MONTH_SELECT = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    YEAR_SELECT = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DAY_SELECT = (By.CSS_SELECTOR, 'div[class*="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DT_MONTH_BTN = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DT_MONTH_LIST = (By.CSS_SELECTOR, 'div[class*="react-datepicker__month-option"]')
    DT_YEAR_BTN = (By.CSS_SELECTOR, 'span[class="react-datepicker__year-read-view--selected-year"]')
    DT_YEAR_LIST = (By.CSS_SELECTOR, 'div[class*="eact-datepicker__year-option"]:not(:first-child):not(:last-child)')
    DT_DAY_LIST = (By.CSS_SELECTOR, 'div[class*="react-datepicker__day react-datepicker__day"]')
    DT_TIME_LIST = (By.CSS_SELECTOR, 'ul[class="react-datepicker__time-list"] li')


class SliderPageLocators:
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')
    SLIDER_LINE = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')


class ProgressBarPageLocators:
    START_STOP_BTN = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    RESET_BTN = (By.CSS_SELECTOR, 'button[id="resetButton"]')
    PR_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')
    PR_BAR_SUCCESS_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-success"]')


class TabsPageLocators:
    TABS_LIST = (By.CSS_SELECTOR, 'nav a')
    TABS_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"] p')


class ToolTipsPageLocators:
    GREEN_BTN = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    HOVER_TIP_BTN = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')
    CONTRARY_LINK = (By.XPATH, '//*[text()="Contrary"]')
    CONTRARY_HOVER_TIP = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')
    SECTION_LINK = (By.XPATH, '//*[text()="1.10.32"]')
    SECTION_HOVER_TIP = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    FIELD_INPUT = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    FIELD_HOVER_TIP = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    HOVER_TIP_INNER_TEXT = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuPageLocators:
    MENU_ITEMS = (By.CSS_SELECTOR, 'ul li a')


class SelectMenuPageLocators:
    SELECT_OPTION_INPUT = (By.XPATH, '//div[@id="withOptGroup"]//input')
    SELECT_OPTION_OUTPUT = (By.XPATH, '//div[@id="withOptGroup"]//div[@class=" css-1uccc91-singleValue"]')
    SELECT_TITLE_INPUT = (By.XPATH, '//div[@id="selectOne"]//input')
    SELECT_TITLE_OUTPUT = (By.XPATH, '//div[@id="selectOne"]//div[@class=" css-1uccc91-singleValue"]')

    COLOR_SELECT = (By.XPATH, '//select[@id="oldSelectMenu"]')
    COLOR_OPTIONS = (By.XPATH, '//select[@id="oldSelectMenu"]/option')
    COLOR_OPTION_BLACK = (By.XPATH, '//option[text()="Black"]')
    MULTISELECT_INPUT = (By.XPATH, '//div[text()="Select..."]/ancestor::div[1]//input')
    MULTISELECT_INPUT_SNEAKY = (By.XPATH, '//div[text()="Blue"]/ancestor::div[3]//input')
    MULTISELECT_OUTPUT_CLR = (By.XPATH, '//div[@class="css-1rhbuit-multiValue"]/div[1]')
    OUTPUT_CLRS = (By.XPATH, '//div[@class="css-12jo7m5"]')