import requests
import pytest
class TestSendRequest:
    token = ""
    def test_get_token(self):
        url = 'https://jxh-api.zx1026.com//User/Login/getToken'
        headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
        "content-type": "application/json;charset=UTF-8"
        }
        params = {
        "account": "19974756755",
        "password": "888888",
        "login_type": "2",
        "user_type": "1",
        }
        response = requests.get(url = url,headers=headers,params=params)
        TestSendRequest.token = response.json()['data']['token']
        print(TestSendRequest.token)
    def test_obtain_woke_number(self):
        url = "https://jxh-api.zx1026.com//ProblemTicket/Emergency/getInfo"
        headers ={
            "token":TestSendRequest.token,
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 Edg/110.0.1587.41",

        }
        params = {
        "id":"2433"
        }
        res = requests.request("get",url = url ,params=params,headers = headers).json()['data']['work_number']
        print(res)
    def test_file_upload(self):
        url = 'https://jxh-api.zx1026.com//Common/Upload/file'
        headers = {
        'token':TestSendRequest.token,
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 Edg/110.0.1587.41",
        }
        data={
            "file" : open("D:/MyGit/img/01c8f15aeac135a801207fa16836ae.jpg@1280w_1l_2o_100sh.jpg", 'rb')
        }

        res = requests.request("post",url=url,headers=headers,files=data).json()['data']['url']
        print(res)
if __name__ == '__main__':
    pytest.main([ ' '])


