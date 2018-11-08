# -*- coding: utf-8 -*-

# __title__ = '3.爬取美女图片.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.08'

import re
import requests


headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}

url = 'http://pic.hao123.com/meinv'


params = {
"v":"1541669047200",
"act":"type"
}

response = requests.get(url=url,params=params,headers=headers)
# print(response.status_code)

page_text = response.text
# print(page_text)
# img_list = re.findall(r'<div class="pic-item" .*?>.*?<img src="(.*?)" .*?>.*?<div>',page_text,re.S)
#
# print(img_list)

# http://img.hb.aicdn.com/32847bcf70041722b1f16754f3d53f662c9b77549bf5-xKZFUq_fw658
