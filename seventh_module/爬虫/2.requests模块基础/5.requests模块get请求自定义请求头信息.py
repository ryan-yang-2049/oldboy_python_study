# -*- coding: utf-8 -*-

# __title__ = '5.requests模块get请求自定义请求头信息.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.07'


# 需求： 指定一个词条，获取搜狗搜索结果所对应的页面数据
import requests
url = 'https://www.sogou.com/web'
# 将参数封装到字典中
params = {
	'query': '唐嫣',
	'ie' : 'utf-8'
}

# 自定义请求头信息
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}
response = requests.get(url=url,params=params,headers=headers)
print(response.status_code)
print(response.content)






