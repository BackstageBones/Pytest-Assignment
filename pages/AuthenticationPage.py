from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from utils.helper import check_if_element_visible, wait_and_send_text, wait_and_click


class AuthenticationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.form_header_title = (By.CLASS_NAME, "page-heading")
        self.email_header_text = (By.XPATH, """//*[@id="create-account_form"]/div/div[2]/label""")
        self.email_address_input = (By.ID, "email_create")
        self.submit_button = (By.ID, "SubmitCreate")

    def verify_elements_presence(self) -> bool:
        if check_if_element_visible(self.driver, *self.form_header_title):
            if check_if_element_visible(self.driver, *self.email_address_input):
                return True
        return False

    def provide_email(self, text) -> None:
        return wait_and_send_text(self.driver, *self.email_address_input, text)

    def navigate_to_registration_form(self) -> object:
        wait_and_click(self.driver, *self.submit_button)
        from pages.RegistrationPage import RegistrationPage
        if RegistrationPage(self.driver)._is_page_loaded():
            return self.set_next_page(RegistrationPage(self.driver))
