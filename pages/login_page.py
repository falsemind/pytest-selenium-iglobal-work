from pages.base_page import BasePage
from pages.locators import FORM_USERNAME, FORM_PASSWORD, FORM_SUBMIT_BTN, HEADER_TITLE

class LoginPage(BasePage):

    def login_user(self, user_name: str, user_password: str):
        # hardcoded url for simplicity and speed, in real world scenario would be different implementation...
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

        # enter creds and submit
        self.wait_for_element(FORM_USERNAME).send_keys(user_name)
        self.find_element(FORM_PASSWORD).send_keys(user_password)
        self.find_element(FORM_SUBMIT_BTN).click()
        # verify header after login
        self.wait_for_element(HEADER_TITLE)
