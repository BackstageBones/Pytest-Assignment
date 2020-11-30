from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from utils.helper import wait_and_get_text, check_if_element_visible
class RegistrationPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

        self.url = 'http://automationpractice.com/index.php?controller=authentication'
        self.page_header = (By.CLASS_NAME, "page-subheading")


    def _is_page_loaded(self) -> bool:
        if check_if_element_visible(self.driver, *self.page_header):
            return True

    def verify_page_name(self):
        return wait_and_get_text(self.driver, *self.page_header)