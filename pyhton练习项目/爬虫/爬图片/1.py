# @Author : 王同学
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait   # 显示等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains     # 动作链
import time
import re
import requests
import os.path
import csv



driver = webdriver.Chrome() # 创建浏览器对象

wait = WebDriverWait(driver,10)

driver.get(url='http://www.xiannvku.cc/pic/show-21201-1.html')
def get_conten(url):
    driver.get(url) # 对网页发送请求
    time.sleep(1)
    mood = wait.until(EC.presence_of_element_located((By.ID,'pcheaderbq'))) # 找到热门表情包点击
    mood.click()    # 找到热门表情包点击
    time.sleep(1)
    chains = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="bqb"]/div[3]/a[8]')))    # 移动到页面末尾，加载元素
    ActionChains(driver).move_to_element(chains).perform()  # 开始移动
    time.sleep(3)