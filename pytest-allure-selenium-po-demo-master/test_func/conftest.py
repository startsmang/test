#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : conftest.py
# @Time : 2022-03-03 15:34
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------



from common.logger import Logger
import pytest



#
# @pytest.fixture(scope="session",autouse=True)
# def driver(driver1):
#     Logger.info("……driver……")
#     return driver1