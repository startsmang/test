"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui
"""
"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

driver.find_element(By.ID,'kw').send_keys('哈哈')

# #1,返回js元素的value的值
value = driver.execute_script("return document.getElementById('su').value")
print("su的值",value)
#
#2、修改的值，并且返回
value = driver.execute_script("return document.getElementById('su').value='测试之道'")
print("修改后su的值",value)

#3、定位元素
# document.getElementById('su')
# document.getElementByName('su')
# document.getElementByClassName('su')
# document.getElementByTag('su')
daozhang_click = "document.getElementById('su').click()"
driver.execute_script(daozhang_click)


#4、页面滚动
#滚动到顶部
# document.documentElement.scrollTop=0
#滚动到底部
# document.documentElement.scrollTop=10000

time.sleep(3)
#滚动到底部
dibu = "document.documentElement.scrollTop=10000"
driver.execute_script(dibu)


time.sleep(3)
#滚动到顶部
dibu = "document.documentElement.scrollTop=0"
driver.execute_script(dibu)