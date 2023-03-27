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
import random
import pytest
from common.login_api import *
from common.logger import Logger
from common.read_yaml import ReadYaml
data = ReadYaml("data.yaml").get_yaml_data()#读取数据

#session 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
@pytest.fixture(scope="function")
def random_num():
    num = random.randint(100, 999)
    return num


@pytest.fixture(scope="session",autouse=False) #False
def Web_Login(driver1):


    driver=driver1
    risk_sys_path='/risk_sys/#/projectList/m'
    Logger.info(data['url'] + risk_sys_path)
    driver.get(data['url'] + risk_sys_path)
    Logger.info('打开浏览器')
    time.sleep(2)
    Logger.info([data['url'], data['login_ID']['user_name'],data['login_ID']['password']])
    Cookie_lisi = login_Cookie(data['url'], data['login_ID']['user_name'],data['login_ID']['password'])  # 调接口获取

    for k, v in Cookie_lisi.items():
        Logger.info([k, v])
        driver.add_cookie({
            'name': k,
            'value': str(v)
        })
    Logger.info('添加cookie')

    driver.get(data['url'] + risk_sys_path)

    # 刷新浏览器
    time.sleep(2)
    try:
        driver.refresh()
        Logger.info('刷新页面成功')
    except Exception as e:
        Logger.info('刷新页面失败')



