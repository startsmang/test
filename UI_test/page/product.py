import time

from selenium.webdriver.common.by import By

# 加载对应的url
from selenium.webdriver.remote.webelement import WebElement

from UI_test.base.base import BasePage
from UI_test.common.common import open_browser
from UI_test.common.parse_yaml import parse_yaml

main_url = parse_yaml("wms.url.main")


class Product(BasePage):
    # 定义基本的元素定位
    loc_mode_biz = (By.ID, "dleft_tab1_1_switch")  # 业务模块
    loc_product_menu = (By.XPATH, "//span[text()='商品管理']")  # 商品管理模块
    main_frame = "rightMain"
    loc_add_btn = (By.XPATH, "//div[@id='box_bottom']/input[@value='新增']")
    loc_save_btn = (By.CSS_SELECTOR, "input[value='确定保存']")
    loc_save_tip_btn = (By.CSS_SELECTOR, "button[class='aui_state_highlight']")
    loc_last_btn = (By.CSS_SELECTOR, "input[value='尾页']")

    loc_input_sn = (By.CSS_SELECTOR, "input[name='sn']")
    loc_input_name = (By.CSS_SELECTOR, "input[name='name']")
    loc_input_costPrice = (By.CSS_SELECTOR, "input[name='costPrice']")
    loc_input_salePrice = (By.CSS_SELECTOR, "input[name='salePrice']")
    loc_input_brandId = (By.CSS_SELECTOR, "select[name='brandId']")
    loc_input_pic = (By.CSS_SELECTOR, "input[name='pic']")
    loc_input_intro = (By.CSS_SELECTOR, "textarea[name='intro']")

    loc_last_delete_btn = (By.XPATH, "//table[@class='table']/tbody/tr[last()]//a[text()='删除']")
    loc_delete_ok_btn = (By.XPATH, "//table[@class='aui_dialog']//button[text()='确定']")
    loc_delete_tip_btn = (By.XPATH, "//table[@class='aui_dialog']//button[text()='确定']")

    loc_total_size = (By.XPATH, "//div[@class='ui_flt']//span[1]")

    def __init__(self):
        """
        初始化浏览器的基本操作
        并且设置对应的cookie
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
        ele_mode_biz = self.wait_ele_visible(self.loc_mode_biz, doc="定位业务处理模块")
        self.click(ele_mode_biz, doc="点击业务处理模块")
        ele_product_menu = self.wait_ele_visible(self.loc_product_menu, doc="定位商品管理菜单")
        self.click(ele_product_menu, doc="点击商品管理菜单")
        self.switch_iframe(self.main_frame, doc="跳转到主页面操作窗口")

    def add_product(self, product):
        ele_add = self.wait_ele_visible(self.loc_add_btn, doc="定位商品新增按钮")
        self.click(ele_add, doc="点击商品新增按钮")
        ele_input_sn = self.wait_ele_visible(self.loc_input_sn, doc="定位编号输入")
        self.input_text(ele_input_sn, product[0], doc="输入商品编号")
        ele_input_name = self.wait_ele_visible(self.loc_input_name, doc="定位商品名称")
        self.input_text(ele_input_name, product[1], doc="输入商品名称")
        ele_input_cost_price = self.wait_ele_visible(self.loc_input_costPrice, doc="定位商品成本价格")
        self.input_text(ele_input_cost_price, product[2], doc="输入商品成本价格")
        ele_input_sale_price = self.wait_ele_visible(self.loc_input_salePrice, doc="定位商品销售价格")
        self.input_text(ele_input_sale_price, product[3], doc="输入商品销售价格")
        ele_input_brand = self.wait_ele_visible(self.loc_input_brandId, doc="定位商品品牌")
        self.select_by_value(ele_input_brand, product[4], doc="选择商品品牌")
        # 商品图片需要选择一个具体路径
        # ele_input_pic = self.wait_ele_visible(self.loc_input_pic, doc="定位商品图片")
        # self.input_text(ele_input_pic, product[5], doc="选择商品图片")
        ele_input_intro = self.wait_ele_visible(self.loc_input_intro, doc="定位商品描述")
        self.input_text(ele_input_intro, product[6], doc="输入商品描述")
        ele_save_btn = self.wait_ele_visible(self.loc_save_btn, doc="定位商品保存按钮")
        self.click(ele_save_btn, doc="点击商品保存按钮")
        ele_save_tip_btn = self.wait_ele_visible(self.loc_save_tip_btn, doc="定位商品保存提示按钮")
        self.click(ele_save_tip_btn)

    def delete_product(self):
        """
        删除最后一条商品信息
        :return:
        """
        self.go_to_last()
        ele_lash_delete_btn = self.wait_ele_visible(self.loc_last_delete_btn, doc="定位到商品删除按钮")
        self.click(ele_lash_delete_btn, doc="商品删除操作")

        ele_delete_ok_btn = self.wait_ele_visible(self.loc_delete_ok_btn, doc="定位商品删除确认按钮")
        self.click(ele_delete_ok_btn, doc="点击商品删除确认按钮")

        ele_delete_tip_btn = self.wait_ele_visible(self.loc_delete_tip_btn, doc="定位商品删除提示按钮")
        self.click(ele_delete_tip_btn, doc="点击商品删除提示按钮")

    def go_to_last(self):
        # 滚动滚动条到最后面
        js = "window.scrollTo(0,window.outerHeight)"
        self.execute_js(js)
        ele_last_btn = self.wait_ele_visible(self.loc_last_btn, doc="定位商品列表尾页按钮")
        self.click(ele_last_btn, doc="点击尾页按钮跳转到最后一页")

    def get_total_size(self):
        """
        获取商品页面总记录数
        :return: 商品总数
        """
        ele_total_size = self.wait_ele_visible(self.loc_total_size, doc="定位页面的总记录数")
        size = self.get_text(ele_total_size, doc="获取商品总记录数")
        return int(size)
