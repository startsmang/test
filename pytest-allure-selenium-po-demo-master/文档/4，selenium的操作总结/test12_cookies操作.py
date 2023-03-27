"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui
"""
driver.add_cookie() #添加cookie信息
driver.get_cookie('a')  #获取指定的name的值为a的cookie信息
driver.get_cookies()    #获取所有cookie
driver.delete_all_cookies()  #删除所有cookie
driver.delete_cookie()   #删除指定的name的值为a的cookie信息

"""
driver = webdriver.Chrome()
driver.get(r"https://www.taobao.com/")

driver.maximize_window()
cook1 = driver.get_cookies()
print("获取所有cookies:",cook1)

cook1 = driver.get_cookie('cna')
print("获取name为cna的cookies:",cook1)

# driver.delete_all_cookies()
# cook2 = driver.get_cookies()
# print("获取所有cookies:",cook2)

driver.delete_cookie('cna')
cook2 = driver.get_cookies()
print("获取所有cookies:",cook2)
