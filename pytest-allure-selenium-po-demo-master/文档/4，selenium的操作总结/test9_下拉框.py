"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""
三种：

select_by_index(): 索引定位（从0开始）
select_by_value():value属性定位
select_by_visible_text():选项的文本属性

"""
driver = webdriver.Chrome()
driver.get(r"a.html")
time.sleep(3)
opt = driver.find_element(By.NAME,"234")
Select(opt).select_by_visible_text("大大。")
time.sleep(3)
Select(opt).select_by_index(2)
time.sleep(3)
Select(opt).select_by_value("04")
