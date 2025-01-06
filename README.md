# Homework assignment for InsightGlobal:


>Create a test automation script using Selenium and Python with Pytest as the test automation Framework for the below scenario:
>Login to https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers
           Note: username and password is provided in the login page.
>In the user management(admin/user Management) web page, select the admin menu item.
>   1. Add a test user(ex: testUser1) with Admin role and status as enabled.
>   2. Add a test user(ex: testUser2)  with ESS role and status as disabled.
>Validate if the users got added as expected and are being displayed using the “Search” button.
>Validate if the users info gets cleared when using the “Reset” button
>Delete the test user(ex: testUser2) with the ESS role and validate if the user got deleted in the front end as well as backend using SQL (please use any sample table data for this part of the exercise).
>Retrieve the user records using an API GET request and validate that the records received match with what is displayed on the user management screen. (You may assume what the API will look like, and include your assumption in the readme).
>Add a readme to explain the code execution workflow process and how to run the code locally.
>Please create the above code in the github repository and share the repository information.

## Assumptions:
Based on limited functionality of the free version of orangecrm I can't fully implement API part of work.
So API fixture to get an auth token is based on their documentation and commented out in `conftest.py` and writen as a basic setup for demonstration.
And same applied to API test to compare users shown on the frontend side with API response, which can be inspected in browser's network logs.
Also, there are few other shortcuts here and there for simplicity and speed since this project is not for real world usage.
Currently only thing remaining is SQL part. Because it slightly not clear what kind of tables I have to use, there is nothing in orangecrm I could find, or even what database(e.g. MySGL, PostgreSQL). So for now I skipped the implementation of sql client and test to verify user record deletion from the DB. Could be added later on, once I have an email reply with clarifications...

## How to set up project and run the code locally(assuming this will be done on Mac).
**Required preinstalled dependencies:**
* PyCharm
* Python3
* Git

### Clone the repository to your local machine:
```
git clone git@github.com:falsemind/pytest-selenium-iglobal-work.git
```
### Set Up Virtual Environment in PyCharm:
1. Open cloned project in PyCharm.
2. Go to File > Settings > Project: pytest-selenium-iglobal-work > Python Interpreter.
3. Click the icon > Add Interpreter > New Virtualenv Environment.
4. Choose Python 3 and click OK.

### Install Required Dependencies:
Install dependencies from requirements.txt:
```
pip3 install -r requirements.txt
```
### Running Tests:
Open terminal in PyCharm and run command:
```
pytest -sv tests/test_create_delete_users.py
```
Additional command may be required to run in terminal(Mac/Linux):
```
source venv/bin/activate
```