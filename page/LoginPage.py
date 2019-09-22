from selenium.webdriver.common.by import By

from page.BasePage import BasePage


class LoginPage(BasePage):
    _my_btn = (By.CLASS_NAME, 'bottom-item4')
    _iphone = (By.ID, "iphone")
    _password = (By.ID, "pass")
    _login_btn = (By.CLASS_NAME, "go-login-btn")

    def login(self, login_iphone, login_password):
        from page.MainPage import MainPage
        # 账号 密码
        self.clear_and_sendkeys(login_iphone, *self._iphone)
        self.clear_and_sendkeys(login_password, *self._password)
        # 点击登陆
        self.click_element(*self._login_btn)

        return MainPage()

    def register(self):
        pass

    def forget(self):
        pass
