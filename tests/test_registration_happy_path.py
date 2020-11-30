import pytest
from assertpy import assertpy

from pages.AuthenticationPage import AuthenticationPage
from pages.RegistrationPage import RegistrationPage


class TestRegistrationForm(object):

    @pytest.mark.usefixtures('driver','setup_teardown', )
    def test_register_happy_path(self, driver):
        email = 'some_email@gmail.com'
        register_page_name = 'Create an account'
        assert AuthenticationPage(driver).verify_elements_presence()
        AuthenticationPage(driver).provide_email(email)
        AuthenticationPage(driver).navigate_to_registration_form()
        assert RegistrationPage(driver).verify_page_name() == register_page_name