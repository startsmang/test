#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure
# @Time    : 2022/11/23 15:49
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 3-操作功能.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


# 设置浏览器大小为500*500像素





driver.get('https://www.baidu.com/')

#新闻 hao123 地图 贴吧 视频 图片 网盘 更多 设置 登录
baidu_link=(By.XPATH, "//*[@class='mnav c-font-normal c-color-t']")


driver.find_element(*baidu_link).click()

driver.find_elements(*baidu_link)[4].click()
driver.set_window_size(500, 500)

time.sleep(1)

# 刷新浏览器
try:
    driver.refresh()
    print('刷新页面成功')
except Exception as e:
    print('刷新页面失败')

# 打开csdn网页
driver.get('https://www.csdn.net/')
time.sleep(1)

# 后退回百度页面
driver.back()
time.sleep(1)


#前进
time.sleep(2)
driver.forward()
#刷新
driver.refresh()
#获取当前浏览器的URL
print(driver.current_url)
#标题
print(driver.title)
#获取访问地址的源代码
# print(driver.page_source)
#获取所有窗口的所有标签
print(driver.window_handles)
#当前窗口的ID
print(driver.current_window_handle)

# 设置浏览器全屏
driver.maximize_window()

input("...")
driver.quit()