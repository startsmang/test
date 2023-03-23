import logging
import time

import allure
import pytest

# 加载对应的路径
from  UI_test.common.parse_xlsx import parse_xlsx
from UI_test.common.parse_yaml import parse_yaml
from UI_test.page.login import Login
from UI_test.config.config import base_path

login_data_path = base_path + parse_yaml("case.path.login")
# 加载数据集
data = parse_xlsx(login_data_path)


@pytest.mark.parametrize(("username", "password", "status"), data)
@allure.feature("用户登录")
class TestLogin:
    def setup(self):
        self.login = Login()

    def teardown(self):
        self.login.quit()

    @allure.story("用户登录1-1")
    def test_01_login(self, username, password, status):
        self.login.login(username, password)
        if status == 1:  # 正常登录
            self.login.login_success_check()
            assert "退出系统" in self.login.driver.page_source
        elif status == 0:  # 用户名或者密码错误
            self.login.login_error_check()
            assert "用户名或者密码错误" in self.login.driver.page_source
        else:
            logging.error(f"传入的status参数的值{status}不正确, 只能是0(用户名或者密码错误)或者1(正常登录)")
            assert False
