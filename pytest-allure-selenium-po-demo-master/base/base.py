import datetime
import os,re
import time,json
import allure
from common.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys#导入键盘操作包

# 封装基本函数 - 执行日志 - 异常处理 - 失败截图
# 所有页面公共的部分
class BasePage:

    def __init__(self,driver):

        self.driver = driver

    def allure_step_json__screenshot(self,step_text:str,content:dict or str,doc="添加附件"):
        with allure.step(step_text):

            allure.attach(json.dumps([content], ensure_ascii=False, indent=4), '文本内容：',
                          allure.attachment_type.JSON)

            self.save_screenshot("{}-截图".format(step_text), step=False)






    # 截图操作
    def save_screenshot(self, doc,step=True):
        """  知识点解析      #time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数 format 决定。"""
        # 图片名称  页面名称  操作名称   时间  png
        doc_srt = re.sub(r'[.,"\' -?:/!;“]', '', doc)
        file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + "/png/{}_{}.png".format(doc_srt,
                                                                    time.strftime("%y%m%d-%H%M%S", time.localtime())))
        try:
            self.driver.save_screenshot(file_path)
            Logger.info("截图成功，文件路径:{}".format(file_path))
            if step:
                with allure.step(doc):
                    allure.attach.file(file_path, doc, allure.attachment_type.PNG)
            else:
                allure.attach.file(file_path, doc, allure.attachment_type.PNG)
        except:
            Logger.exception("{}-截图失败！！！".format(doc))

    # 等待元素存在
    def wait_ele_presence(self, locator, center=True, timeout=20, doc=""):
        """     知识点解析：
        #https://zhuanlan.zhihu.com/p/32094268
        #scrollIntoView:
                # 如果为true，元素的顶端将和其所在滚动区的可视区域的顶端对齐。
                # 如果为false，元素的底端将和其所在滚动区的可视区域的底端对齐。
        #scrollIntoViewIfNeeded:
                #如果为true，则元素将在其所在滚动区的可视区域中居中对其。
                # 如果为false，则元素将与其所在滚动区的可视区域最近的边缘对齐。 根据可见区域最靠近元素的哪个边缘，
                # 元素的顶部将与可见区域的顶部边缘对准，或者元素的底部边缘将与可见区域的底部边缘对准。

        #log.exception('exception') #异常信息被自动添加到日志消息中
        #Logger.error(msg[ , *args[ , **kwargs] ] )只记录错误信息"""
        try:
            start = datetime.datetime.now()
            #https://blog.csdn.net/weixin_53782558/article/details/126910789
            #显示等待需要用到两个类：WebDriverWait 和 expected_conditions两个类
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            Logger.info("{}-元素{}已存在，等待{}秒".format(doc, locator, (end - start).seconds))
            self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(arguments[1]);", ele, center)##滚动查找
            return ele
        except Exception as e :
            Logger.exception("{}-元素不存在-{} :{}".format(doc, locator,e))

            self.save_screenshot("{}-元素不存在".format(doc))
            raise

    def get_url(self,url):

        self.driver.get(url)
        result_dic = {'url': url}
        self.allure_step_json__screenshot(step_text="打开url %s "%url,content=result_dic)

    # 等待元素可见
    def wait_ele_visible(self, locator, center=True, timeout=15, doc=""):
        self.wait_ele_presence(locator, center, timeout, doc)
        try:
            start = datetime.datetime.now()
            #https://blog.csdn.net/weixin_53782558/article/details/126910789
            #显示等待需要用到两个类：WebDriverWait 和 expected_conditions两个类
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            Logger.info("{}-元素{}已可见，等待{}秒".format(doc, locator, (end - start).seconds))
            return ele
        except:
            Logger.exception("{}-元素不可见-{}".format(doc, locator))
            self.save_screenshot("{}-元素不可见".format(doc))
            raise

    # 点击操作
    def click_element(self, locator, center=True, mode=1, timeout=15, timewait=0.2,doc=""):

        time.sleep(timewait)
        try:

            if mode == 1:
                ele = self.wait_ele_visible(locator, center, timeout, doc)
                ele.click()
            if mode == 2:
                ele = self.wait_ele_visible(locator, center, timeout, doc)
                #JavaScript是运行在客户端（浏览器）和服务器端的脚本语言，允许将静态网页转换为交互式网页。可以通过 Python Selenium WebDriver
                # 执行 JavaScript 语句，在Web页面中进行js交互。那么js能做的事，Selenium应该大部分也能做。WebDriver是模拟终端用户的交互，
                # 所以就不能点击不可见的元素，有时可见元素也不能点击。在这些情况下，我们就可以通过WebDriver 执行JavaScript来点击或者执行页面元素
                self.driver.execute_script("arguments[0].click();", ele)
            if mode == 3:
                ele = self.wait_ele_presence(locator, center, timeout, doc)

                #有时候我们在通过Selenium做UI自动化的时候，明明能够在DOM树内看到这个元素，但是我在通过driver click、sendkey的时候，
                # 就是点击不到或无法输入字符串。实际上这是由于WEB中某些元素需要通过一系列连贯的操作才能处于可以点击的状态，
                # driver提供的click方法是每次都只执行一个命令操作，而我们需要连贯的操作。或者经常遇到那种，需要鼠标悬浮后，
                # 要操作的元素才会出现的某种场景，那么我们就要模拟鼠标悬浮到某一个位置，做一系列的连贯操作，
                # 这里就要应用Selenium提供的ActionChains模块
                ActionChains(self.driver).click(ele).perform()#

            self.allure_step_json__screenshot(step_text=doc, content="{}-元素点击成功".format(doc))
            Logger.info("{}-元素{}点击成功".format(doc, locator))
            time.sleep(timewait)

        except:
            Logger.exception("{}-元素点击失败-{}".format(doc, locator))
            #self.save_screenshot("{}-点击失败".format(doc))
            self.allure_step_json__screenshot(step_text=doc, content="{}-元素点击失败-{}".format(doc, locator))
            time.sleep(timewait)
            raise


    # 输入操作
    def input_text(self, locator, text, clear="", center=True, timeout=15,timewait=0.3, doc=""):
        ele = self.wait_ele_presence(locator, center, timeout, doc)
        time.sleep(timewait)
        try:
            if clear == 1:
                ele.clear()
            elif clear == 2:
                ele.send_keys(Keys.CONTROL, "a")
                ele.send_keys(Keys.DELETE)
            ele.send_keys(text)
            result_dic = {
                '输入内容': text
            }

            self.allure_step_json__screenshot(step_text=doc, content=result_dic)

            Logger.info("{}-元素{}输入：{}".format(doc, locator, text))
            time.sleep(timewait)

        except:
            Logger.error("{}-元素{}输入：{}".format(doc, locator, text))
            result_dic={
                    '输入内容':text
                }
            self.allure_step_json__screenshot(step_text="{}-输入失败".format(doc), content=result_dic)

            time.sleep(timewait)
            raise

    # 下拉框处理
    def select_ele(self, locator, index=None, text=None, value=None, center=True, timeout=15,timewait=0.3, doc=""):
        ele = self.wait_ele_visible(locator, center, timeout, doc)
        time.sleep(timewait)
        try:
            if index:
                Select(ele).select_by_index(index)
            if text:
                Select(ele).select_by_visible_text(text)
            if value:
                Select(ele).select_by_value(value)

            Logger.info("{}-下拉框元素{}选择：index-{}，text-{}，value-{}".format(doc, locator, index, text, value))
            self.allure_step_json__screenshot(step_text="{}-下拉框选择成功".format(doc), content="{}-下拉框选择成功".format(doc))
            time.sleep(timewait)

        except:
            Logger.exception("{}-下拉框元素选择失败-{}".format(doc, locator))
            Logger.exception("{}-下拉框元素{}选择：index-{}，text-{}，value-{} --【失败】".format(doc, locator, index, text, value))
            self.allure_step_json__screenshot(step_text="{}-下拉框选择失败".format(doc), content="{}-下拉框选择失败".format(doc))
            time.sleep(timewait)
            raise


    # 鼠标悬停
    def hover(self, locator, center=True, timeout=15,timewait=0.3, doc=""):
        ele = self.wait_ele_presence(locator, center, timeout, doc)
        time.sleep(timewait)
        #https://blog.csdn.net/jiachuan/article/details/108099705
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
            Logger.info("{}-元素{}鼠标悬停".format(doc, locator))
            self.allure_step_json__screenshot(step_text=doc, content="{}-元素{}鼠标悬停".format(doc, locator))
            time.sleep(timewait)
        except:
            Logger.exception("{}-元素悬停失败-{}".format(doc, locator))
            self.allure_step_json__screenshot(step_text=doc, content="{}-元素悬停失败-{}".format(doc, locator))
            time.sleep(timewait)
            raise

    # 查找元素
    def get_element(self, locator, doc="", center=True, timeout=15, timewait=0):
        ele = self.wait_ele_visible(locator, center, timeout, doc)
        time.sleep(timewait)

        try:
            Logger.info("{}-查找元素：{}".format(doc, locator))
            time.sleep(timewait)
            element=self.driver.find_element(*locator)

            self.allure_step_json__screenshot(step_text=doc, content="{}-查找元素：{}".format(doc, locator))
            return element
        except:
            Logger.exception("{}-元素查找失败-{}".format(doc, locator))
            self.allure_step_json__screenshot(step_text=doc, content="{}-元素查找失败-{}".format(doc, locator))
            time.sleep(timewait)
            raise



    # 查找匹配元素
    def get_elements(self, locator, center=True, timeout=15, timewait=0,doc="",mode=0):
        time.sleep(timewait)
        ele = self.wait_ele_visible(locator, center, timeout, doc)
        try:

           Logger.info("{}-查找所有匹配的元素：{}".format(doc, locator))

           elementdata=self.driver.find_elements(*locator)
           total=len(elementdata)

           data=''
           if mode==0:
               data=elementdata
           elif mode==1:
               data = total
           elif mode == 2:
               data = {"elements":elementdata,"total":total}
           data_ele = {"elements": str(elementdata), "total": total}

           self.allure_step_json__screenshot(step_text='{}查找所有匹配的元素：{}'.format(doc, locator[1]), content=str(data))
           time.sleep(timewait)
           return data

        except:
            Logger.exception("{}-元素集查找失败-{}".format(doc, locator))
            self.allure_step_json__screenshot(step_text='{}查找所有匹配的元素：{}'.format(doc, locator[1]), content="{}-元素集查找失败-{}".format(doc, locator))
            time.sleep(timewait)
            raise

    # 获取元素的属性
    def get_ele_attribute(self, locator, name, center=True, timeout=15, timewait=0, doc="获取元素的属性"):
        ele = self.wait_ele_presence(locator, center, timeout, doc)
        time.sleep(timewait)
        try:
            value = ele.get_attribute(name)
            Logger.info("{}-元素{}的{}属性-{}".format(doc, locator, name, value))
            time.sleep(timewait)
            self.allure_step_json__screenshot(step_text=doc, content="{}-元素{}的{}属性-{}".format(doc, locator, name, value))
            return value
        except:
            Logger.exception("{}-元素获取属性{}失败-{}".format(doc, name, locator))
            self.allure_step_json__screenshot(step_text=doc,
                                              content="{}-元素获取属性{}失败-{}".format(doc, name, locator))
            time.sleep(timewait)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, center=True, timeout=15,timewait=0, doc=""):
        ele = self.wait_ele_presence(locator, center, timeout, doc)
        time.sleep(timewait)
        try:
            text = ele.text
            Logger.info("{}-元素{}的文本内容-【{}】".format(doc, locator, text))
            time.sleep(timewait)
            self.allure_step_json__screenshot(step_text="获取元素text内容：{}".format(text), content="{}-元素{}的text内容-【{}】".format(doc, locator, text))
            return text
        except:
            Logger.exception("{}-元素获取文本失败-{}".format(doc, locator))
            self.allure_step_json__screenshot(step_text=doc, content="{}-元素获取文本失败-{}".format(doc, locator))
            time.sleep(timewait)
            raise

    # 获取元素的标签名
    def get_tag_name(self, locator, center=True, timeout=15,timewait=0, doc="获取元素的标签名"):
        ele = self.wait_ele_presence(locator, center, timeout, doc)
        time.sleep(timewait)
        try:
            tag_name = ele.tag_name
            Logger.info("{}-元素{}的标签名-{}".format(doc, locator, tag_name))
            time.sleep(timewait)
            self.allure_step_json__screenshot(step_text=doc, content="{}-元素{}的标签名-{}".format(doc, locator, tag_name))
            return tag_name
        except:
            Logger.exception("{}-元素获取标签名失败-{}".format(doc, locator))
            self.allure_step_json__screenshot(step_text=doc, content="{}-元素获取标签名失败-{}".format(doc, locator))
            time.sleep(timewait)
            raise

    # iframe处理
    def switch_iframe(self, iframe_reference, timeout=60,timewait=0, doc="进入切换iframe"):
        """"""
        time.sleep(timewait)
        #https://blog.51cto.com/u_15127619/4897451

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
    def scroll_window_element_visible(self, locator, doc="滚动查找元素至可见",timewait=0,):
        time.sleep(timewait)
        # 查找元素
        ele = self.get_element(locator, doc)
        # 开始滚动元素
        Logger.info("{} 滚动元素{}至页面可见".format(doc, locator))
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            self.allure_step_json__screenshot(step_text=doc,
                                              content="{} 滚动元素{}至页面可见".format(doc, locator))
            time.sleep(timewait)
        except:
            Logger.info("{} 滚动元素{}至页面可见失败".format(doc, locator))
            self.allure_step_json__screenshot(step_text=doc,
                                              content="{} 滚动元素{}至页面可见失败".format(doc, locator))
            raise

    # 退回上层表单
    def switch_parent_iframe(self, doc="退回上层iframe"):
        self.driver.switch_to.parent_frame()
        self.allure_step_json__screenshot(step_text=doc, content=doc)

        Logger.info(doc)


    # 退回初始表单
    def switch_default_iframe(self, doc="退回最外层iframe表单"):
        self.driver.switch_to.default_content()
        self.allure_step_json__screenshot(step_text=doc, content=doc)
        Logger.info(doc)



    # 刷新页面
    def page_refresh(self, doc="刷新页面"):
        self.driver.refresh()
        # driver.execute_script("location.reload()")
        self.allure_step_json__screenshot(step_text=doc, content=doc)
        Logger.info(doc)
    def get_title(self,doc='获取窗口句柄title'):
        title_name = self.driver.title
        Logger.info('获取窗口句柄title：“{}”'.format(title_name))
        self.allure_step_json__screenshot(step_text=doc, content='获取窗口句柄title：“{}”'.format(title_name))


        return title_name

    def exec_js(self, js, doc=''):
        Logger.info("{} 开始执行js语句： {}".format(doc, js))
        try:
            self.driver.execute_script(js)
            self.allure_step_json__screenshot(step_text=doc, content="{} 执行js语句： {}-成功".format(doc, js))
        except:
            Logger.exception("{} js 执行失败".format(doc))
            self.allure_step_json__screenshot(step_text=doc, content="{} 执行js语句： {}-失败".format(doc, js))
            raise



    def switch_to_window(self,handlelist='',tab_name='',handle='',mode=0,doc='',timewait=0.5,):
        '''


        '''

        Logger.info("切换句柄-{}".format(doc))
        if mode==0:
            if handle!="":
                self.driver.switch_to.window(handle)
                time.sleep(timewait)
                current_handle = self.driver.current_window_handle  # 获取浏览器当前句柄
                Logger.info("切换【{}】页面成功!-%s".format(tab_name, current_handle))
                #self.save_screenshot("切换【{}】页面成功".format(tab_name), step=False)
                self.allure_step_json__screenshot(step_text="切换句柄-{}".format(doc), content="切换【{}】页面成功!-%s".format(tab_name, current_handle))
            else:
                Logger.error("handle!="",请检查参数")
                self.allure_step_json__screenshot(step_text="切换句柄-{}".format(doc),
                                                  content="handle!="",请检查参数")
                raise
        elif mode==1:
            if handlelist!="" and tab_name!="" :
                tab_name_list=[]
                for hand in handlelist:
                    self.driver.switch_to.window(hand)
                    get_tab_name=self.driver.title
                    if get_tab_name==tab_name:
                        current_handle = self.driver.current_window_handle  # 获取浏览器当前句柄
                        time.sleep(timewait)
                        Logger.info("切换【{}】页面成功!-{}-{}".format(tab_name,current_handle,hand))
                        #self.save_screenshot("切换【{}】页面成功".format( tab_name), step=False)
                        self.allure_step_json__screenshot(step_text="切换句柄-{}".format(doc),
                                                          content="切换【{}】页面成功!-%s".format(tab_name, current_handle))
                        tab_name_list.append(get_tab_name)
                        break
                    else:
                        tab_name_list.append(get_tab_name)
                if tab_name not in  tab_name_list:
                    Logger.info(tab_name_list)
                    Logger.info("切换【{}】页面失败，没有找到这个句柄页面!-{}".format(tab_name, tab_name_list))
                    #self.save_screenshot("切换【{}】页面失败，没有找到这个句柄页面！".format(tab_name), step=False)
                    self.allure_step_json__screenshot(step_text="切换句柄-{}".format(doc),
                                                      content="切换【{}】页面失败，没有找到这个句柄页面!-{}".format(tab_name, tab_name_list))
                    raise
            else:
                Logger.error("“ndlelist!="" and tab_name!=""”,请检查参数")
                self.allure_step_json__screenshot(step_text="切换句柄-{}".format(doc),
                                                  content="“ndlelist!="" and tab_name!=""”,请检查参数")
                raise
        time.sleep(timewait)


    # 等待元素出现再消失
    def wait_ele_gone(self, locator, timeout=15, poll_frequency=0.5, doc="等待元素出现再消失"):

        #

        try:
            start = datetime.datetime.now()

            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
            #until是当某元素出现或什么条件成立则继续执行
            #https://blog.csdn.net/m0_66887922/article/details/124060624
            end = datetime.datetime.now()
            Logger.info("{}-元素{}已存在，等待{}秒".format(doc, locator, (end - start).seconds))
            WebDriverWait(self.driver, timeout, poll_frequency).until_not(EC.presence_of_element_located(locator))
            #until_not是当某元素消失或什么条件不成立则继续执行，参数也相同。
            end = datetime.datetime.now()
            Logger.info("{}-元素{}已消失，等待{}秒".format(doc, locator, (end - start).seconds))
            try:
                #self.save_screenshot("{}-成功".format(doc))
                self.allure_step_json__screenshot(step_text="{}".format(doc),
                                                  content="{}-成功-{}".format(doc,locator,))

            finally:
                return True
        except:
            #Logger.exception("{}-元素不消失-{}".format(doc, locator))
            self.allure_step_json__screenshot(step_text="{}".format(doc),
                                              content="{}-元素不消失-{}".format(doc, locator))
            try:
                #self.save_screenshot("{}-元素不消失".format(doc))
                self.allure_step_json__screenshot(step_text="{}".format(doc),
                                                  content="{}-元素不消失".format(doc))
            finally:
                return False

    # 断言元素文本包含指定值
    def assert_text(self, locator, expect_text, center=True, timeout=60,timewait=0.3, doc=""):
        time.sleep(timewait)
        try:

            text = self.get_text(locator, center, timeout)
            result = expect_text in text

            result_dic={
                "期望":expect_text,
                "实际":text,
                "结果":"%s (包含或相等)"%result
            }

            #     allure.attach(json.dumps(result_dic, ensure_ascii=False, indent=4),'断言结果：%s'%result,allure.attachment_type.JSON )
            Logger.info('{}-元素{}文本预期为"{}"，实际为"{}"，用例执行结果为- [{}]'.format(doc, locator, expect_text, text, result))
            try:
                #self.save_screenshot("{}-{}".format(doc, result),step=False)
                self.allure_step_json__screenshot(step_text="{}-断言：{}".format(doc,result),
                                                  content=result_dic)
            finally:

                return result
        except:
            #Logger.exception("{}-获取文本失败，用例执行失败！！！".format(doc))
            self.allure_step_json__screenshot(step_text="{}-断言：{}".format(doc,"False"),
                                              content="{}-获取文本失败，用例执行失败！！！".format(doc))

            return False

        # 点击操作
    def get_window_handle(self,  mode=0,  doc=""):

        #获取当前的窗口句柄
        window1 = self.driver.current_window_handle
        # 获取所有打开的窗口句柄
        all_windows = self.driver.window_handles
        # print("当前句柄：%s"%window1)
        # print("所有句柄：%s"%all_windows)
        window1_handle={}
        if mode==0:
            window1_handle= window1
        elif mode==1:
            window1_handle=all_windows
        elif mode==2:
            window1_handle= {"window1":window1,"all_windows":all_windows}

        #self.save_screenshot("{}-获取窗口句柄".format(doc), step=False)
        #Logger.info('获取窗口句柄-{},获取结果{}'.format(doc,{"window1":window1,"all_windows":all_windows}))

        self.allure_step_json__screenshot(step_text='获取窗口句柄-{}'.format(doc),
                                          content=window1_handle)
        return window1_handle


    def upload_file_notInput(self, locator, file, doc=''): #非 input类型标签的上传
        import pyautogui
        import win32gui
        import win32con
        Logger.info("{0} {1}文件上传 {2}".format(doc, locator, file))
        self.click_element(locator,mode=3, doc='点击上传按钮，进入文件选择界面')
        time.sleep(0.5)
        # 输入文件地址
        try:
            dialog = win32gui.FindWindow("#32770", "打开")  # 对话框
            # 向下传递
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)  # 二级
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)  # 三级
            # 编辑按钮
            Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入Edit对象的句柄
            # 打开按钮
            button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
            time.sleep(0.5)
            # 输入文件的绝对路径，点击打开按钮
            win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None,file)
            time.sleep(1)
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
            self.allure_step_json__screenshot(step_text='{}-文件上传'.format(doc),
                                              content="{0} {1}文件上传 {2}".format(doc, locator, file))
        except:
            Logger.exception("{} 文件上传失败".format(doc))
            self.allure_step_json__screenshot(step_text="{} 文件上传失败".format(doc).format(doc),
                                              content="{} 文件上传失败".format(doc))
            raise



