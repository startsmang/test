from selenium import webdriver
import  pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait   # 显示等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains     # 动作链
from time import sleep
driver = webdriver.Chrome()
def test_login():
    driver.get('https://jxh.zx1026.com/')
    driver.maximize_window()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/button[1]').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/div[1]/div/div[1]/input').send_keys('19974756755')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/div[2]/div/div/input').send_keys('888888yy')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/button').click()
    sleep(3)
    name = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[5]/span').text
    assert '声琪' in name
def test_chengGuan():
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[6]/div[1]/div[2]/div[2]/div').click()
    sleep(1)
    text = driver.find_element(By.XPATH,'//*[@id="breadcrumb-container"]/span/span[2]/span[1]/span').text
    assert '问题汇总' in text

def test_delete_workOrder():
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div/div/div[4]/div/div[5]/div[2]/table/tbody/tr[2]/td[17]/div/div/span[2]').click()
    sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/button[2]/span').click()
    sleep(1)
    assert '删除成功' in driver.page_source

# def test_quit():
#     driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[5]/div[3]/div/img').click()
#     sleep(1)
#     driver.find_element(By.CSS_SELECTOR,'#dropdown-menu-1283 > li:nth-child(2) > span').click()
#     sleep(1)
#     tittle = driver.find_element(By.XPATH,'//*[@id="app"]/div/section[2]/p[1]').text
#     assert '福城管' in tittle
if __name__ == '__main__':
    pytest.main(['--vs'])

