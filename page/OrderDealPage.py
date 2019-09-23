import time

from selenium.webdriver.common.by import By

from common.utils import get_logger
from page.AuctionDetailPage import AuctionDetailPage
from page.BasePage import BasePage

logg = get_logger(__name__)


class OrderDealPage(BasePage):
    # todo  有弹窗，需重新进入集合购买页面 -- 本场竞拍已结束，请等待下一场
    # todo  有弹窗，超出剩余可拍票面金额  -- 无法继续
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
        # 竞买额 输入
        self.clear_and_sendkeys(price, *self._input_tag)
        # 同意服务协议
        self.click_element(*self._check_selected)
        # 确认竞拍
        time.sleep(2)  # 需要sleep两秒，否则"确认竞拍"后，会弹出"超出剩余可拍票面金额"
        self.click_element(*self._deal_submit)

        # 弹窗确认
        message = self.find_element(*self._dialog_message)

        logg.info("message: %s" % message.text)  # 会获取不到text,可忽略
        confirm = self.find_element(*self._dialog_confirm)
        logg.info("confirm.text: %s" % confirm.text)
        # 确认购买
        confirm.click()

        return AuctionDetailPage()
