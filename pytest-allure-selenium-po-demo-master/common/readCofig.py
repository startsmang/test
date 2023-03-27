# coding:utf-8
#heboqiang

import os
import configparser

#获取当前路径下的配置文件
configpath  = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + r"\config\config.ini")
conf = configparser.ConfigParser()

# conf.read(configpath,encoding="utf-8")
conf.read(configpath,encoding="utf-8-sig")

#获取配置文件中的key值
browerType = conf.get('BrowserType','type')
timeout = conf.get('WaitTime','WaitTime')
Environ = conf.get('Environ','Environ')

# print(browerType)



