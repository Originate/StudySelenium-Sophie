# filename: pages/dynamic_loading_page.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage

class DynamicLoadingPage(BasePage):
    _start_button = {"by": By.CSS_SELECTOR, "value": "#start button"}
    _finish_text = {"by": By.ID, "value": "finish"}

    def __init__(self, driver):
        self.driver = driver

    def load_example(self, example_number):
        self._visit("http://the-internet.herokuapp.com/dynamic_loading/" + example_number)
        self._click(self._start_button)

    def finish_text_present(self):
        return self._wait_for_is_displayed(self._finish_text, 10)

    def _wait_for_is_displayed(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located((locator['by'], locator['value']))
            )
        except TimeoutException:
            return False

        return True
