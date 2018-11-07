# -*- coding: utf-8 -*-

# __title__ = '6.requests模块的post请求.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.07'


# 登陆豆瓣网，获取登成功后的页面数据
import requests
# 1.指定 post 请求的url
url = 'https://accounts.douban.com/login'
# 2.封装post的请求
data = {
	'source':'movie',
	'redir':'https://movie.douban.com/',
	'form_email':'461580544@qq.com',
	'form_password':'Ryan!@99',
	'login':'登录'
}
# 自定义请求头信息
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}

# 3.发起post请求
response = requests.post(url=url,data=data,headers=headers)

# 4.获取响应对象中的页面数据
page_text =response.text

# 5.持久化操作
with open('./data_storage/douban.html','w',encoding='utf-8') as fp:
	fp.write(page_text)


