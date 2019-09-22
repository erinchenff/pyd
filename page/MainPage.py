from selenium.webdriver.common.by import By

from conf.config import cf
from page.BasePage import BasePage
from page.LoginPage import LoginPage
from page.OrderDetailPage import OrderDetailPage
from page.UcenterPage import UcenterPage


class MainPage(BasePage):
    # 底部'我的'
    _my_btn = (By.CLASS_NAME, 'bottom-item4')

    # 登陆
    def gotoLogin(self):
        self.find_element(*self._my_btn).click()
        return LoginPage()

    # 账户中心
    def gotoUcenter(self):
        self.find_element(*self._my_btn).click()
        return UcenterPage()

    # 购买指定测试集合
    def gotoTestOrderDetail(self):
        self.driver.get(cf.set_url)
        return OrderDetailPage()
