from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import default_timeout


def wait_and_click(driver, locator, value, timeout=default_timeout) -> None:
    return WebDriverWait(driver, timeout=default_timeout).until \
        (EC.element_to_be_clickable((locator ,value)))


def wait_and_get_text(driver, locator, value, timeout=default_timeout) -> str:
    return WebDriverWait(driver, timeout=default_timeout).until \
        (EC.presence_of_element_located((locator ,value))).text()

def wait_and_send_text(driver, locator, value, text, timeout=default_timeout) -> None:
    return WebDriverWait(driver, timeout=default_timeout).until \
        (EC.presence_of_element_located((locator, value))).send_keys(text)


def check_if_element_visible(driver, locator, value, timeout=default_timeout) -> bool:
    if WebDriverWait(driver, timeout=default_timeout).until \
            (EC.visibility_of_element_located((locator, value))):
        return True
    return False
