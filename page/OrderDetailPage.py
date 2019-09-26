import time

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
        # 页面显示"立即竞拍"按钮，并按钮名称非空
        self.get_text_to_be_present(self._detail_bottombtn_locator, '立即竞拍', cf.auction_interval_time)
        logg.info("立即竞拍 按钮显示")

        if not self.check_van_dialo():
            # 无弹窗
            self.click_element(*self._detail_bottombtn_locator)
            logg.info("点击：立即竞拍")
            return OrderDealPage()