#     # 断言元素属性包含指定值
#     def wait_attribute_tobe(self, locator, attribute, expect_value, timeout=60, poll_frequency=0.5, doc=""):
#         try:
#             start = datetime.datetime.now()
#             if attribute == "text":
#                 WebDriverWait(self.driver, timeout, poll_frequency).until(EC.text_to_be_present_in_element(locator, expect_value))
#             else:
#                 WebDriverWait(self.driver, timeout, poll_frequency).until(attribute_tobe(locator, attribute, expect_value))
#             end = datetime.datetime.now()
#             Logger.info(
#                 "{}-元素{}的{}变为{}-成功，等待{}秒".format(doc, locator, attribute, expect_value, (end - start).seconds))
#             try:
#                 self.save_screenshot("{}-成功".format(doc))
#             finally:
#                 return True
#         except:
#             Logger.exception("{}-元素{}的{}变为{}-失败！！！：".format(doc, locator, attribute, expect_value))
#             try:
#                 self.save_screenshot("{}-失败".format(doc))
#             finally:
#                 return False
#
#
# class attribute_tobe(object):
#
#     def __init__(self, locator, attribute, expect_value):
#         self.locator = locator
#         self.attribute = attribute
#         self.expect_value = expect_value
#
#     def __call__(self, driver):
#         try:
#             element_value = _find_element(driver, self.locator).get_attribute(self.attribute)
#             result = self.expect_value in element_value
#             return result
#         except:
#             return False


# def _find_element(driver, by):
#     try:
#         return driver.find_element(*by)
#     except:
#         raise


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("www.baidu.com")
    test = BasePage(driver)
    # test.
