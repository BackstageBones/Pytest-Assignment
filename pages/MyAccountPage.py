from pages.basepage import BasePage
from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from utils.helper import wait_and_get_text, check_if_element_visible, \
    wait_and_click, wait_and_send_text, select_from_dropdown


class MyAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.url = 'http://automationpractice.com/index.php?controller=my-account'
        self.confirmation_text = (By.CLASS_NAME, 'info-account')
        self.page_header = (By.CLASS_NAME, 'page-heading')

    def _is_page_loaded(self):
        if check_if_element_visible(self.driver, *self.confirmation_text):
            if check_if_element_visible(self.driver, *self.page_header):
                return True
        return False