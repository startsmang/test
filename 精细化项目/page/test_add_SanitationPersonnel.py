
# -*- coding: utf-8 -*-
# @Time : 2023/3/24 16:04
# @Author : 廖声琪
# @Site :
# @File : test_login.py
# @Software: PyCharm
# @Description: 登录测试用例


from selenium import webdriver
import  pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait   # 显示等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains     # 动作链
from selenium.webdriver.support.select import Select
from time import sleep
driver = webdriver.Chrome()
# driver.implicitly_wait(10)
def test_openbrowser():
    driver.get('https://jxh.zx1026.com/')
    driver.maximize_window()
def test_login():
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/button[1]').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/div[1]/div/div[1]/input').send_keys('admin')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/div[2]/div/div/input').send_keys('FJzx@2019.')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/button').click()
    sleep(3)
    name = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[5]/span').text
    assert '超级管理员' in name
# def test_chengGuan():  # 进入城管公众问题上报页面
#     driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]').click()
#     sleep(1)
#     driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[6]/div[1]/div[2]/div[2]/div').click()
#     sleep(1)
#     text = driver.find_element(By.XPATH,'//*[@id="breadcrumb-container"]/span/span[2]/span[1]/span').text
#     assert '问题汇总' in text  #对问题汇总进行断言
#
# def test_delete_workOrder():  # 删除工单
#     driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div/div[4]/div/div[5]/div[2]/table/tbody/tr[2]/td[17]/div/div/span[2]').click()
#     sleep(1)
#     driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/button[2]/span').click()
#     sleep(1)
#     assert '删除成功' in driver.page_source    #对删除成功进行断言
def test_sanitationPersonnel():
    # 点击全部应用
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]').click()
    sleep(1)
    # 点击环卫数据库
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[6]/div[1]/div[2]/div[1]/div').click()
    sleep(5)
    # 点击环卫人员管理
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[4]/li/div').click()
    sleep(1)
    # 点击作业人员管理
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[4]/li/ul/div[2]/a/li/span').click()
    sleep(1)
    # 点击新增作业人员
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[2]/div[1]/div[1]/div/div/button').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[1]/div/div/div/input').send_keys('测试')
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[2]/div/div/div/input').send_keys('测试')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[3]/div/div/div/input').send_keys('19978787878')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[4]/div/div/div/input').send_keys('123456')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[5]/div/div/div/div/input').click()
    sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[6]/div/div/div/div/input').click()
    sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[7]/div/div/div/input').send_keys('430482200004124312')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[8]/div/div/div/input').send_keys('测试')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[9]/div/div/div/input').send_keys('湖南省')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[10]/div/div/div/div[1]/input').click()
    sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[11]/div/div/div/div/input').click()
    sleep(0.5)
    driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/button[1]/span').click()
# def test_quit():
#     driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[5]/div[3]/div/img').click()
#     sleep(1)
#     driver.find_element(By.CSS_SELECTOR,'#dropdown-menu-1283 > li:nth-child(2) > span').click()
#     sleep(1)
#     tittle = driver.find_element(By.XPATH,'//*[@id="app"]/div/section[2]/p[1]').text
#     assert '福城管' in tittle
if __name__ == '__main__':
    pytest.main(['--vs'])


