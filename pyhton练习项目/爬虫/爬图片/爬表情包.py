# @Author : 王同学
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



driver = webdriver.Chrome() # 创建浏览器对象

wait = WebDriverWait(driver,10)

def get_conten(url):
    driver.get(url) # 对网页发送请求
    time.sleep(1)
    # mood = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/center/img[1]'))) # 找到热门表情包点击
    # mood.click()    # 找到热门表情包点击
    # time.sleep(1)
    chains = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[1]/div')))    # 移动到页面末尾，加载元素
    ActionChains(driver).move_to_element(chains).perform()  # 开始移动
    time.sleep(3)


def get_data():
    all_data = []   # 定义列表 储存数据
    n = 1
    # while n < 6:    # 设置循环,翻页次数
    #     print(f'================================================正在爬取第{n}页的数据===========================================')
    #     time.sleep(2)

    all = wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[3]/center/img')))   # 直到元素出现,继续往下执行

    for i in all:
        title = i.find_element(By.XPATH,'/html/body/div[3]/center/img').get_attribute('alt')
        if len(title) >= 295:   # 判断 处理因标题过长而保存不了图片
            title = 'not'
        ditail = i.find_element(By.XPATH,'//*[@id="pages"]/a[]').get_attribute('href')   # 获取详细页
        images = i.find_element(By.XPATH,'/html/body/div[3]/center/img').get_attribute('src')    # 获取图片链接
        item = {
            '标题': title,
            '详情页': ditail,
            '图片': images
        }
        print(item)
        all_data.append(item)
        save_Images(images,title)
        save_csv(all_data)
    # 翻页
    time.sleep(2)
    page = wait.until(EC.presence_of_element_located((By.LINK_TEXT,'下一页')))
    if page.get_attribute('href'):
        page.click()
        n += 1
print('======================爬取结束==================================')
 # 手机号校验 正则





def save_csv(all_data):
    # 表头
    headers = ['标题','详情页','图片']
    with open('表情包.csv',mode='w',encoding='utf-8',newline='')as f:
        filt = csv.DictWriter(f,headers)
        filt.writeheader()
        filt.writerows(all_data)



def save_Images(images,title):
    if not os.path.exists('./表情包/'):
        os.mkdir('./表情包/')
    image_data = requests.get(url=images).content
    big = '[?<>/\|():!"*]'
    new_title = re.sub(big,"",title)
    with open('./表情包/' + new_title + '.jpg',mode='wb')as f:
        f.write(image_data)
        print('正在保存图片===>:',title)



def main():
    url = 'http://www.xiannvku.cc/pic/show-21201-1.html'
    get_conten(url)
    get_data()


if __name__ == '__main__':
    main()
