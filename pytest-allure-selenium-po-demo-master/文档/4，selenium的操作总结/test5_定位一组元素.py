"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""
定位一组元素
find_elements和find_element区别

定位element,返回值为WebElement类；
定位elements，返回值为list列表类型，列表中每个值为WebElement类；
elements主要用于当一个页面有多个属性相同的元素时，可通过获取所有元素，再通过取值方式获取某个所需的元素


"""
#实例化浏览器驱动
driver = webdriver.Chrome()
#窗口最大话
driver.maximize_window()
#打开百度
driver.get("http://www.baidu.com")

l1 = driver.find_element(By.ID,'kw')
print(l1)
l2 = driver.find_elements(By.ID,'kw')
print(l2)

input("...")
driver.quit()