#!/user/bin/env python3
# -*- coding: utf-8 -*-





from urllib import parse
import requests
import json
from test. common.logger import Logger

def login(addr,loginAccount,password):
	url = "%s/risk_tongji/memberService/login.html"%addr
	payload = json.dumps({
		"loginAccount": loginAccount,
		"password": password,
		"verifyCode": "",
		"randomCode": "",
		"sourceType": "3"
	})
	headers = {
		'Content-Type': 'application/json'
	}
	try:
		response = requests.request("POST", url, headers=headers, data=payload)
		# Logger.info(response.text)
		# Logger.info(type(response.text))
		data=response.json()
		if data['code']=="10000":
			return data
		else:
			Logger.error('登录请求失败……【%s】' % data)
			raise '登录请求失败……【%s】' % data

	except Exception as e:
		Logger.error('登录请求失败……【%s】'%e)
		raise '登录请求失败……【%s】'%e


def login_Cookie(addr,loginAccount,password):
	data=login(addr, loginAccount, password)
	memberInfo=parse.quote(json.dumps(data['data']['memberInfo']))#json.dumps(data['data']['memberInfo'])
	token=json.dumps(data['data']['memberInfo']['token'])

	return {"Admin-UserInfo": memberInfo,'sidebarStatus':0,'Admin-Token': token}
