#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure
# @Time    : 2022/11/23 16:47
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 6-切换iframe.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
一、selenium处理frame
1. frame概要
在web自动化中，如果一个元素定位不到，很有可能定位的元素在iframe中
frame是html中的框架，在html中，所谓的框架就是可以在同一个浏览器中显示不止一个页面
基于html框架，又分为垂直架构和水平架构
frame分为三种：frameset、frame、iframe

frmeset和普通的html标签一样，不会影响正常的定位，可使用常用的定位方法进行定位
frame和iframe在selenium则是有一组方法进行操作
frame嵌套分为两种：一种是嵌套的，一种是未嵌套的

切换frame语法：

driver.switch_to.frame()：根据元素id或者index切换frame
driver.switch_to.default_content()：切换到默认frame
driver.switch_to.parent_frame()：切换到父级frame
对于未嵌套frame：

driver.switch_to.frame(“frame id”)
driver.switch_to.frame(“frame-index”)frame无ID的时候依据索引来处理，索引从0开始，例如：driver.switch_to.frame(0)
对于嵌套的frame：

对于嵌套的frame需要先进入到iframe的父节点，再进入到子节点，然后可以对字节点里面的对象进行处理和操作
driver.switch_to.frame(“父节点”)
driver.switch_to.farme(“子节点”)
————————————————
WebDriverWait(driver, 20, 0.5).until(EC.frame_to_be_available_and_switch_to_it(iframe_element))
'''



driver = webdriver.Chrome()
driver.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_html_form_radio")
# # 下标
#driver.switch_to.frame(1)
# name属性



#//*[@id="iframeResult"]
#知识点：
#frame处理：switch_to.frame，传入frame的id，即可进入对应的frame，返回上一层用parent_frame()，返回初始页面使用default_content()
# 打开页面后，进入到id=iframeResult的frame下，操作元素
# driver.switch_to.frame("iframeResult"),也可传元素对象
#driver.switch_to.frame(iframe的name属性或webelement对象或下标)
#driver.switch_to.frame(“login_frame_qq”)#切换到name为login_frame_qq的iframe中
#driver.switvh_to.frame(0)#切换到第一个iframe中
#driver.switch_to.frame((By.xpath,"//div[@class="ptlogin_wrap"]))

#WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(iframe_reference))

iframe_element=driver.find_element(By.XPATH,'//*[@id="iframeResult"]')
#driver.switch_to.frame(iframe_element)#iframe frameborder="0" id=""iframeResult" name="iframeResult"cd_frame_id_="5e3196f2ecb49b11cc2835e2890068f">

WebDriverWait(driver, 20, 0.5).until(EC.frame_to_be_available_and_switch_to_it(iframe_element))
# webelement对象
# driver.switch_to.frame(driver.find_element(By.ID,"iframeResult"))

# ===========  进入了iframe当中的html  ==============
driver.find_element(By.XPATH, '/html/body/form/input[2]').click() ##'//*[@value="female"]'
time.sleep(2)

# 切换回上一层
driver.switch_to.parent_frame()

driver.find_element(By.XPATH, "//a[text()='运行代码']").click() ##'//*[@value="female"]'

#/html/body/form/input[2]
#//input[@value="female"]


element_text= WebDriverWait(driver, 20, 0.5).until(EC.text_to_be_present_in_element((By.XPATH,'//*[@id="tiy_btn_tryit"]/a'),"运行代码"),)
print(element_text)
# # 从iframe当中，切换回最顶层的html
# driver.switch_to.default_content()


driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

# 打开页面后，进入到id=iframeResult的frame下，操作元素
#driver.switch_to.frame("iframeResult")

WebDriverWait(driver, 20, 0.5).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"iframeResult")))

print(driver.find_element(By.XPATH, '//*[@id="draggable"]').text)
# 操作完成后，回到页面，操作"点击运行",使用parent_frame()或default_content()
driver.switch_to.parent_frame()
driver.find_element(By.XPATH, '//*[@id="submitBTN"]').click()


input("...")
driver.quit()