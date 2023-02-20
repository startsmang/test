import requests
import pytest

from Api_test.common.yaml_util import YamlUtil

def test_login():
    url ='https://cg.zx1026.com:6706//User/UserApp/loginWxMiniApp'
    headers = {

    "Accept":"*/*",
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive',
    'token':''

    }
    data = {
    'code':'2',
    "telephone":'19974756755'
    }
    res = requests.request("post",url=url ,headers = headers ,data=data ).json()['data']['token']
    YamlUtil().write_extract_yaml({'token': res})
def test_add_breed():
    value= YamlUtil().read_extract_yaml('token')
    url = 'https://cg.zx1026.com:6706//DogmsOpenApi/dogs/add'
    print(value)
    headers ={
        "token" : value,
        'Accept': '*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    data ={
        "breed_id":"1",
        "color_id" : "2",
        "sex":"1",
        "sterilization":"0",
        "birthday":"2017-08-05",
        "vaccine_type":"1",
        "vaccine_number":"88888888218956266",
        "vaccine_date":"2021-09-05",
        "vaccine_front":"36466",
        "vaccine_back":"36466",
        "upload_head":"36466",
        "upload_top":"36466",
        "upload_front":"36466",
        "bind_type":"1",
        "bind_id":"57",
        "user_id":"154",
        "hospital_id":"9",

    }
    resource = requests.request("post",url = url ,headers = headers,data = data).json()
    print(resource)
