from selenium.webdriver.common.by import By

from common.utils import get_logger
from conf.config import cf
from page.BasePage import BasePage
from page.LoginPage import LoginPage
from page.OrderDetailPage import OrderDetailPage
from page.UcenterPage import UcenterPage

logg = get_logger(__name__)

class MainPage(BasePage):
    # 底部'我的'
    _my_btn = (By.XPATH, '//*[contains(@class,"bottom-item")][2]')

    # 登陆
    def gotoLogin(self):
        self.find_element(*self._my_btn).click()
        logg.info('点击我的，跳转登陆页面')
        return LoginPage()

    # 账户中心
    def gotoUcenter(self):
        self.find_element(*self._my_btn).click()
        return UcenterPage()

    # 购买指定测试集合
    def gotoTestOrderDetail(self):
        self.driver.get(cf.set_url)
        return OrderDetailPage()
