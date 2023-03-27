"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
"""
1，键盘操作
"""
#实例化浏览器驱动
driver = webdriver.Chrome()
#窗口最大话
driver.maximize_window()
#打开百度
driver.get("http://www.baidu.com")

driver.find_element(By.ID,'kw').click()
driver.find_element(By.ID,'kw').send_keys('哈哈哈哈哈哈')
#删除键
driver.find_element(By.ID,'kw').send_keys(Keys.BACK_SPACE)
#空格键
driver.find_element(By.ID,'kw').send_keys(Keys.SPACE)
#制表键tab
driver.find_element(By.ID,'kw').send_keys(Keys.TAB)
#回车键
driver.find_element(By.ID,'kw').send_keys(Keys.ENTER)
time.sleep(3)
#全选
driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'a')

input("...")
driver.quit()