from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from utils.helper import wait_and_get_text, check_if_element_visible, \
    wait_and_click, wait_and_send_text, select_from_dropdown


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.url = 'http://automationpractice.com/index.php?controller=authentication'
        self.page_header = (By.CLASS_NAME, "page-subheading")
        self.radio_men_button = (By.ID, "uniform-id_gender1")
        self.radio_women_button = (By.ID, "uniform-id_gender2")
        self.user_first_name_input = (By.ID, "customer_firstname")
        self.user_last_name_input = (By.ID, "customer_lastname")
        self.user_email_input = (By.ID, "email")
        self.user_password_field = (By.ID, "passwd")
        self.date_of_birth_day = (By.ID, "days")
        self.date_of_birth_month = (By.ID, "months")
        self.date_of_birth_year = (By.ID, "years")
        self.address_first_name_input = (By.ID, "firstname")
        self.address_last_name_input = (By.ID, "lastname")
        self.address_street_input = (By.ID, "address1")
        self.address_city_input = (By.ID, "city")
        self.address_state_list = (By.ID, "id_state")
        self.address_post_code = (By.ID, "postcode")
        self.country_list = (By.ID, "id_country")
        self.phone_number_input = (By.ID, "phone_mobile")
        self.register_submit_button= (By.ID, "submitAccount")



    def _is_page_loaded(self) -> bool:
        if check_if_element_visible(self.driver, *self.page_header):
            return True

    def verify_page_name(self):
        return wait_and_get_text(self.driver, *self.page_header)

    def provide_user_title(self, gender=None):
        if gender == 'male':
            return wait_and_click(self.driver, *self.radio_men_button)
        else:
            return wait_and_click(self.driver, *self.radio_women_button)

    def provide_user_first_name(self, name):
        return wait_and_send_text(self.driver, *self.user_first_name_input, name)

    def provide_user_lastname(self, name):
        return wait_and_send_text(self.driver, *self.user_last_name_input, name)

    def provide_user_password(self, password):
        return wait_and_send_text(self.driver, *self.user_password_field, password)

    def provide_date_of_birth(self, day, month, year):
        select_from_dropdown(self.driver, *self.date_of_birth_day, day)
        select_from_dropdown(self.driver, *self.date_of_birth_month, month)
        select_from_dropdown(self.driver, *self.date_of_birth_year, year)

    def provide_address_name(self, name):
        wait_and_send_text(self.driver, *self.address_first_name_input, name)

    def provide_address_last_name(self, last_name):
        wait_and_send_text(self.driver, *self.address_last_name_input, last_name)

    def provide_street_address(self, street):
        wait_and_send_text(self.driver, *self.address_street_input, street)

    def provide_city_address(self, city):
        wait_and_send_text(self.driver, *self.address_city_input, city)

    def provide_state(self, state):
        select_from_dropdown(self.driver, *self.address_state_list, state)

    def provide_postal_code(self, code):
        wait_and_send_text(self.driver, *self.address_post_code, code)

    def select_country(self):
        select_from_dropdown(self.driver, *self.country_list, '21')

    def provide_phone_number(self, phone_number):
        wait_and_send_text(self.driver, *self.phone_number_input, phone_number)

    def submit_registration(self):
        wait_and_click(self.driver, *self.register_submit_button)
        from pages.MyAccountPage import MyAccountPage
        if MyAccountPage(self.driver)._is_page_loaded():
            return self.set_next_page(MyAccountPage(self.driver))

