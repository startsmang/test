import requests
def test_add_breed():
    url = 'http://www.wisdom.com:8003/DogmsOpenApi/dogs/add'
    headers ={
        "token" : "337fafd16f10e7bde184100d4509171d",
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': 'jxh-api.zx1026.com',
        'Connection': 'keep-alive'
    }
    data ={
        "breed_id":"1",
        "color_id" : "2",
        "sex":"1",
        "sterilization":"0",
        "birthday":"2017-08-05",
        "vaccine_type":"1",
        "vaccine_number":"888888882155133",
        "vaccine_date":"2021-09-05",
        "vaccine_front":"36466",
        "vaccine_back":"36466",
        "upload_head":"36466",
        "upload_top":"36466",
        "upload_front":"36466",
        "bind_type":"1",
        "bind_id":"57",
        "user_id":"173",
        "hospital_id":"9",

    }
    resource = requests.request("post",url = url ,headers = headers,data = data).json()
    print(resource)
