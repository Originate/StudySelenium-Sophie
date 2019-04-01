# filename: tests/login_test.py
import pytest
from selenium import webdriver
from pages import login_page

class TestLogin():

    @pytest.fixture
    def login(self, request):
        _driver = webdriver.Chrome()

        def quit():
            _driver.quit()

        request.addfinalizer(quit)

        return login_page.LoginPage(_driver)

    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        assert login.success_message_present()

    def test_invalid_credentials(self, login):
        login.with_("tomosmith", "bad password")
        assert login.failure_message_present()
