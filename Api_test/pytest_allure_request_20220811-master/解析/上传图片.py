#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/11 20:28
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 上传图片.py
# @Software: PyCharm
#-------------------------------------------------------------------------------

import requests
from requests_toolbelt import MultipartEncoder
import os
def hy_files():
    url='https://cg.zx1026.com:6706/Common/Upload/file' # 传图片
    headers={
        "token": "c09fd8bd8a119f7af49e2aaf92aca8ff",
    }
    data = MultipartEncoder(

        fields={
            "thumb":"1",
            "file": ('1.jpg',
                             open('D:/MyGit/Api_test/config/1.jpg', 'rb'),
                             "image/jpeg"),

        }
    )
    headers["Content-Type"] = data.content_type
    r=requests.request(url=url,method='post',headers=headers,data=data)#,data=data
    print(r.text)

hy_files()
