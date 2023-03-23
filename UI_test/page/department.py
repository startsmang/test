from selenium.webdriver.common.by import By


# 加载对应的url
from UI_test.base.base import BasePage
from UI_test.common.common import open_browser
from UI_test.common.parse_yaml import parse_yaml

main_url = parse_yaml("wms.url.main")


class Department(BasePage):
    # 页面元素定位
    loc_mode_sys = (By.ID, "left_tab2")
    loc_mode_sys_img = (By.ID, "dleft_tab1_1_switch")
    loc_mode_dept_menu = (By.ID, "dleft_tab1_2_span")
    loc_input_name = (By.CSS_SELECTOR, "input[name='name']")
    loc_input_sn = (By.CSS_SELECTOR, "input[name='sn']")

    main_frame = "rightMain"
    loc_add_btn = (By.XPATH, "//div[@id='box_bottom']/input[@value='新增']")
    loc_save_btn = (By.CSS_SELECTOR, "input[value='确定保存']")
    loc_save_tip_btn = (By.CSS_SELECTOR, "button[class='aui_state_highlight']")
    loc_last_btn = (By.CSS_SELECTOR, "input[value='尾页']")

    loc_last_delete_btn = (By.XPATH, "//table[@class='table']/tbody/tr[last()]//a[text()='删除']")

    loc_total_size = (By.XPATH, "//div[@class='ui_flt']//span[1]")

    def __init__(self):
        """
        初始化操作
        1 设置cookie
        2 打开主页面
        3 跳转到主窗口
        """
        driver = open_browser()
        driver.get(main_url)
        cookies = parse_yaml("wms.cookie")
        driver.delete_all_cookies()
        driver.add_cookie(cookies)
        driver.refresh()
        driver.get(main_url)
        super().__init__(driver)

    def switch_to_main_frame(self):
        """
        跳转到主操作页面
        :return:
        """
        ele_mode_sys = self.wait_ele_visible(self.loc_mode_sys, doc="定位系统模块")
        self.click(ele_mode_sys, doc="点击系统管理模块")
        ele_loc_mode_sys_img = self.wait_ele_visible(self.loc_mode_sys_img, doc="定位系统管理模块")
        self.click(ele_loc_mode_sys_img, doc="点击系统管理模块")
        ele_loc_mode_dept_menu = self.wait_ele_visible(self.loc_mode_dept_menu, doc="定位部门管理")
        self.click(ele_loc_mode_dept_menu, doc="点击部门管理模块")
        self.switch_iframe(self.main_frame, doc="跳转到主页面操作窗口")

    def add_dept(self, dept):
        """
        添加部门信息
        :param dept:  元组, 部门数据
        :return:
        """
        ele_add = self.wait_ele_visible(self.loc_add_btn, doc="定位商品新增按钮")
        self.click(ele_add, doc="点击部门新增按钮")
        ele_dept_name = self.wait_ele_visible(self.loc_input_name, doc="定位部门名称")
        self.input_text(ele_dept_name, dept[0], doc="输入部门名称")
        ele_dept_sn = self.wait_ele_visible(self.loc_input_sn, doc="定位部门编码")
        self.input_text(ele_dept_sn, dept[1], doc="输入部门编码")
        ele_save_btn = self.wait_ele_visible(self.loc_save_btn, doc="定位部门保存按钮")
        self.click(ele_save_btn, doc="点击部门确定保存")

    def delete_dept(self):
        """
        删除最后一条部门信息
        :return:
        """
        self.go_to_last()
        ele_lash_delete_btn = self.wait_ele_visible(self.loc_last_delete_btn, doc="定位到部门删除按钮")
        self.click(ele_lash_delete_btn, doc="部门删除操作")

    def go_to_last(self):
        ele_last_btn = self.wait_ele_visible(self.loc_last_btn, doc="定位部门列表尾页按钮")
        self.click(ele_last_btn, doc="点击部门尾页按钮跳转到最后一页")

    def get_total_size(self):
        """
        获取部门页面总记录数
        :return: 总数
        """
        ele_total_size = self.wait_ele_visible(self.loc_total_size, doc="定位页面的总记录数")
        size = self.get_text(ele_total_size, doc="获取部门总记录数")
        return int(size)
