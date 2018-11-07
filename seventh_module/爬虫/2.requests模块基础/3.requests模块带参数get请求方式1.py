# -*- coding: utf-8 -*-

# __title__ = '3.requests模块带参数get请求方式1.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.07'


# 需求： 指定一个词条，获取搜狗搜索结果所对应的页面数据

import requests

url = 'https://www.sogou.com/web?query=唐嫣&ie=utf-8'


response = requests.get(url=url)

page_text = response.text   # str类型
# page_text = response.content  #bytes 类型

with open('./data_storage/tangyan.html','w',encoding='utf-8') as  fp:
	fp.write(page_text)






