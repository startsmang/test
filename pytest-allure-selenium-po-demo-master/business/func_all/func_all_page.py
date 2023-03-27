#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure_risk
# @Time    : 2022/12/3 15:23
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : func_all_page.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------
from selenium.webdriver.common.by import By
class FuncHandleBage():
    # 新闻 hao123 地图 贴吧 视频 图片 网盘 更多 设置 登录
    # 关于句柄 https://blog.csdn.net/weixin_45207460/article/details/121672498
    menu_baidu=(By.XPATH, "//*[@class='mnav c-font-normal c-color-t']")# 百度搜索界面的菜单按钮 # 新闻 hao123 地图 贴吧 视频 图片 网盘 更多 设置 登录

    baidu_search_box=(By.ID, "kw")#百度搜索界面的搜索框
    baidu_search_button=(By.ID,"su")# 百度搜索界面的搜索按钮

    baidu_news_box=(By.ID, "ww")#百度新闻界面的搜索框
    baidu_news_button=(By.ID,"s_btn_wr")# 百度新闻界面的搜索按钮

    baidu_tieba_box=(By.ID, "wd1")#百度贴吧界面的搜索框
    baidu_tieba_button=(By.XPATH, '//*[@class="search_btn_wrap search_btn_enter_ba_wrap"]')# 百度贴吧界面的搜索按钮

class FuncIframeBage():
    iframeResult=(By.XPATH, '//*[@id="iframeResult"]')#iframe对象
    female_button=(By.XPATH,'//*[@value="female"]')#iframe中的 female按钮,

    run_button=(By.XPATH, '//*[@id="tiy_btn_tryit"]/a')#iframe外的运行代码按钮,




