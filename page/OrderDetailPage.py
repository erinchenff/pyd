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
    _dialog = (By.XPATH, '//div[@role="dialog"]')

    def gotoOrderDeal(self):
        # 页面显示"立即竞拍"按钮，并按钮名称非空
        self.get_text_to_be_present(self._detail_bottombtn_locator, '立即竞拍', cf.auction_interval_time)

        if not self.check_van_dialo(self._dialog):
            # 无弹窗
            detail_bottombtn = self.find_element(*self._detail_bottombtn_locator)
            logg.info("拍品详情 页面 竞拍状态: %s" % (detail_bottombtn.text))
            detail_bottombtn.click()
            return OrderDealPage()
        else:
            logg.info("拍品详情 有弹窗，需重新进入集合购买页面")
            # 您已在本场出价成功，请勿重复出价  本场竞拍已结束，请等待下一场
            # todo 拍品详情 有弹窗，需重新进入集合购买页面
