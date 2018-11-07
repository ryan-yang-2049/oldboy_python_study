# -*- coding: utf-8 -*-

# __title__ = '2.response常用属性.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.07'


# 需求：爬取搜狗首页的页面数据
import requests
# 指定url
url = 'https://www.sogou.com'
# 发起get请求 : get方法会返回请求成功的响应对象
response = requests.get(url=url)

# content ：获取的是响应对象(response)中二进制(byte)类型的页面数据
print(response.content)

# status_code : 返回响应状态码
print(response.status_code)

# headers : 获取响应头信息
print(response.headers)

# url : 获取请求的url
print(response.url)



