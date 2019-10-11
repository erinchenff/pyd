import time

from selenium.webdriver.common.by import By

from common.utils import get_logger
from page.AuctionDetailPage import AuctionDetailPage
from page.BasePage import BasePage

logg = get_logger(__name__)


class OrderDealPage(BasePage):
    # todo  金额不足，需要充值 -- 充值

    # 竞买额 输入
    _input_tag = (By.TAG_NAME, "input")
    # 同意服务协议
    _check_selected = (By.CLASS_NAME, 'check-i')
    # 确认竞拍
    _deal_submit = (By.CLASS_NAME, "rg.deal-bottom-buttons-submit")

    # 弹窗确认  # 超出剩余可拍票面金额
    _dialog_message = (By.CLASS_NAME, "van-dialog__message")
    _dialog_confirm = (By.CLASS_NAME, "van-dialog__confirm")

    def gotoAuctionDetail(self, price):

        if not self.check_van_dialo(): # 无弹窗
            # 竞买额 输入
            self.clear_and_sendkeys(price, *self._input_tag)
            logg.info("竞买额 输入")
        if not self.check_van_dialo():  # 无弹窗
            # 同意服务协议
            self.click_element(*self._check_selected)
            logg.info("同意服务协议")



        # 确认竞拍
        time.sleep(2)  # 需要sleep两秒，否则"确认竞拍"后，会弹出"超出剩余可拍票面金额"
        if not self.check_van_dialo(): # 无弹窗
            self.click_element(*self._deal_submit)
            logg.info("无弹窗，点击购买")



        # 弹窗确认
        message = self.find_element(*self._dialog_message)

        logg.info("message: %s" % message.text)  # 会获取不到text,可忽略
        confirm = self.find_element(*self._dialog_confirm)
        logg.info("确认购买弹窗的confirm.text内容是: %s" % confirm.text)
        # 确认购买
        confirm.click()
        logg.info("点击确认购买")

        # if not self.check_van_dialo():  # 无弹窗 todo  同时点击 确认购买和 已结束的时候，已购买成功。但会跳转首页，中断流程。
        return AuctionDetailPage()
