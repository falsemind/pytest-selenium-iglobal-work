from selenium import webdriver
import pytest
import requests
import json

from socks import method


@pytest.fixture(scope="class")
def browser_driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

# Simple boilerplate code based on documentation: https://api.orangehrm.com/#api-Access_Token-issueToken
# Paid license required, so can't properly implement all API related functionality to get token and actual tests...
# @pytest.fixture(scope="class")
# def orange_crm_auth_headers():
#     url = "https://api-sandbox.orangehrm.com/oauth/issueToken"
#     token = None
#     payload = {
#         "grant_type": "client_credentials",
#         "client_id": "valid client_id",
#         "client_secret": "valid client_secret"
#     }
#
#     try:
#         response = requests.post(url, data=payload)
#         assert response.status_code == 200
#         data = response.json()
#         token = data.get("access_token")
#
#     except Exception as e:
#         print(f"Failed to get auth token: {e}")
#
#     return {
#             "Authorization": f"Bearer {token}",
#             "Content-Type": "application/json"
#         }

@pytest.fixture(scope="class")
def orange_crm_auth_headers():
    # not valid placeholder just for demonstration of the test
    return {
                "Authorization": f"Bearer access_token",
                "Content-Type": "application/json"
            }