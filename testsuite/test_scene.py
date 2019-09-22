import pytest

from common import utils
from common.utils import xiao_ding, logg
from conf.config import cf


@pytest.mark.usefixtures('main_page')
class TestScene():
    def test_order_success(self, main_page):
        try:
            login_iphone, login_password = cf.login_name_password
            ucenter_name = utils.phone(login_iphone)

            # 登陆账号，并通过账户中心验证登陆成功
            main_page.gotoLogin() \
                .login(login_iphone, login_password) \
                .gotoUcenter() \
                .check_ucenter_username(ucenter_name)

            # 打开集合详情，进行竞拍,竞拍成功后，确认是否购买成功
            main_page \
                .gotoTestOrderDetail() \
                .gotoOrderDeal() \
                .gotoAuctionDetail(cf.input_price) \
                .test_check_success()
        except Exception as e:
            formatter = '自动化用例执行过程中出现未知异常'
            res = xiao_ding(formatter)
            logg.info("钉钉报警状态：%s, 报警内容：%s" % (res, formatter))
