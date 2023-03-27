#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure_risk
# @Time    : 2022/12/3 15:22
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : func_all_bs.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------
from base.base import BasePage
from business.func_all.func_all_page import FuncHandleBage as FIB
from business.func_all.func_all_page import FuncIframeBage as FIFB
from time import sleep
from common.logger import Logger
class Func_All_BS():
    def __init__(self, driver):
        self.driver = BasePage(driver)

    def func_handle_bs(self):
        self.driver.get_url('https://www.baidu.com/')
        menu_baidu_element_data=self.driver.get_elements(FIB.menu_baidu, doc="", mode=2)
        Logger.info(menu_baidu_element_data)
        menu_baidu_elements=menu_baidu_element_data['elements']

        menu_baidu_total=menu_baidu_element_data['total']
        menu_baidu_elements[0].click()
        sleep(3)
        menu_baidu_elements[3].click()
        sleep(5)
        window_handle=self.driver.get_window_handle(mode=2)
        window1=window_handle["window1"]
        all_windows=window_handle["all_windows"]


        self.driver.switch_to_window(handlelist=all_windows,tab_name="百度一下，你就知道",mode=1,doc='切换到百度搜索界面')#handlelist:list,tab_name='',handle='',mode=0,doc='',timewait=0.5
        self.driver.input_text(FIB.baidu_search_box,text='mojin', doc='百度搜索框输入“mojin”' )
        self.driver.click_element(FIB.baidu_search_button,doc='点击搜索')

        self.driver.switch_to_window(handlelist=all_windows,tab_name="百度新闻——海量中文资讯平台",mode=1,doc='切换到百度新闻界面')#handlelist:list,tab_name='',handle='',mode=0,doc='',timewait=0.5
        self.driver.input_text(FIB.baidu_news_box,text='mojin', doc='百度新闻搜索框输入“mojin”' )
        self.driver.click_element(FIB.baidu_news_button,doc='点击搜索')

        self.driver.switch_to_window(handlelist=all_windows,tab_name="百度贴吧——全球领先的中文社区",mode=1,doc='切换到百度贴吧界面')#handlelist:list,tab_name='',handle='',mode=0,doc='',timewait=0.5
        self.driver.input_text(FIB.baidu_tieba_box,text='mojin', doc='百度贴吧搜索框输入“mojin”' )
        self.driver.click_element(FIB.baidu_tieba_button,doc='点击搜索')

        self.driver.switch_to_window(handlelist=all_windows,tab_name="mojin_百度搜索",mode=1,doc='切换到百度搜索界面')#handlelist:list,tab_name='',handle='',mode=0,doc='',timewait=0.5
        self.driver.input_text(FIB.baidu_search_box,text='哈哈', doc='百度搜索框输入“哈哈”' )
        self.driver.click_element(FIB.baidu_search_button,doc='点击搜索')


    def func_iframe_bs(self):
        self.driver.get_url("https://www.w3school.com.cn/tiy/t.asp?f=eg_html_form_radio")
        self.driver.click_element(FIFB.run_button,doc="点击iframe外的运行代码按钮") #iframe外的按钮

        self.driver.switch_iframe(FIFB.iframeResult,doc='切换进入iframe')
        self.driver.click_element(FIFB.female_button,doc="点击选中Female中的female按钮",timewait=1) #iframe里的按钮

        self.driver.switch_parent_iframe(doc="退出当前iframe层")
        self.driver.switch_default_iframe(doc="退出最外层iframe")

        self.driver.click_element(FIFB.run_button,doc="点击iframe外的运行代码按钮") #iframe外的按钮









