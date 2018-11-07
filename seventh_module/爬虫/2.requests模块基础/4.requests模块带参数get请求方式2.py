# -*- coding: utf-8 -*-

# __title__ = '3.requests模块带参数get请求方式1.py'
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
response = requests.get(url=url,params=params)
print(response.status_code) # 查看响应状态
print(response.content) # 查看响应内容

