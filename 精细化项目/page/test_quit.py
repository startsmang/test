from selenium  import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait   # 显示等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains     # 动作链
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
def test_quit():
    driver.get('https://jxh.zx1026.com/')
    driver.maximize_window()
