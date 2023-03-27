import os
import sys
from common.logger import Logger
from common.readCofig import Environ
import yaml

class ReadYaml():
    def __init__(self,filename):
        Logger.info(Environ)
        self.filepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + Environ+"/"+filename)#拼接定位到data文件夹
        Logger.info(self.filepath)

    def get_yaml_data(self):
        #print(self.filepath)
        with open(self.filepath, "r", encoding="utf-8")as f:
            # 调用load方法加载文件流
            return yaml.load(f,Loader=yaml.FullLoader)

if __name__ == '__main__':
    data = ReadYaml("data.yaml").get_yaml_data()  # 读取数据
    Logger.info(data)

