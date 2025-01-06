from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))

    def wait_for_element_visibility(self, locator):
        return self._wait.until(ec.visibility_of_element_located(locator))

    def wait_for_elements_visibility(self, locator):
        return self._wait.until(ec.visibility_of_all_elements_located(locator))

    def wait_for_element_invisibility(self, locator):
        return self._wait.until(ec.invisibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self._wait.until(ec.element_to_be_clickable(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

