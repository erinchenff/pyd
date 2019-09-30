from selenium.webdriver.common.by import By

from common.utils import get_logger
from page.BasePage import BasePage

logg = get_logger(__name__)


class LoginPage(BasePage):
    _iphone = (By.ID, "iphone")
    _password = (By.ID, "pass")
    _login_btn = (By.CLASS_NAME, "go-login-btn")

    def login(self, login_iphone, login_password):
        from page.MainPage import MainPage
        # 账号 密码
        self.clear_and_sendkeys(login_iphone, *self._iphone)
        self.clear_and_sendkeys(login_password, *self._password)
        logg.info("输入手机号是:%s 和密码，登陆" % login_iphone)
        # 点击登陆
        self.click_element(*self._login_btn)
        logg.info("点击登陆按钮")

        return MainPage()

    def register(self):
        pass

    def forget(self):
        pass
