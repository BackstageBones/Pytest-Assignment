from selenium import webdriver
from selenium.webdriver import ChromeOptions
from tests.conftest import default_timeout
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    opts.add_argument("--start-maximized")

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(options=BasePage.opts)
        self._open_webpage()

    def _close_session(self):
        return self.driver.close()

    def _open_webpage(self):
        return self.driver.get(self.url)

    @property
    def _verify_header(self):
        return self.driver.title

    def _verify_url(self):
        return self.driver.current_url == self.url

    def set_next_page(self,  next_page=None) -> object:
        self.__class__ = next_page.__class__
        self.__dict__ = next_page.__dict__
        return next_page
