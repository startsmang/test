"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""
获得验证信息
"""
#实例化浏览器驱动
driver = webdriver.Chrome()
#窗口最大话
driver.maximize_window()
#打开百度
driver.get("http://www.baidu.com")

#标题
print(driver.title)
#获取属性值
id = driver.find_element(By.ID,'su')

print(id.get_attribute('value'))

print(id.get_attribute('class'))
print(id.get_attribute('type'))

print(id.get_attribute('id'))
#获取文本信息
xinwen = driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[3]')
print(xinwen.text)
input("...")
driver.quit()