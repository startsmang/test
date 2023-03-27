#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-selenium-allure
# @Time    : 2022/11/23 15:21
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 1-初始化浏览器webdriver.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------




from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service = Service(executable_path=ChromeDriverManager().install())  # selenium4.0自动下载驱动
print(service.path)
#driver = webdriver.Chrome( service=service) # selenium4.0  自动下载驱动 上面代码就是简单触发了一下浏览器，主要是由ChromeDriverManager().install() 方法自动安装默认浏览器的适配驱动，首先它会获取当前浏览器版本号，再去下载相关驱动。


# 设置无界面浏览器
option = webdriver.ChromeOptions()  # 创建一个配置对象
option.add_argument("--headless")  # 开启无界面模式
option.add_argument("--disable-gpu")  # 禁用gpu
#options=option,


driver = webdriver.Chrome(service=Service(r'D:\Program Files\python310\chromedriver.exe'))  # selenium4.0  手动配置驱动

#driver = webdriver.Chrome() #默认python主目录下

#driver = webdriver.Chrome(r'D:\Program Files\python310\chromedriver.exe')  # 旧版手动配置驱动写法

driver.get('https://www.baidu.com/')

#新闻 hao123 地图 贴吧 视频 图片 网盘 更多 设置 登录
baidu_link=(By.XPATH, "//*[@class='mnav c-font-normal c-color-t']")

driver.find_element(*baidu_link).click()

driver.find_elements(*baidu_link)[4].click()



input("...")
driver.quit()


'''
options.add_argument(‘headless’) # 无头模式
options.add_argument(‘window-size={}x{}’.format(width, height)) # 直接配置大小和set_window_size一样
options.add_argument(‘disable-gpu’) # 禁用GPU加速
options.add_argument(‘proxy-server={}’.format(self.proxy_server)) # 配置代理
options.add_argument(’–no-sandbox’) # 沙盒模式运行
options.add_argument(’–disable-setuid-sandbox’) # 禁用沙盒
options.add_argument(’–disable-dev-shm-usage’) # 大量渲染时候写入/tmp而非/dev/shm
options.add_argument(’–user-data-dir={profile_path}’.format(profile_path)) # 用户数据存入指定文件
options.add_argument('no-default-browser-check) # 不做浏览器默认检查
options.add_argument("–disable-popup-blocking") # 允许弹窗
options.add_argument("–disable-extensions") # 禁用扩展
options.add_argument("–ignore-certificate-errors") # 忽略不信任证书
options.add_argument("–no-first-run") # 初始化时为空白页面
options.add_argument(’–start-maximized’) # 最大化启动
options.add_argument(’–disable-notifications’) # 禁用通知警告
options.add_argument(’–enable-automation’) # 通知(通知用户其浏览器正由自动化测试控制)
options.add_argument(’–disable-xss-auditor’) # 禁止xss防护
options.add_argument(’–disable-web-security’) # 关闭安全策略
options.add_argument(’–allow-running-insecure-content’) # 允许运行不安全的内容
options.add_argument(’–disable-webgl’) # 禁用webgl
options.add_argument(’–homedir={}’) # 指定主目录存放位置
options.add_argument(’–disk-cache-dir={临时文件目录}’) # 指定临时文件目录
options.add_argument(‘disable-cache’) # 禁用缓存
options.add_argument(‘excludeSwitches’, [‘enable-automation’]) # 开发者模式
'''