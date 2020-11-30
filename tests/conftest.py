import pytest
from pages.AuthenticationPage import AuthenticationPage

default_timeout=10

@pytest.fixture(scope='class', autouse=True)
def setup_teardown(driver):
    AuthenticationPage(driver)._open_webpage()
    yield
    AuthenticationPage(driver)._close_session()
