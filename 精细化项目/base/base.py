
import datetime
import os,re
import time,json
import allure
from 精细化项目.common.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys#导入键盘操作包



def switch_iframe(self, iframe_reference, timeout=60, timewait=0, doc="进入切换iframe"):
    """"""
    time.sleep(timewait)
    # https://blog.51cto.com/u_15127619/4897451

    try:
        start = datetime.datetime.now()
        WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(iframe_reference))
        end = datetime.datetime.now()
        Logger.info("{}-进入表单切换iframe成功，等待{}秒".format(doc, (end - start).seconds))

        self.allure_step_json__screenshot(step_text=doc, content="{}-进入表单切换iframe成功-{}".format(doc, iframe_reference))
        time.sleep(timewait)
    except:
        Logger.exception("{}-进入表单失败-{}".format(doc, iframe_reference))
        self.allure_step_json__screenshot(step_text=doc, content="{}-进入表单失败-{}".format(doc, iframe_reference))
        time.sleep(timewait)
        raise
