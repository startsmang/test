"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui
import win32gui
import win32con
"""
带有input标签并且type属性的值为file可直接使用send_keys方法上传文件


"""


#上传非input标签
driver = webdriver.Chrome()
driver.get(r"http://sahitest.com/demo/php/fileUpload.htm")
driver.maximize_window()
driver.implicitly_wait(10)
# time.sleep(1)

element=driver.find_element(By.XPATH,'//*[@id="file5"]')
ActionChains(driver).click(element).perform() #点击上传按钮

# if browser_type.lower() == 'chrome':
#     title = '打开'
# elif browser_type.lower() == 'Firefox':
#     title = '文件上传'
# elif browser_type.lower() == 'ie':
#     title = '选择要加载的文件'
# log.info('本次使用{0}进行上传操作'.format(browser_type))
# 一级顶层窗口，此处title为上传窗口名称，浏览器不一样上传窗口名称不一样,加程序休眠
time.sleep(2)
dialog = win32gui.FindWindow("#32770", "打开")
# 二级窗口
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
# 三级窗口
comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
# 四级窗口
edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)

file=os.path.join(os.getcwd(),"__init__.py") #输入文件的绝对路径
# 执行操作 输入文件路径
win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file)
# 点击打开上传文件
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)



# ActionChains(driver).click(element).perform() #点击上传按钮
#
#
# # pyautogui.moveTo(68,190,0.2)
# # pyautogui.leftClick()
#
# #找元素，一级窗口“#32770”，打开
# time.sleep(1)
# dialog = win32gui.FindWindow("#32770","打开") #对话框
# #向下传递
#
# ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,'ComboBoxEx32',None) #二级
#
# ComboBox = win32gui.FindWindowEx(ComboBoxEx32,0,'ComboBox',None) #三级
#
# #编辑按钮
# Edit = win32gui.FindWindowEx(ComboBox,0,'Edit',None) #上面三句依次寻找对象，直到找到输入Edit对象的句柄
#
# #打开按钮
# button = win32gui.FindWindowEx(dialog,0,'Button',None) #确定按钮Button
# time.sleep(1)
#
# file=os.path.join(os.getcwd(),"__init__.py") #输入文件的绝对路径
# #输入文件的绝对路径，点击打开按钮
# win32gui.SendMessage(Edit,win32con.WM_SETTEXT,None,file)
#
# time.sleep(1)
# win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button) #点击打开按钮








input("...")
driver.quit()


