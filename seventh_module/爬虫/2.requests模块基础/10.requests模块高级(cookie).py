# -*- coding: utf-8 -*-

# __title__ = '10.requests模块高级(cookie).py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.08'

# 需求：爬取张三用户的豆瓣网的个人主页页面数据

import requests
session = requests.session()

# 1.发送登陆请求：将cookie获取，且存储到session对象中
login_url = 'https://accounts.douban.com/login'

data = {
	'source':'movie',
	'redir':'https://movie.douban.com/',
	'form_email':'461580544@qq.com',
	'form_password':'Ryan!@99',
	'login':'登录'
}
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}
# 使用session发起post请求
login_response = session.post(url=login_url,data=data,headers=headers)

# 2.对个人主页发起请求(session),获取响应页面数据
url = 'https://www.douban.com/people/84385895/'
response = session.get(url=url,headers=headers)
page_text = response.text

with open('./data_storage/douban_person.html','w',encoding='utf-8') as fp:
	fp.write(page_text)


