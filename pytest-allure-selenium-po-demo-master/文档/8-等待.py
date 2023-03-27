#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure
# @Time    : 2022/11/23 17:09
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 8-等待.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------
# until是当某元素出现或什么条件成立则继续执行
# https://blog.csdn.net/m0_66887922/article/details/124060624
# until_not是当某元素消失或什么条件不成立则继续执行，参数也相同。
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 

from selenium.webdriver.common.by import By
from urllib3.util import timeout

driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待

time.sleep(2) #强制等待

WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator)) #显式等待