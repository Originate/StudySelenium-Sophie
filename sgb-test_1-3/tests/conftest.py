# filename: tests/conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    _driver = webdriver.Chrome()

    def quit():
        _driver.quit()

    request.addfinalizer(quit)
    return _driver
