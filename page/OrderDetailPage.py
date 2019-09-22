from selenium.webdriver.common.by import By

from common.utils import get_logger
from conf.config import cf
from page.BasePage import BasePage
from page.OrderDealPage import OrderDealPage

logg = get_logger(__name__)


class OrderDetailPage(BasePage):
    # 立即竞拍
    _detail_bottombtn_locator = (By.CLASS_NAME, "detail-bottombtn")

    def gotoOrderDeal(self):
        # todo 您已在本场出价成功，请勿重复出价  -- 需要解决   van-dialog__message
        # todo 本场竞拍已结束，请等待下一场  -- 需要解决   //body[@class='van-overflow-hidden']   van-dialog__message text:本场竞拍已结束，请等待下一场  van-button__text 确认

        self.get_text_to_be_present(self._detail_bottombtn_locator, '立即竞拍', cf.auction_interval_time)
        detail_bottombtn = self.find_element(*self._detail_bottombtn_locator)
        logg.info("拍品详情 页面 竞拍状态: %s" % (detail_bottombtn.text))
        detail_bottombtn.click()
        return OrderDealPage()
