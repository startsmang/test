#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure_risk
# @Time    : 2022/12/3 15:23
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : func_all_assert.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------

from base.base import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from business.func_all.func_all_page import FuncIframeBage as FIFB
import allure,json
class Func_All_Assert():

    def __init__(self, driver):
        self.driver1=driver
        self.driver = BasePage(driver)

    def func_handle_assert(self,expect):
        title_name= self.driver.get_title()
        result = WebDriverWait(self.driver1, 20,0.5).until(EC.title_contains(expect))
        #result=expect in title_name
        self.driver.allure_step_json__screenshot(step_text="断言:{}".format(result),content={"期望":expect,"实际":title_name,"结果":"{}（包含或相等）".format(result),})
        return result

    def func_iframe_assert(self,expect):
        element_text=self.driver.get_text(FIFB.run_button,)
        element_result = WebDriverWait(self.driver1,20, 0.5).until(
            EC.text_to_be_present_in_element(FIFB.run_button, expect), )
        self.driver.allure_step_json__screenshot(step_text="断言:{}".format(element_result),content={"期望":expect,"实际":element_text,"结果":"{}（包含或相等）".format(element_result),})
        return element_text


