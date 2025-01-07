from pages.base_page import BasePage
from pages.locators import *

class UserManagementPage(BasePage):

    def create_user(self, role: str, status: str, user_name: str, user_password: str):
        user_role = ADMIN_ROLE if role == "admin" else ESS_ROLE
        user_status = STATUS_ENABLED if status == "enabled" else STATUS_DISABLED

        self.wait_for_element(ADD_USER_BTN).click()
        # select user role
        self.wait_for_element(ROLE_DROPDOWN).click()
        self.wait_for_element_visibility(user_role).click()
        # select user status
        self.wait_for_element(STATUS_DROPDOWN).click()
        self.wait_for_element_visibility(user_status).click()
        # enter user and employee names
        self.find_element(EMPLOYEE_NAME_INPUT).send_keys("John  Doe") # hardcoded existing name for the sake of simplicity
        self.wait_for_element_visibility(EMPLOYEE_NAME_SEARCH).click()
        self.find_element(USERNAME_INPUT).send_keys(user_name)
        # enter password
        self.find_element(PASSWORD_INPUT).send_keys(user_password)
        self.find_element(PASSWORD_CONFIRM_INPUT).send_keys(user_password)
        # save/create user
        self.find_element(SAVE_BTN).click()
        # verify confirmation message
        self.wait_for_element_visibility(TOAST_MSG)

    def search_user(self, role: str, status: str, user_name: str):
        user_role = ADMIN_ROLE if role == "admin" else ESS_ROLE
        user_status = STATUS_ENABLED if status == "enabled" else STATUS_DISABLED

        self.wait_for_element_invisibility(LOADER)
        # select user role
        self.wait_for_element_clickable(ROLE_DROPDOWN).click()
        self.wait_for_element_visibility(user_role).click()
        # enter user_name
        self.wait_for_element_visibility(USERNAME_INPUT).send_keys(user_name)
        # select user status
        self.wait_for_element(STATUS_DROPDOWN).click()
        self.wait_for_element_visibility(user_status).click()
        # click search
        self.find_element(USER_SEARCH_BTN).click()
        # verify user in search results
        self.wait_for_element_visibility(FOUND_1USER)
        self.wait_for_element_visibility(FOUND_USER(user_name))
        # reset search results and verify first(by default) shown record is Admin
        self.find_element(RESET_SEARCH_BTN).click()
        self.wait_for_element_visibility(FOUND_USER("Admin"))

    def delete_user(self, user_name: str):
        # click delete icon in a row based on username
        self.wait_for_element_visibility(DEL_USER_ROW_BTN(user_name)).click()
        # confirm delete on popup
        self.wait_for_element_visibility(DEL_USER_POPUP_BTN).click()
        # verify deleted confirmation message
        self.wait_for_element_visibility(DEL_TOAST_MSG)

    def get_all_users(self):
        users_text = self.wait_for_elements_visibility(USER_TABLE_CELL)

        user_names = [user.text for user in users_text]

        return user_names
