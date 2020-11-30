from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from utils.helper import check_if_element_visible, wait_and_send_text, wait_and_click

class AuthenticationPage(BasePage):

    url = 'http://automationpractice.com/index.php?controller=authentication'

    def __init__(self, url):
        super().__init__(url)

        self.form_header_title = (By.NAME, "Authentication")
        self.email_header_text = (By.XPATH, """//*[@id="create-account_form"]/div/div[2]/label""")
        self.email_address_input = (By.ID, "email_create")
        self.sumbit_button = (By.ID, "SubmitCreate")

    def verify_elements_poresnece(self) -> bool:
        if check_if_element_visible(self.driver, *self.form_header_title):
            if check_if_element_visible(self.driver, *self.email_address_input):
                return True
        return False

    def provide_email(self, text) -> None:
        return wait_and_send_text(self.driver,*self.email_address_input, text)

    def navigate_to_registration_form(self) -> object:
        wait_and_click(self.driver, *self.sumbit_button)
        self.set_next_page()



