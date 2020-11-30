import pytest
from pages.basepage import BasePage
from selenium import webdriver
from selenium.webdriver import ChromeOptions


opts = ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--start-maximized")



@pytest.fixture(scope='class', autouse=True)
def driver():
    return webdriver.Chrome(options=opts)

@pytest.fixture(scope='class', autouse=True)
def setup_teardown(driver):
    BasePage(driver)._open_webpage()
    yield
    BasePage(driver)._close_session()
