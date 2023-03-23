import os
import time
from loguru import logger
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from UI_test.common.parse_yaml import parse_yaml

png_path = parse_yaml("wms.path.png")


class BasePage:
    """
    对于一些原生api的一个封装
    所有基本的原生的api的操作处理方法
    """

    def __init__(self, driver):
        """
        初始化一个浏览器驱动对象
        :param driver: 从外面传递一个浏览器驱动过来
        """
        self.driver = driver

    # 页面截图:截图操作
    def save_screenshot(self, doc=""):
        """页面截图
        :param doc: 需要提示的模块
        :return 不需要返回值
        """
        file_path = png_path + f"{doc}_{time.strftime('%y%m%d%H%M%S', time.localtime())}.png"
        try:
            self.driver.save_screenshot(file_path)
            logger.info(f"截图成功, 文件路径:{file_path}")
        except:
            logger.error(f"{doc}-截图失败!")
            raise

    def get_element(self, by, value, doc=""):
        """
        定位元素
        :param by:  定位方式
        :param value: 定位的表达式
        :param doc: 提示的模块信息
        :return:  返回定位的元素, 如果没有找到, 则抛出异常
        """
        try:
            ele = self.driver.find_element(by, value)
            logger.info(f"模块:{doc},获取元素成功, 定位类型{by},定位表达式:{value}")
            return ele
        except:
            logger.error(f"模块:{doc},元素获取失败, 定位类型{by},定位表达式:{value}")
            self.save_screenshot(doc)
            raise

    def get_all_element(self, by, value, doc=""):
        """
        获取所有的元素 如果没有则返回一个空列表
        :param by: 定位方式
        :param value: 定位表达式
        :param doc:  说明文档
        :return: 返回一个定位的列表集合,如果没有定位元素, 返回一个空列表
        """
        try:
            ele_list = self.driver.find_elements(by, value)
            logger.info(f"模块:{doc},获取元素成功, 定位方式:{by},定位表达式:{value}")
            return ele_list
        except:
            logger.error(f"{doc}-获取所有元素失败, 定位方式:{by},定位表达式:{value}")
            self.save_screenshot(doc)
            raise

    def wait_ele_presence(self, locator, timeout=10, doc=""):
        """
        等待获取元素
        :param locator: 元组, 包括元素定位方式, 元素定位的表达式
        :param timeout: 等待超时时间 默认为10s
        :param doc: 说明文档
        :return:返回定位的元素
        """
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            logger.info(f"{doc}等待元素成功,定位方式{locator}")
            return ele
        except:
            logger.error(f"{doc}等待元素失败,定位方式{locator}")
            self.save_screenshot(doc)
            raise

    def wait_ele_all_presence(self, locator, timeout=10, doc=""):
        """
        等待获取元素
        :param locator: 元组, 包括元素定位方式, 元素定位的表达式
        :param timeout: 等待超时时间 默认为10s
        :param doc: 说明文档
        :return:返回定位的元素列表, 如果没有, 返回一个空列表
        """
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            logger.info(f"{doc}等待元素成功,定位方式{locator}")
            return ele
        except:
            logger.error(f"{doc}等待元素失败,定位方式{locator}")
            self.save_screenshot(doc)
            raise

    def url_matches(self, url, timeout=10, doc="url路径匹配"):
        """
        等待页面的请求的路径匹配
        :param url: 期望的url路径
        :param timeout: 超时时间 默认10s
        :param doc: 说明文档
        :return: 没有返回
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            logger.info(f"{doc}:页面路径:{self.driver.current_url}, 匹配路径:{url}")
        except:
            logger.error(f"{doc}:页面路径:{self.driver.current_url}, 匹配路径:{url}")
            self.save_screenshot(doc)
            raise

    # 等待元素可见
    def wait_ele_visible(self, locator, timeout=10, doc=""):
        """
        等待元素课件
        :param locator: 元组  (定位方式, 定位表达式)
        :param timeout: 超时时间 默认为10s
        :param doc: 说明文档
        :return: 返回找到的元素
        """
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            logger.info(f"{doc}:元素定位成功,定位方式:{locator}")
            return ele
        except:
            self.save_screenshot(doc)
            logger.error("{}-元素不存在:{}".format(doc, locator))
            raise

    def clear(self, ele, type=1, doc=""):
        """
        清除元素内容
        :param ele: 定位到的元素
        :param type: 1: 使用常规方式清除 0: 使用选中, 然后使用回退键
        :param doc:
        :return:
        """
        try:
            if type == 1:
                ele.clear()
            else:
                ele.send_keys(Keys.Ctrontrol, 'a')
                ele.send_keys(Keys.BACKSPACE)
            logger.info(f"模块:{doc},清楚元素内容成功, 清除方式{type},操作元素{ele.get_attribute('outerHTML')}")
        except:
            logger.error(f"{doc}-清楚元素内容失败!, 清除方式{type},操作元素{ele.get_attribute('outerHTML')}")
            self.save_screenshot(doc)
            raise

    def execute_js(self, js, doc=""):
        """
        执行js脚本
        :param js:
        :param doc:说明文档
        :return:
        """
        try:
            self.driver.execute_script(js)
            logger.info(f"执行js脚本成功:{js}")
        except:
            logger.error(f"执行js脚本失败:{js}")
            self.save_screenshot(doc)
            raise

    def sleep(self, seconds=1, doc=""):
        """
        强制暂停
        :param seconds: 秒数 默认值为1秒
        :param doc: 功能模块
        :return: 不用返回
        """
        time.sleep(seconds)
        logger.info(f"功能模块{doc},强制暂停{seconds}秒")

    def input_text(self, ele, value, doc=""):
        """
        给指定元素WebElement元素设置值
        :param ele: 定位的元素
        :param value: 设置对应的值
        :return: 无返回值
        """
        try:
            ele.send_keys(value)
            logger.info(f"功能模块:{doc}, 输入文本内容{value}, 定位的元素{ele.get_attribute('outerHTML')}")
        except:
            logger.error(f"{doc}-设置内容失败,  输入文本内容{value}, 定位的元素{ele.get_attribute('outerHTML')}")
            self.save_screenshot(doc)
            raise

    def get_text(self, ele, doc="获取元素内容"):
        """
        获取元素内容
        :param ele: 定位的元素 WebElement
        :param doc: 说明文档
        :return: 返回对应的内容
        """
        try:
            data = ele.text
            return data
        except:
            logger.error(f"{doc}-获取元素失败")
            self.save_screenshot(doc)
            raise

    def get_attribute(self, ele, name, doc="获取属性值"):
        """
        根据key获取对应的属性值
        :param ele: Webelement元素
        :param name: 对应的属性名称
        :param doc: 对应的说明文档
        :return: 返回对应的值
        """
        try:
            value = ele.get_attribute(name)
            logger.info(f"{doc}: 获取属性{name}值{value}成功")
            return value
        except:
            logger.error(f"{doc}-获取属性{name}值{value}失败")
            self.save_screenshot(doc)
            raise

    def select_by_value(self, ele, value, doc=""):
        """
        根据对应的下拉框的值选择对应的选项
        :param ele: 定位的元素
        :param value: 选择的值
        :param doc: 说明文档
        :return: 无返回值
        """
        try:
            ele_select = Select(ele)
            ele_select.select_by_value(str(value))
            logger.info(f"{doc}:{ele.get_attribute('outerHTML')}选择对应的值{value}")
        except:
            logger.error(f"操作失败:{doc}:{ele.get_attribute('outerHTML')}选择对应的值{value}")
            self.save_screenshot(doc)
            raise

    def select_by_index(self, ele, index, doc=""):
        """
        根据对应的下拉框的值选择对应的选项
        :param ele: 定位的元素
        :param index: 选择的索引 索引值从1开始
        :param doc: 说明文档
        :return: 无返回值
        """
        try:
            ele_select = Select(ele)
            ele_select.select_by_index(index)
            logger.info(f"{doc}:{ele.get_attribute('outerHTML')}选择对应的索引值{index}")
        except:
            logger.error(f"操作失败:{doc}:{ele.get_attribute('outerHTML')}选择对应的索引值{index}")
            self.save_screenshot(doc)
            raise

    def select_by_visible_text(self, ele, text, doc=""):
        """
        根据对应的下拉框的值选择对应的选项
        :param ele: 定位的元素
        :param text: 选择对应的内容选项
        :param doc: 说明文档
        :return: 无返回值
        """
        try:
            ele_select = Select(ele)
            ele_select.select_by_visible_text(text)
            logger.info(f"{doc}:{ele.get_attribute('outerHTML')}选择对应的内容{text}")
        except:
            logger.error(f"操作失败:{doc}:{ele.get_attribute('outerHTML')}选择对应的内容{text}")
            self.save_screenshot(doc)
            raise

    def click(self, ele, doc=""):
        """
        单击页面元素
        :param ele:  页面中的元素
        :param doc: 说明文档
        :return: 无返回值
        """
        try:
            logger.info(f"操作说明{doc},点击页面元素{ele.get_attribute('outerHTML')}")
            ele.click()
        except:
            logger.error(f"{doc}-点击操作{ele.get_attribute('outerHTML')}失败")
            self.save_screenshot(doc)
            raise

    def switch_iframe(self, iframe, timeout=10, doc="切换iframe"):
        """
        切换iframe窗口到指定的iframe
        :param iframe: 可以是id, name, 或者是一个webelement元素
        :param timeout: 超时时间 默认为10s
        :param doc: 说明文档
        :return: 无返回值
        """
        try:
            self.driver.switch_to.frame(iframe)
            logger.info(f"{doc}:切换iframe窗口成功,定位iframe:{iframe}")
        except:
            logger.error(f"{doc}:切换iframe窗口失败,定位iframe:{iframe}")
            self.save_screenshot(doc)
            raise

    def switch_parent_iframe(self, doc="返回上层窗口"):
        """
        返回上层窗口
        :param doc: 说明文档
        :return: 无返回值
        """
        try:
            self.driver.switch_to.parent_frame()
            logger.info(f"{doc}:切换到上层iframe窗口成功")
        except:
            logger.error(f"{doc}:切换iframe窗口失败")
            self.save_screenshot(doc)
            raise

    def switch_default_iframe(self, doc="退回到默认iframe窗口"):
        """
        切换到默认窗口
        :param doc: 说明文档
        :return: 无返回值
        """
        try:
            self.driver.switch_to.default_content()
            logger.info(f"{doc}:切换到默认窗口成功")
        except:
            logger.error(f"{doc}:切换默认窗口失败")
            self.save_screenshot(doc)
            raise

    def quit(self):
        """
        退出浏览器
        :return:
        """
        self.driver.quit()
        logger.info(f"退出浏览器成功")


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    ele: WebElement = driver.find_element(By.ID, "kw")
