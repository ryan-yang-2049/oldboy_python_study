# -*- coding: utf-8 -*-

# __title__ = '7.requests模块ajax的get请求.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.07'


# 需求：抓取肯德基城市餐厅数据
import requests
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
data = {
	"cname":"",
	"pid":"",
	"keyword":"上海",
	"pageIndex":"1",
	"pageSize":"100",
}
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}
response = requests.post(url=url,data=data,headers=headers)
print(response.text)

