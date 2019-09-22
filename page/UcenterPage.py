from selenium.webdriver.common.by import By

from common import utils
from common.utils import get_logger
from page.BasePage import BasePage

logg = get_logger(__name__)


class UcenterPage(BasePage):
    # 账户中心
    _ucenter_head_username = (By.CLASS_NAME, "ucenter-head-username")

    # 检测是否登陆成功
    def check_ucenter_username(self, login_iphone):
        ucenter_name = utils.phone(login_iphone)
        self.get_text_to_be_present(self._ucenter_head_username, ucenter_name)
        logg.info("账户中心手机号 %s" % ucenter_name)
