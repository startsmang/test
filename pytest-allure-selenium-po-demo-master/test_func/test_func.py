#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure_risk
# @Time    : 2022/12/3 15:00
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : test_func.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------
from business.func_all.func_all_bs import Func_All_BS as FAB
from business.func_all.func_all_assert import Func_All_Assert as FAA
from common.logger import Logger
import pytest,allure

@allure.epic("selenium功能")  # 项目名称

class TestFunc():#
    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('句柄切换')  # 二级标签 二级标签_测试模块
    @allure.title("百度搜索新闻句柄切换")# 三级标签 用例名称@
    @allure.step('百度搜索新闻句柄切换')
    @allure.severity('blocker')#等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_handle(self,driver1):

        FAB(driver1).func_handle_bs()
        expect="mojin哈哈"
        assert FAA(driver1).func_handle_assert(expect)

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('iframe切换')  # 二级标签 二级标签_测试模块
    @allure.title("iframe切换后操作")# 三级标签 用例名称@
    @allure.step('iframe切换后操作')
    @allure.severity('blocker')#等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_iframe(self,driver1):

        FAB(driver1).func_iframe_bs()
        expect="运行代码"
        assert FAA(driver1).func_iframe_assert(expect)

