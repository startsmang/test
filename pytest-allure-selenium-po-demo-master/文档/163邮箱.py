#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure
# @Time    : 2022/11/23 17:42
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 163邮箱.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

service = ChromeService(executable_path=ChromeDriverManager().install())  # selenium4.0自动下载驱动
print("驱动地址：", service.path)
driver = webdriver.Chrome(service=service)  # 初始化driver

driver.implicitly_wait(20)  # 隐式等待


# 查找元素
def get_element(locator):
    try:
        button = driver.find_element(*locator)

        webdriver.ActionChains(driver).move_to_element(button).click(button).perform()
        print('%s,%s:存在' % locator)
        return True
    except:
        print('%s,%s:不存在' % locator)
        return False


url = "https://mail.163.com/js6/main.jsp?sid=lBTCJYgsYOKbMTUHHmssuOLCfZXAVMLm&df=mail163_letter#module=mbox.ListModule%7C%7B%22fid%22%3A4%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D"
driver.get(url)  # 打开浏览器地址

# 浏览器中F12 接口请求中获取cookie信息
cookie_dic = {

    "MAIL_PINFO": "huangpeng245@163.com|1669081420|1|mail163|11&16|sxi&1668630573&mail163#sxi&610100#10#0#0|&0|mail163|huangpeng245@163.com"
    ,
    "MAIL_PASSPORT": "pgWa3YfJ74wXMw57.uxCCyPwylULITPCEEBBjcnPjwgWj0mKjiCG5_snVCxBM4a3Y11JHhZv_XxLn7fJrrFCAlEFPw1ztGQobMA_RMM.7FkRiE7lnarizGmiNDamaAIbh_VzDi_MCnjo5R73KuPI2z6XH9ZEdlzb3q86kmWuv6dM_FV026e.eOZeq43uXYaO1"

}

for k, v in cookie_dic.items():  # 添加cookie
    print(k, v)
    driver.add_cookie({
        'name': k,
        'value': str(v)
    })
print('添加cookie')

driver.get(url)  # 打开浏览器地址
driver.maximize_window()
time.sleep(3)
#//*[@id="_mail_component_83_83"]/span[2]
#//*[@id="_mail_component_83_83"]/span[2]
#//*[@id="_mail_component_82_82"]/span[2]
#//*[@id="_mail_component_83_83"]/span[2]
#//*[@id="_mail_component_82_82"]/span[2]
#//*[@id="_mail_component_83_83"]/span[2]
driver.find_element(By.XPATH,"//*[@class='nui-tree-item-text']").click()
driver.find_element(By.XPATH,"//*[@class='js-component-icon nui-ico nui-ico-checkbox  ']").click()
#//*[@id="fly0"]
#//*[@id="fly0"]
# driver.find_element(By.XPATH, '//*[@id="spnHideFolders"]').click()  # 点击其他2个文件
# driver.find_element(By.XPATH, '//*[@id="dvNavTree"]/ul/li/ul/li[5]/div/span[2]').click()  # 点击已删除

# # 定位点击 confirm
# driver.find_element(By.XPATH, '//*[@id="_mail_button_49_661"]/span').click()
# # 切换到 confirm 弹框
# confirm = driver.switch_to.alert
# # 获取 confirm 文本内容
# print(confirm.text)
# # 取消
# confirm.dismiss()
# # 确定
# # confirm.accept()

# 2.常用Xpath的定位方式汇总：
# /child::  （由父节点定位子节点），
# /parent::（由子节点定位父节点），
# /preceding-sibling::（由弟弟节点定位哥哥节点），
# /following::（由哥哥节点定位弟弟节点）
# /..  (父级)
# text/父级/父级/（子）android.widget.ImageView


index = 1
while True:
    print(index)
    all_sel = (By.XPATH, "//*[@class='js-component-icon nui-ico nui-ico-checkbox']")  # 全选框元素定位
    if get_element(all_sel) == False:  # 判断全选框是否存在
        break
    driver.find_element(all_sel).click()  # 点击全选框
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='彻底删除']").click()
    driver.find_element(By.XPATH, "//span[text()='确 定']").click()
    time.sleep(3)

    index += 1

driver.close()
