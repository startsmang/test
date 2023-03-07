import pytest
import requests
import yaml
from


@pytest.mark.parametrize('phone',)
def test_login():
    url ='https://jxh-api.zx1026.com/User/Register/getPublicUserTokenByTel',

    data = {
        'telephone' : ''
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