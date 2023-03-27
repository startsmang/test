#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure
# @Time    : 2022/11/23 17:42
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 163邮箱.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# service = ChromeService(executable_path=ChromeDriverManager().install())  # selenium4.0自动下载驱动
# print("驱动地址：", service.path)
#service=service

import re

driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://sahitest.com/demo/php/fileUpload.htm")




