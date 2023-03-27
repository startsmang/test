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

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

#新闻 hao123 地图 贴吧 视频 图片 网盘 更多 设置 登录
baidu_link=(By.XPATH, "//*[@class='mnav c-font-normal c-color-t']")
#//*[@id="s-top-left"]/a[1]
#//*[@id="s-top-left"]/a[2]
driver.find_element(*baidu_link).click()
print(driver.find_elements(*baidu_link))

driver.find_elements(*baidu_link)[4].click()



input("...")
driver.quit()


