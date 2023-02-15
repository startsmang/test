import yaml
import os

class YamlUtil:
    # 读取extract.yml

    def read_extract_yaml (self,key):
        with open(os.getcwd()+"/extract.yml",mode='r',encoding='utf-8')as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value
    #     写入extract.yml
    def  write_extract_yaml(self,data):
        with open (os.getcwd()+"/extract.yml",mode = 'w',encoding='utf-8')as f :
            yaml.dump(data=data,stream=f,allow_unicode=True)