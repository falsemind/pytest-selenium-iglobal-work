import pytest
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from random import randint
import requests

class TestCreateDeleteUsers:
    # for simplicity and speed these vars hardcoded in test suite
    # in real world implementation would different in different directories with data objects
    # and password stored and retrieved via api from secret storage like hashicorp vault, aws secrets manager, etc...
    login_user_name = "Admin"
    login_user_password = "admin123"
    test_user1 = f"test{randint(1, 500)}User1"
    test_user2 = f"test{randint(1, 500)}User2"
    user_names = None

    @pytest.mark.run(order=1)
    def test_login_user(self, browser_driver):
        login_page = LoginPage(browser_driver)
        login_page.login_user(self.login_user_name, self.login_user_password)

    @pytest.mark.run(order=2)
    def test_create_admin_user(self, browser_driver):
        login_page = UserManagementPage(browser_driver)
        login_page.create_user(role="admin", status="enabled", user_name=self.test_user1,
                               user_password=self.login_user_password)

    @pytest.mark.run(order=3)
    def test_search_admin_user(self, browser_driver):
        manage_page = UserManagementPage(browser_driver)
        manage_page.search_user(role="admin", status="enabled", user_name=self.test_user1)

    @pytest.mark.run(order=4)
    def test_create_ess_user(self, browser_driver):
        manage_page = UserManagementPage(browser_driver)
        manage_page.create_user(role="ess", status="disabled", user_name=self.test_user2,
                               user_password=self.login_user_password)

        self.user_names = manage_page.get_all_users()

    @pytest.mark.run(order=5)
    def test_search_ess_user(self, browser_driver):
        manage_page = UserManagementPage(browser_driver)
        manage_page.search_user(role="ess", status="disabled", user_name=self.test_user2)

    @pytest.mark.run(order=6)
    def test_delete_ess_user(self, browser_driver):
        manage_page = UserManagementPage(browser_driver)
        manage_page.delete_user(user_name=self.test_user2)

    @pytest.mark.xfail(reason="Failing test, implemented on assumptions due to no access to paid license")
    @pytest.mark.run(order=7)
    def test_verify_frontend_users_with_api(self, orange_crm_auth_headers):
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users"
        params = {
            "limit": 50,
            "offset": 0,
            "sortField": "u.userName",
            "sortOrder": "ASC"
        }
        response = requests.get(url, params=params, headers=orange_crm_auth_headers)
        assert response.status_code == 200
        assert response.json() is not None

        resp_users = [user["userName"] for user in response.json()["data"]]

        assert resp_users == self.user_names
