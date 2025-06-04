from selene import browser
from selenium import webdriver
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.config.window_width = 900
    browser.config.window_height = 1000
    driver_options = webdriver.ChromeOptions()
    driver_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    browser.config.driver_options = driver_options

    yield

    browser.quit()
