# -*- coding: utf-8 -*-

# __title__ = '7.requests模块ajax的get请求.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.07'


# 需求：抓取豆瓣网上电影的详情数据

import requests
url = 'https://movie.douban.com/j/chart/top_list'

# 封装ajax请求中携带的get参数
params = {
	"type": "13",
	"interval_id": "100:90",
	"action":"",
	"start":"0",    # 起始位置
	"limit": "200"  # 限制条数
}
# 自定义请求头信息
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}
response = requests.get(url=url,params=params,headers=headers)

print(response.text)






