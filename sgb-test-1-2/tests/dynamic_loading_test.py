# filename: test/dynamic_loading_test.py
import pytest
from selenium import webdriver
from pages import dynamic_loading_page

class TestDynamicLoading():

    @pytest.fixture
    def dynamic_loading(self, request):
        _driver = webdriver.Chrome()

        def quit():
            _driver.quit()

        request.addfinalizer(quit)
        return dynamic_loading_page.DynamicLoadingPage(_driver)

    def test_hidden_element(self, dynamic_loading):
        dynamic_loading.load_example("1")
        assert dynamic_loading.finish_text_present()

    def test_rendered_element(self, dynamic_loading):
        dynamic_loading.load_example("2")
        assert dynamic_loading.finish_text_present()
