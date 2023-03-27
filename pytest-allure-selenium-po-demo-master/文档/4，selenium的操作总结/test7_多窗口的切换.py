"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
"""
多窗口切换
有些web页面打开后，会重新打开一个新的窗口，如果想要在新的窗口上操作，
就得先切换窗口。获取窗口的唯一标识用句柄表示，所以只要切换句柄，
就可以在多个页面上操作

driver.current_window_handle:获取当前窗口句柄
driver.window_handles :返回所有窗口的句柄
driver.switch_to.window() :用于切换到相应的窗口

"""
#实例化浏览器驱动
driver = webdriver.Chrome()
#窗口最大话
driver.maximize_window()
#打开百度
driver.get("http://www.baidu.com")

#获取百度搜索窗口句柄
sreach = driver.current_window_handle
print(sreach)
driver.find_element(By.LINK_TEXT,'登录').click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,'立即注册').click()
#获取注册页窗口句柄
sreach1 = driver.current_window_handle
print(sreach1)
#获取当前所有打开的窗口句柄
all_handles = driver.window_handles
print(all_handles)
#句柄从0开始，比如0代表第一个，1代表第二个，-1代表切换到最新的页面
driver.switch_to.window(all_handles[-1])
driver.find_element(By.NAME,'userName').send_keys(534535345)
driver.find_element(By.NAME,'phone').send_keys(34534534)
time.sleep(3)
driver.switch_to.window(all_handles[0])
time.sleep(3)

