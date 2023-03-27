"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import time
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
"""
1，sleep 强制等待
优点：代码简洁，简单明了。
缺点：如果设置sleep等待时间过短，元素还没加载出来，程序报错，sleep设置等待时间过长，
    元素早就加载出来了，程序还在等待，浪费时间，影响代码整体的运行效率。
time.sleep(3)    

2，implicitly_wait() 隐式等待
优点：
a、代码简洁。
b、在代码前部分加implicitly_wait(10),整个的程序运行过程中都会有效（作用于全局，
直接在初始化driver的后面加，后面的代码都会受影响），都会等待元素加载完成。
c、在设置的时间内没有加载到整个页面，则会报错，如果元素在第10s被加载出来，自动执行下面的脚本，不会一直等待10s。

缺点：
a、非要加载到整个页面才执行代码，这样影响代码的执行效率，一般情况下，我们想要的结果是只加载到了我要定位的元素就执行代码，
不需要等待整个页面的完全加载出来再执行代码。

3，WebDriverWait() 显示等待
优点：代码执行效率快。无需等待整个页面加载完成，只需加载到你要定位的元素就可以执行代码。是最智能的设置元素等待的方式

缺点：
a、导入三个包比较麻烦 EC WebDriverWait  By
b、写等待时间的代码比较复杂


"""
#实例化浏览器驱动
driver = webdriver.Chrome()
#窗口最大话
driver.maximize_window()
#打开百度
driver.get("http://www.baidu.com")
#强制等待
sleep(3)
#隐式等待
driver.implicitly_wait(10)
#显示等待
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw')))
driver.find_element('kw').click()
driver.find_element('kw').send_keys('哈哈')

