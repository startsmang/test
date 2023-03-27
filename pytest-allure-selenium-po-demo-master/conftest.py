#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : conftest.py
# @Time : 2022-03-03 15:34
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------


import time
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure
from selenium import webdriver
from common.logger import Logger
from common.screen_recordings import RecordScreen
from common.readCofig import *
from selenium.webdriver.chrome.service import Service as ChromeService

Firefox = 'firefox'
Chrome = 'chrome'
IE = 'ie'
# Grid = 'grid'
ChromeHeadless = 'chrome-headless'
FirefoxHeadless = 'firefox-headless'


@pytest.fixture(scope="function", autouse=True)
def screencap():
    now = time.strftime("%y%m%d%H%M%S", time.localtime())
    images_path = f'./images/{now}.mp4'
    SR = RecordScreen(images_path=images_path)
    SR.start()

    yield

    SR.stop()

    allure.attach.file(images_path, name='录屏',
                       attachment_type=allure.attachment_type.MP4)  # 测试步骤中添加一张图片或视频


#session 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
# 声明使用request测试固件
@pytest.fixture(scope="session")
def driver1(request):


    # 定义一个清理函数, 清理函数向相当于teardown_xxx
    def end():
        Logger.info("全部用例执行完后 teardown quit dirver1")
        time.sleep(5)
        driver.quit()

    # 注册一个清理函数
    request.addfinalizer(end)
    # 注册完清理函数后，如果在测试固件里抛出异常,只有清理函数照常执行


    global driver
    if browerType == Chrome:
        # chromeOptions 是一个配置 chrome 启动是属性的类。通过这个类，我们可以为chrome配置如下参数
        # 添加启动参数(add_argument)
        #设置 chrome 二进制文件位置 (binary_location)
        # 添加启动参数 (add_argument)
        # 添加扩展应用 (add_extension, add_encoded_extension)
        # 添加实验性质的设置参数 (add_experimental_option)
        # 设置调试器地址 (debugger_address)
        service = ChromeService(executable_path=ChromeDriverManager().install())  # selenium4.0自动下载驱动
        #pip install webdriver_manager -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
        path = r'D:'
        Logger.info("驱动地址：%s"%service.path)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--user-data-dir='+path)  # 文件下载设置路径防止弹窗
        #chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片，提升运行速度
        driver = webdriver.Chrome(options=chrome_options,service=service)
        driver.implicitly_wait(timeout)
        driver.maximize_window()
        # assert(1 == 3)

    elif browerType == ChromeHeadless:
        # chrome headless模式
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片，提升运行速度
        service = ChromeService(executable_path=ChromeDriverManager().install())  # selenium4.0自动下载驱动
        Logger.info("驱动地址：%s"%service.path)
        driver = webdriver.Chrome(options=chrome_options,service=service)
        driver.implicitly_wait(timeout)

    elif browerType == Firefox:
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(timeout)


    elif browerType == FirefoxHeadless:
        # firefox headless模式
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)
        driver.implicitly_wait(timeout)

    # elif browerType == Grid:
    #     # 通过远程节点运行
          # https://www.jianshu.com/p/5c57df3ca3b7
    #     chrome_capabilities = {
    #         "browserName": "chrome",
    #         "version": "",
    #         "platform": "ANY",
    #         "javascriptEnabled": True,
    #         # "marionette": True,
    #     }
    #
    #     driver = webdriver.Remote(hubIP, desired_capabilities=chrome_capabilities)
    #
    #     driver.set_window_size(1920, 1080)
    #
    # else:
    #     raise NameError("driver驱动类型定义错误！")

    return driver





#每个方法执行前都会执行清理其他标签页
@pytest.fixture(autouse=True)
def close():
    yield
    First_handle = driver.current_window_handle#获取当前句柄
    n = driver.window_handles#获取所以句柄
    Logger.info(n)
    for handle in n:
        if handle != First_handle:
            driver.switch_to.window(handle)
            # 做完一系列操作后关闭school_handle
            driver.close()
            # 切换窗口会第一个窗口
    driver.switch_to.window(First_handle)
    # driver.get(data['URL'])









#def driver1(request):
#     """定义全局driver fixture，给其它地方作参数调用"""
#     if platform.system()=='Windows':
#         print("当前运行的操作系统为windows")
#         chrome_options = Options()
#         chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度，高度
#         # chrome_options.add_argument('--headless')  # 无界面
#         _driver = webdriver.Chrome(options=chrome_options)
#         # _driver.get(url)
#         _driver.get("https://www.oschina.net/home/login")
#         login1=LoginBusiness(_driver)
#         login1.login("18821768014","hbq19941120")
#
#     else:
#         print('当前运行的操作系统为linux')
#         chrome_options = Options()
#         chrome_options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在报错问题
#         chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度，高度
#         chrome_options.add_argument('--disable-gpu')#禁用GPU硬件加速，如果软件渲染器没有就位，则GPU进程将不会启动
#         chrome_options.add_argument('--disable-dev-shm-usage')#-禁用-开发-SHM-使用
#         chrome_options.add_argument('--headless')  # 无界面
#         _driver = webdriver.Chrome(options=chrome_options)
#         # _driver.get(data['URL'])
#         _driver.get("https://www.oschina.net/home/login")
#         print('打开了网页')
#
    # def end():
    #     print("全部用例执行完后 teardown quit dirver1")
    #     time.sleep(5)
    #     _driver.quit()
    #
    # # 注册一个清理函数
    # request.addfinalizer(end)
    # # 注册完清理函数后，如果在测试固件里抛出异常,清理函数照常执行
    # return _driver


