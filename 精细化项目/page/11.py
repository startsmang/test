# 使用pytest框架 写一个测试用例，打开浏览器，打开百度首页，输入关键字，点击搜索，关闭浏览器
# 1.导包
import pytest
from selenium import webdriver
# 2.定义测试类
class TestBaidu:
# 3.定义测试方法
    def test_baidu(self):
        # 4.打开浏览器
        driver = webdriver.Chrome()
        # 5.打开百度首页
        driver.get("https://www.baidu.com/")
        # 6.输入关键字
        driver.find_element_by_id("kw").send_keys("python")
        # 7.点击搜索
        driver.find_element_by_id("su").click()
        # 8.关闭浏览器
        driver.quit()
# 9.运行测试用例
if __name__ == '__main__':
    pytest.main(["-s", "test_baidu.py"])
# 10.运行结果
# ============================= test session starts ==============================
# platform win32 -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
# rootdir: D:\PycharmProjects\UI_test
# collected 1 item
#
# test_baidu.py python
#

