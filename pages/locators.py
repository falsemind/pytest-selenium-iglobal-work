from selenium.webdriver.common.by import By

# LOGIN PAGE
FORM_USERNAME = (By.CSS_SELECTOR, "input[name='username']")
FORM_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
FORM_SUBMIT_BTN = (By.XPATH, "//button[contains(., 'Login')]")

# ADMIN / USER MANAGEMENT PAGE
HEADER_TITLE = (By.CLASS_NAME, "oxd-topbar-header-title")
USER_SEARCH_BTN = (By.XPATH, "//button[contains(., 'Search')]")
RESET_SEARCH_BTN = (By.XPATH, "//button[contains(., 'Reset')]")
LOADER = (By.CLASS_NAME, "oxd-form-loader")
ADD_USER_BTN = (By.XPATH, "//button[contains(., 'Add')]")
DEL_USER_ROW_BTN = lambda username: (By.XPATH, f"//div[@role='row'][div[2]/div[text()='{username}']]//div[@class='oxd-table-cell-actions']//button[1]")
DEL_USER_POPUP_BTN = (By.XPATH, "//button[contains(., 'Yes, Delete')]")
DEL_TOAST_MSG = (By.XPATH, "//p[contains(., 'Successfully Deleted')]")

FOUND_1USER = (By.XPATH, "//span[contains(., '(1) Record Found')]")
FOUND_USER = lambda username: (By.XPATH, f"//div[@class='oxd-table-body']//div[contains(text(), '{username}')]")
USER_TABLE_CELL = (By.XPATH, "//div[@role='row']//div[@role='cell'][2]//div")

ROLE_DROPDOWN = (By.XPATH, "//label[text()='User Role']/following::div[contains(@class, 'oxd-select-text')][1]")
ADMIN_ROLE = (By.XPATH, "//div[@class='oxd-select-option']//span[text()='Admin']")
ESS_ROLE = (By.XPATH, "//div[@class='oxd-select-option']//span[text()='ESS']")

STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/following::div[contains(@class, 'oxd-select-text')][1]")
STATUS_ENABLED = (By.XPATH, "//div[@class='oxd-select-option']//span[text()='Enabled']")
STATUS_DISABLED = (By.XPATH, "//div[@class='oxd-select-option']//span[text()='Disabled']")

USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/following::input[1]")
EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[text()='Employee Name']/following::input[1]")
EMPLOYEE_NAME_SEARCH = (By.XPATH, "//div[@role='listbox']//div[@role='option']//span[text()='joker john selvam']")

PASSWORD_INPUT = (By.XPATH, "//label[text()='Password']/following::input[@type='password'][1]")
PASSWORD_CONFIRM_INPUT = (By.XPATH, "//label[text()='Confirm Password']/following::input[@type='password'][1]")

SAVE_BTN = (By.CSS_SELECTOR, "button[type='submit'].oxd-button--secondary")
TOAST_MSG = (By.ID, "oxd-toaster_1")