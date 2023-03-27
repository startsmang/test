"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
"""
1，鼠标事件
ActionChains(driver):
    driver： webdriver实例执行用户操作
    ActionChains：ActionChains用于生产用户的行为，所有的行为都存储在ActionChains对象上，
    再通过perform()执行所有ActionChains中存储的行为。


"""
#实例化浏览器驱动
driver = webdriver.Chrome()
#窗口最大话
driver.maximize_window()
#打开百度
driver.get("http://www.baidu.com")
# driver.find_element_by_id('kw').click()
driver.find_element(By.ID,'kw').send_keys("哈哈")
# driver.find_element_by_id('su').click()
sleep(2)

#右击
ele = driver.find_element(By.ID,'kw')
ActionChains(driver).context_click(ele).perform()
sleep(2)
#双击
ele = driver.find_element(By.ID,'kw')
ActionChains(driver).double_click(ele).perform()
sleep(2)
#鼠标悬浮在一个元素上
ele = driver.find_element(By.ID,'kw')
ActionChains(driver).move_to_element(ele).perform()
sleep(2)
#按下鼠标左键在一个元素上不松开
ele = driver.find_element(By.ID,'kw')
ActionChains(driver).click_and_hold(ele).perform()
sleep(2)
# searchButtonJS = "document.getElementById('su').click()"
# driver.execute_script(searchButtonJS)

input("...")
driver.quit()