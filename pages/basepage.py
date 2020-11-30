from selenium import webdriver
from selenium.webdriver import ChromeOptions


class BasePage(object):


    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://automationpractice.com/index.php?controller=authentication'

    def _close_session(self):
        return self.driver.close()

    def _open_webpage(self):
        return self.driver.get(self.url)

    @property
    def _verify_header(self):
        return self.driver.title

    def _verify_url(self, url):
        return self.driver.current_url == url

    def set_next_page(self, next_page=None) -> object:
        self.__class__ = next_page.__class__
        self.__dict__ = next_page.__dict__
        return next_page
