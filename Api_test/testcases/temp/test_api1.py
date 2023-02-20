import  requests
import pytest

def test_api1 ():
    url = 'https://cg.zx1026.com:6706/Cs/Cs/test1'
    headers ={


    }
    res = requests.request("post",url = url , headers = headers).json()
    print(res)

if __name__ == '__main__':
    pytest.main(['-vs','test_api.py'])