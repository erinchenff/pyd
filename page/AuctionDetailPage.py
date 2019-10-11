import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from common.utils import get_logger, xiao_ding
from conf.config import cf
from page.BasePage import BasePage

logg = get_logger(__name__)


class AuctionDetailPage(BasePage):
    # 已成功加入竞拍：我的竞拍
    _success_btns = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]')
    # 竞拍中 第一个
    _myAuction_list = (By.CLASS_NAME, 'myAuction-list-title')
    # 已成交
    _auction_sucess = (By.XPATH, '//*[@id="app"]/div/div[3]/span[2]')

    def test_check_success(self):
        self.get_title_contains('竞拍成功')
        logg.info('竞拍成功!跳转到我的竞拍页面')

        # 我的竞拍
        self.find_element(*self._success_btns).click()  # todo bug: 页面可能有蒙层
        # 竞拍中
        self.find_element(*self._myAuction_list).click()
        # 竞拍详情页面

        value = False
        wait_time = 0
        refresh_time_interval = 30
        logg.info('开始匹配竞拍状态,最长等待等待时间为 %s 秒' % (int(cf.auction_clear_time) + refresh_time_interval))
        while value == False and wait_time <= cf.auction_clear_time:
            time.sleep(refresh_time_interval)
            value = EC.text_to_be_present_in_element(self._auction_sucess, '已成交')(self.driver)  # todo bug:此时截图为灰色，没有此元素
            self.driver.refresh()
            wait_time += refresh_time_interval
            logg.info('每隔%s秒刷新获取竞选状态，已等待%s秒' % (refresh_time_interval, wait_time))
        if value:
            logg.info('已成交!!!')
        else:
            formatter = "自动化测试用例执行：购买成功后，等待 %s 秒后，未成交" % (cf.auction_clear_time)
            self.get_windows_img()
            res = xiao_ding(formatter)
            logg.info("钉钉报警状态：%s, 报警内容：%s" % (res,formatter))

