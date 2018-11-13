# -*- coding: utf-8 -*-

# __title__ = '3.爬取图片.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.09'


import requests
from bs4 import BeautifulSoup


url = 'http://jandan.net/ooxx/'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text

soup = BeautifulSoup(page_text,'lxml')

img_url = soup.select('li  .row > .text > p > img')
print(img_url)





