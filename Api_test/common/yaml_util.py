import yaml
import os

class YamlUtil:
    # 读取extract.yml

    def read_extract_yaml (self,key):
        with open(os.getcwd()+"./extract.yml",mode='r',encoding='utf-8')as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]
    #     写入extract.yml
    def  write_extract_yaml(self,data):
        with open (os.getcwd()+"./extract.yml",mode = 'a',encoding='utf-8')as f :
            yaml.dump(data=data,stream= f,allow_unicode=True)

    # 清除extratt.yml文件
    def  clear_extract_yaml(self):
        with open (os.getcwd()+"./extract.yml",mode = 'a',encoding='utf-8')as f :
            f.truncate()
#     读取测试用例的yml文件
    def read_test_yaml (self,yaml_name):
        with open(os.getcwd()+"./testcases/"+yaml_name,mode='r',encoding='utf-8')as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value

