import pytest
from assertpy import assertpy
from utils.UiUsers import UiUsers, Male_user
from pages.AuthenticationPage import AuthenticationPage
from pages.RegistrationPage import RegistrationPage


class TestRegistrationForm(object):

    @pytest.mark.usefixtures('driver','setup_teardown', )
    def test_register_happy_path(self, driver):

        register_page_name = 'CREATE AN ACCOUNT'
        assert AuthenticationPage(driver).verify_elements_presence()
        AuthenticationPage(driver).provide_email(Male_user.generate_email)
        AuthenticationPage(driver).navigate_to_registration_form()
        assert RegistrationPage(driver).verify_page_name() == register_page_name
        RegistrationPage(driver).provide_user_title(Male_user.gender)
        RegistrationPage(driver).provide_user_first_name(Male_user.name)
        RegistrationPage(driver).provide_user_lastname(Male_user.surname)
        RegistrationPage(driver).provide_user_password(Male_user.passwords)
        RegistrationPage(driver).provide_date_of_birth(Male_user.day_of_birth, Male_user.month_of_birth, Male_user.year_of_birth)
        RegistrationPage(driver).provide_address_name(Male_user.name)
        RegistrationPage(driver).provide_address_last_name(Male_user.surname)
        RegistrationPage(driver).provide_street_address(Male_user.street_address)
        RegistrationPage(driver).provide_city_address(Male_user.city)
        RegistrationPage(driver).provide_postal_code(Male_user.zip_code)
        RegistrationPage(driver).provide_state('53')
        RegistrationPage(driver).select_country()
        RegistrationPage(driver).provide_phone_number(Male_user.phone_number)
        assert RegistrationPage(driver).submit_registration()