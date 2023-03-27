#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure_risk
# @Time    : 2022/12/5 14:30
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : te_001.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# service = ChromeService(executable_path=ChromeDriverManager().install())  # selenium4.0自动下载驱动
# print("驱动地址：", service.path)
#service=service
driver = webdriver.Chrome()  # 初始化driver

driver.implicitly_wait(25)  # 隐式等待


url = "https://2342342342342/234234/#/projectList/m"
driver.get(url)  # 打开浏览器地址

# 浏览器中F12 接口请求中获取cookie信息
cookie_dic = {

    "Admin-Token": "183920n_token_1670202680e3aiv57306lor5bw4p51",
    'Admin-UserInfo':'{%22address%22:22birthday%22:null%2C%22card_type%22:null%2C%22check_project_id_key%22:1%2C%22city%22:null%2C%22company%22:%22%E6%B5%8E%E7%9B%AE%E7%A7%91%E6%8A%80%22%2C%22company_job%22:%22%E6%B5%8E%E7%9B%AE%E7%A7%91%E6%8A%80%22%2C%22create_time%22:1667448852%2C%22email%22:%22178999718@qq.com%22%2C%22in_use%22:1%2C%22load_name%22:%2218392041218%22%2C%22login_code%22:%22ar_help/kick_out/18392041218202212050911202465093453525312%22%2C%22member_id%22:85%2C%22member_type%22:1%2C%22nation%22:null%2C%22nick_name%22:%22%E9%BB%84%E9%B9%8F1218%E9%BB%84%E9%B9%8F%22%2C%22person_pic%22:null%2C%22phone%22:%2218392041218%22%2C%22pic_path%22:null%2C%22picpath%22:null%2C%22province%22:null%2C%22qq%22:null%2C%22real_name%22:%22%E9%BB%84%E9%B9%8F%22%2C%22sex%22:%221%22%2C%22source_type%22:1%2C%22tel%22:null%2C%22token%22:%2218392041218_login_token_1670202680e3aiv57306lor5bw4p51%22}',
    'sidebarStatus':'0'

}

for k, v in cookie_dic.items():  # 添加cookie
    print(k, v)
    driver.add_cookie({
        'name': k,
        'value': str(v)
    })
print('添加cookie')

driver.get(url)  # 打开浏览器地址
driver.maximize_window()
# 刷新浏览器
try:
    driver.refresh()
    print('刷新页面成功')
except Exception as e:
    print('刷新页面失败')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@class="infoBox"]/div[2]/div/div[2]').click()
#driver.get('https://34634535345345345/risk_sys/#/personBase/index')  # 打开浏览器地址
driver.find_element(By.ID,'hamburger-container').click()
driver.find_element(By.XPATH,  '//span[text()="资料管理"]').click()
driver.find_element(By.XPATH,"//*[@class='el-col el-col-24']/button").click()
time.sleep(2)
ti=r'F:\2d4d396b185521eaf2e5a8b532f573dc.png'
# driver.find_element(By.XPATH,"//*[@class='updatainput']").click()

ActionChains(driver).click(driver.find_element(By.XPATH,"//*[@class='updatainput']")).perform()

#driver.find_element(By.XPATH,"//*[@class='updatainput']").send_keys(ti)


input("...")

driver.close()
