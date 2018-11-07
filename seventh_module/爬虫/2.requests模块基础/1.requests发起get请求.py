# -*- coding: utf-8 -*-

# __title__ = '1.requests发起get请求.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.07'

# 需求：爬取搜狗首页的页面数据
import requests
# 指定url
url = 'https://www.sogou.com'
# 发起get请求 : get方法会返回请求成功的响应对象
response = requests.get(url=url)
# 获取响应中的数据值: text 可以获取响应对象中字符串形式的页面数据
page_data = response.text
# 持久化操作
with open('./data_storage/sougou.html','w',encoding='utf-8') as fp:
	fp.write(page_data)









