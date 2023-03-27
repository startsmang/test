#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure
# @Time    : 2022/11/23 15:08
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 7-切换句柄.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

element = driver.find_elements(By.XPATH, "//*[@class='mnav c-font-normal c-color-t']")
print(len(element))
print((element))
element[0].click()
time.sleep(3)
element[3].click()
time.sleep(5)

handles_all=driver.window_handles #获取浏览器所以窗口句柄
print(handles_all)

for handle in handles_all:
    driver.switch_to.window(handle) #切换句柄
    if (driver.title)=="百度一下，你就知道":
        print(driver.title)
        current_handle=driver.current_window_handle #获取浏览器当前句柄
        print(current_handle)
        driver.find_element(By.ID,"kw").send_keys('mojin')
        driver.find_element(By.ID,"su").click()
        time.sleep(3)
        break



#新闻 hao123 地图 贴吧 视频 图片 网盘 更多 设置 登录
#关于句柄 https://blog.csdn.net/weixin_45207460/article/details/121672498



for handle in handles_all:
    driver.switch_to.window(handle) #切换句柄

    if (driver.title)=="百度新闻——海量中文资讯平台":
        print(driver.title)
        current_handle=driver.current_window_handle #获取浏览器当前句柄
        print(current_handle)

        driver.find_element(By.ID,"ww").send_keys('mojin')
        driver.find_element(By.ID,"s_btn_wr").click()
        time.sleep(1)
        break



for handle in handles_all:
    driver.switch_to.window(handle) #切换句柄
    if (driver.title)=="百度贴吧——全球领先的中文社区":
        print(driver.title)
        current_handle=driver.current_window_handle #获取浏览器当前句柄
        print(current_handle)
        driver.find_element(By.ID,"wd1").send_keys('mojin')
        driver.find_element(By.XPATH,'//*[@class="search_btn_wrap search_btn_enter_ba_wrap"]').click()
        time.sleep(1)
        break

for handle in handles_all:
    driver.switch_to.window(handle) #切换句柄
    if (driver.title)=="mojin_百度搜索":
        print(driver.title)
        current_handle=driver.current_window_handle #获取浏览器当前句柄
        print(current_handle)
        driver.find_element(By.ID,"kw").send_keys('哈哈')
        driver.find_element(By.ID,"su").click()
        break


#
input("...")
driver.quit()



