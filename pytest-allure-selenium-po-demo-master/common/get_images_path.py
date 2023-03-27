#!/user/bin/env python3
# -*- coding: utf-8 -*-
import random,os
def get_images_list(n):  # 获取随机图片路径
    images_path=r'F:\测试资源图\故障图_png'
    images_name_list=os.listdir('./images')#'./images'
    getcwd=os.getcwd()
    images_name_list_n=random.sample(images_name_list, int(n))

    images_path_list = ['%s\\images\\%s'%(getcwd,x)  for x in images_name_list_n]
    #images_path_list = [os.path.join(images_path,x) for x in images_name_list_n]
    return images_path_list

