import time

from selenium import webdriver
from loguru import logger
import os

from UI_test.common.parse_yaml import parse_yaml

# 读取配置文件, 并且配置对应的日志存放路径
log_path = parse_yaml("wms.path.log")
filename_info = log_path + "wms_info_" + time.strftime("%Y%m%d", time.localtime()) + ".log"
filename_error = log_path + "wms_error_" + time.strftime("%Y%m%d", time.localtime()) + ".log"
logger.add(filename_info, level="INFO", encoding="utf-8", rotation="00:00")
logger.add(filename_error, level="ERROR", encoding="utf-8", rotation="00:00")


# 打开浏览器的函数
def open_browser():
    driver = webdriver.Chrome()  # 使用google浏览器
    driver.maximize_window()  # 最大化窗口
    return driver  # 返回浏览器驱动



