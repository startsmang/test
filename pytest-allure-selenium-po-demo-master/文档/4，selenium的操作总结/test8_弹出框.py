"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

"""
弹出框
在web页面上经常会遇到一些弹出框，弹出框也分很多种，有的点击确定和取消，有的可以输入一些内容

弹出框分三种，分别是：alert，confirm，prompt

弹出框的主要操作方法

text:获取文本值
accept():点击‘确认’
dismiss() :点击“取消”或者关闭弹出框
send_keys(): 输入文本值


"""
#实例化浏览器驱动
driver = webdriver.Chrome()
#窗口最大话
driver.maximize_window()
#打开百度

#
# #alert
# driver.find_element_by_id('hbq').click()
# #切换到alert
# a = driver.switch_to.alert
# #打印弹出框文本内容
# print(a.text)
# time.sleep(5)
# #点击确定
# a.accept()
#
# #confirm
# driver.find_element_by_id('hbq').click()
# #切换到alert
# a = driver.switch_to.alert
# #打印弹出框文本内容
# print(a.text)
# time.sleep(5)
# #点击取消
# a.dismiss()
# print(a.text)
# time.sleep(5)
# #点击确定
# a.accept()

#prompt
url3 ="http://sahitest.com/demo/promptTest.htm"
driver.maximize_window()
driver.get(url=url3)

driver.find_element(By.XPATH,"//input[@name = 'b1']").click()
time.sleep(2)

#通过switch_to.alert切换alert
a3 = driver.switch_to.alert
print(a3.text)

#在prompt型alert中输入字符
a3.send_keys('哈哈哈哈哈')
time.sleep(2)

a3.accept()





# driver.find_element_by_xpath('/html/body/input').click()
# time.sleep(3)
# #切换到alert
# a = driver.switch_to.alert
# #打印弹出框文本内容
# print(a.text)
# time.sleep(3)
# a.send_keys('测试之道啊')
# time.sleep(2)
# #点击确定
# a.accept()
# #点击取消
# a.dismiss()
# print(a.text)
# time.sleep(3)

