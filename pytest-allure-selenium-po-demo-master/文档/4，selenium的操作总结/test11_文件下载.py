"ddd"
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui
"""


"""

options = webdriver.ChromeOptions()

#profile.default_content_settings.popups：设置为 0 禁止弹出窗口 download.default_directory：设置下载路径
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r'D:\daima\xin-daima\kejian\webUI自动化测试\4，selenium的操作总结'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=options)

driver.get('http://npm.taobao.org/mirrors/chromedriver/2.13/')
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/table/tbody/tr[4]/td[2]/a').click()
time.sleep(3)
driver.quit()
