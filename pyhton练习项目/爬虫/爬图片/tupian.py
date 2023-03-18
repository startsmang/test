from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait   # 显示等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains     # 动作链
import time
import re
import requests
import os.path
import csv
driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
# url ='http://www.xiannvku.cc/?ref=www.ooee2022.top' /* 首页*/
url = 'https://www.tisun.ltd/2022/03/30/%e5%94%90%e5%ae%89%e7%90%aa%e5%86%99%e7%9c%9f/'
header={
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
"content-length": "0",
"content-type": "text/plain",
"origin": 'http://www.xiannvku.cc',
"referer": "http://www.xiannvku.cc/",
"sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "cross-site",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
}
driver.get(url)  # 对网页发送请求
driver.maximize_window()

time.sleep(3)
data_src_url= [ ]
time.sleep(1)
data_src=driver.find_element(By.XPATH,"/html/body/main/div/div/article/div[3]/div[1]/figure[1]/figure/img").get_attribute('data-srcset')
print(data_src)
img_url = re.findall(r'768w, (.*?) 994',data_src)
print(img_url)
data_src_url.append(img_url)
print(data_src_url)

if __name__ == '__main__':
    pass


# mood = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/center/img[1]'))) # 找到热门表情包点击
# mood.click()    # 找到热门表情包点击
# time.sleep(1)
# chains = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div')))  # 移动到页面末尾，加载元素
# ActionChains(driver).move_to_element(chains).perform()  # 开始移动
# time.sleep(3)
# res = requests.request("post",url=url ,headers=header)
#
# title = driver.find_element(By.XPATH, '/html/body/div[3]/center/img').get_attribute('alt')
# if len(title) >= 295:  # 判断 处理因标题过长而保存不了图片
#     title = 'not'
# ditail = driver.find_element(By.XPATH, '//*[@id="pages"]/a').get_attribute('href')  # 获取详细页
# images = driver.find_element(By.XPATH, '/html/body/div[3]/center/img').get_attribute('src')  # 获取图片链接
#
# print(title,ditail,images)
