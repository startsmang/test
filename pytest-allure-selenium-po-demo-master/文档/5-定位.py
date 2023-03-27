#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure
# @Time    : 2022/11/23 15:59
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 5-定位.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()     # 初始化一个浏览器
driver.implicitly_wait(10)      # 设置隐性等待
driver.maximize_window()        # 浏览器窗口最大化

# 1、进入网页
url = 'https://ke.qq.com/'
driver.get(url)      # 打开一个网页

# 2、主页面，点击“登录”按钮
el = driver.find_element('xpath', "//a[text()='登录']")#登录
#//*[@class='header-index-text---ejBK4h']/div[3]/a
#"//*[@class='mod-header__link-login---mOvHOZ']"
el.click()

# 3、切换到 iframe
# iframe = driver.find_element('xpath', '//div/div/iframe')
# driver.switch_to.frame(iframe)
# 4、点击“账号密码登录”

el = driver.find_element('xpath', "//h2[text()='账号登陆']/../div[2]/span")#勾选协议
#/html/body/div[5]/section/div[2]/div/div[2]/span
#/html/body/div[5]/section/div[2]/div/div[2]/span
#//h2[text()='账号登陆']/parent::*/div[2]/span  ==  //h2[text()='账号登陆']/../div[2]/span  成功
#//*[@class='kecomp-checkbox-icon']
#//h2[text()='账号登陆']/following::*div[2]/span  失败
#//h2[text()='账号登陆']/following-sibling::div[2]   成功
#'//*[@class="el-table__header-wrapper"]/following-sibling::div//tbody//td[4]//span'
time.sleep(2)
# 2.常用Xpath的定位方式汇总：
# /child::  （由父节点定位子节点），
# /parent::（由子节点定位父节点），
# /preceding-sibling::（由弟弟节点定位哥哥节点），
# /following::（由哥哥节点定位弟弟节点）
# /..  (父级)
# text/父级/父级/（子）android.widget.ImageView
# XPath轴(XPath
# Axes)可定义某个相对于当前节点的节点集：
#
# 1、child
# 选取当前节点的所有子元素
#
# 2、parent
# 选取当前节点的父节点
#
# 3、descendant
# 选取当前节点的所有后代元素（子、孙等）
#
# 4、ancestor
# 选取当前节点的所有先辈（父、祖父等）
#
# 5、descendant - or -self
# 选取当前节点的所有后代元素（子、孙等）以及当前节点本身
#
# 6、ancestor - or -self
# 选取当前节点的所有先辈（父、祖父等）以及当前节点本身
#
# 7、preceding - sibling
# 选取当前节点之前的所有同级节点
#
# 8、following - sibling
# 选取当前节点之后的所有同级节点
#
# 9、preceding
# 选取文档中当前节点的开始标签之前的所有节点
#
# 10、following
# 选取文档中当前节点的结束标签之后的所有节点
#
# 11、self
# 选取当前节点
#
# 12、attribute
# 选取当前节点的所有属性
#
# 13、namespace
# 选取当前节点的所有命名空间节点
#https://www.cnblogs.com/zhaozhan/archive/2009/09/10/1564347.html

el.click()


el = driver.find_element('xpath', "//p[text()='手机号']")  #点手机登录
el.click()

#通过倒数索引获取
# 代表倒数第1个元素：last()
# 示例：
# //div[@id='food']/*[last()]
#
# 代表倒数第2个元素：last()-1
# 示例：
# //div[@id='food']/*[last()-1]
#
# 代表倒数第3个元素：last()-2
# 示例：
# //div[@id='food']/*[last()-2]


#postion()的用法
# 这里position()就是代表元素的位置，这种写法也是xpath中的一部分。
# //div[@id='food']/*[position()=2]
#
# 高级用法：
# 表示最后1个元素：
# //div[@id='food']/*[position()=last()]
# 表示倒数第3个元素
# //div[@id='food']/*[position()=last()-2]
# 表示最后3个元素
# //div[@id='food']/*[position()>=last()-2]

Expert_list_status = (
By.XPATH, '//*[@class="mainPage"]/*[@class="el-dialog__wrapper mapDialog"]//tbody/tr/td[3]//span')  # 断言 邀请专家状态待发送状态
