import time

from selenium.webdriver.common.by import By


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 加载对应的url
from UI_test.base.base import BasePage
from UI_test.common.common import open_browser
from UI_test.common.parse_yaml import parse_yaml

login_url = parse_yaml("wms.url.login")


class Login(BasePage):
    # 定义元素位置
    loc_username = (By.ID, "name")
    loc_password = (By.ID, "pwd")
    loc_submit_btn = (By.ID, "login_sub")
    loc_login_error = (By.XPATH, "//span[text()='用户名或者密码错误']")
    loc_login_success = "main"

    def __init__(self):
        driver = open_browser()
        driver.get(login_url)
        super().__init__(driver)

    # 定义业务方法
    def login(self, username, password):
        username_ele = self.get_element(*self.loc_username)
        self.clear(username_ele)
        self.input_text(username_ele, username)
        password_ele = self.get_element(*self.loc_password)
        self.clear(password_ele)
        self.input_text(password_ele, password)
        submit_ele = self.get_element(*self.loc_submit_btn)
        self.click(submit_ele)

    def login_success_check(self):
        self.url_matches(self.loc_login_success)

    def login_error_check(self):
        self.wait_ele_all_presence(self.loc_login_error, doc="用户登录错误验证")
