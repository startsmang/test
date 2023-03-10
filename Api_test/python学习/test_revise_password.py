import pytest
import requests
from utils.read_files_tools.yaml_control import GetYamlData
@pytest.mark.parametrize('phone',)
def test_login():
    url ='https://jxh-api.zx1026.com/User/Register/getPublicUserTokenByTel',

    data = {
        'telephone' : GetYamlData()
    }
@pytest.mark.parametrize('phone',)
def test_revise(self,phone):
    url = '1'
    headers = {

    }
    data = {
    'new':'888888yy',
    'phone':' '+phone,
    'code':'123456'
}
    res = requests.request('post',url = url ,data=data,headers=headers)