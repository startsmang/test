#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure
# @Time    : 2022/11/24 9:35
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 7.1_弹窗处理.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
link_list = driver.find_element(By.XPATH,'//span[text()="设置"]')#  s-usersetting-top
ActionChains(driver).move_to_element(link_list).perform()

# 打开搜索设置
driver.find_element(By.LINK_TEXT,"搜索设置").click()

# 保存设置
driver.find_element(By.XPATH,"//*[text()='保存设置']").click()
time.sleep(2)

# 获取警告框文本
alert_text = driver.switch_to.alert.text
print(alert_text)
# 接受警告框, 相当于点击确定
driver.switch_to.alert.accept()

# 鼠标悬停至“设置”链接
link_list = driver.find_element(By.XPATH,'//span[text()="设置"]')#  s-usersetting-top
ActionChains(driver).move_to_element(link_list).perform()

# 打开搜索设置
driver.find_element(By.LINK_TEXT,"搜索设置").click()


#4.driver.switch_to.alert.send_keys(value) 是一个向弹出框中输入内容的方法 其中value是输入的内容，
# 针对于prompt()弹出框中要输入内容，那么就要用到该方法来模拟输入数据内容

# 关闭警告框, 相当于点击取消
# driver.switch_to.alert.dismiss()
time.sleep(2)
input("...")
driver.quit()
