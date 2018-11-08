# -*- coding: utf-8 -*-

# __title__ = '11.requests模块的代理操作.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.08'


import requests

url = 'http://www.baidu.com/s?ie=utf-8&wd=IP'
# 将代理IP封装到字典中
# http://www.goubanjia.com/  类型为key IP:PORT为值
proxy = {
	'http':'31.29.212.82:35066'
}
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}
# 更换网络IP
response = requests.get(url=url,proxies=proxy,headers=headers)
with open('./data_storage/daili.html','w',encoding='utf-8') as fp:
	fp.write(response.text)





