from selenium import webdriver


def OpenBrowser():
    driver = webdriver.Chrome()
    driver.maximize_window()  #最大化窗口
    return driver