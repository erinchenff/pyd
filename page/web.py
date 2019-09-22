from conf.config import cf
from page.BasePage import BasePage
from page.MainPage import MainPage


class Web(BasePage):
    @classmethod
    def main_page(cls):
        cls.getClient().open_browser(cf.browser, cf.baseURL)
        return MainPage()

    @classmethod
    def quit(cls):
        cls.driver_quit()

