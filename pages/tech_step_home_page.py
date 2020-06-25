from basepage import BasePage, BaseElement

class TechStepHomePage(BasePage):

    url = 'https://techstepacademy.com/'

    def __init__(self, url):
        self.url = url
        super().__init__(url)
        self._verify_url()