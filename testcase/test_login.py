import pytest

from conf.config import cf

@pytest.mark.usefixtures('main_page')
class TestLogin:

    @pytest.mark.parametrize("login_iphone,login_password", [cf.login_name_password])
    def test_login_password(self, login_iphone, login_password, main_page):
        main_page.gotoLogin().login(login_iphone, login_password)
