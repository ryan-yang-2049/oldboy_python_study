# -*- coding: utf-8 -*-

# __title__ = '2.爬取古诗文网中三国小说里的标题和内容.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.09'


# 需求：爬取古诗文网中三国小说里的标题和内容

import requests
from bs4 import BeautifulSoup

def get_content(url):
	page_text = requests.get(url=url,headers=headers).text
	soup = BeautifulSoup(page_text,'lxml')
	div = soup.find('div',class_='chapter_content')
	content = div.text
	return content


url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}

page_text = requests.get(url=url,headers=headers).text

# 数据解析
soup = BeautifulSoup(page_text,'lxml')
title_list = soup.select('.book-mulu > ul > li > a')
# print(type(title_list[0]))    # <class 'bs4.element.Tag'>
# 注意：Tag类型的对象可以继续调用响应的解析属性和方法进行局部数据的解析

for item in title_list:
	title = item.string
	content_url = 'http://www.shicimingju.com'+item.attrs['href']
	# print(title,content_url)
	content = get_content(content_url)

	with open('./data/%s.txt'%title,'w',encoding='utf-8') as fp:
		fp.write(content)


