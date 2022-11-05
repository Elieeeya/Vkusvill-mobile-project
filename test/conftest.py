import allure_commons
import pytest
import config
import time
from selene.support.shared import browser
from selene import support
from appium import webdriver
from dotenv import load_dotenv

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def create_driver():
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )

    return browser
