"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

"""
多表单切换

1，什么是表单
就是网页标签名为iframe或frame的元素，表单引用了其他页面的链接，真正的页面数据没有出现在源码中，
但是 在浏览器中可以看见，与浏览器的多个窗口类似

2，为什么需要切换
在web应用会遇到iframe或frame表单嵌套的应用，
selenium的webdriver只能在一个页面对元素操作以及定位，对表单里的元素无法直接定位，此时需要切换到表单页面再进行定位

表单切换方法1，switch_to.frame('id的值')，这个方法是默认取表单的ID的值或name属性的值进行定位
表单切换方法2，先定位到表单，再切换到表单，然后才能正常定位到表单内的元素

如果iframe有ID：switch_to.frame('id的值')
如果iframe没有ID：driver.find_element_by_tag_name('iframe')
                driver.switch_to_frame(a)
释放iframe表单返回主页：driver.switch_to_default_content()
切换到上一级iframe,如果没有上一级，那就保留在当前页面
    driver.switch_to.parent_frame()
"""
#实例化浏览器驱动
driver = webdriver.Chrome()
#窗口最大话
driver.maximize_window()
#打开百度
driver.get(r"http://23432me_demo.html")

#切换到iframe
driver.switch_to.frame('if')
driver.find_element(By.XPATH,'//*[@id="toolbar-search-input"]').click()
driver.find_element(By.XPATH,'//*[@id="toolbar-search-input"]').send_keys('哈哈')