# -*- coding: utf-8 -*-

# __title__ = '9.requests综合项目实战.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.07'

# 需求：爬取搜狗知乎某一个词条对应一定范围页码表示的页面数据
# 获取前三页数据
import requests
import os
if not os.path.exists('./pages'):
	os.mkdir('./pages')
url = 'http://zhihu.sogou.com/zhihu'
word = input("enter a word:")
#动态指定页码的范围：
start_pageNum = 1
end_pageNum = 3
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}
for page in range(start_pageNum,end_pageNum+1):
	param = {
		'query':word,
		'page':page,
		'ie':'utf-8',
	}
	response = requests.get(url=url,params=param,headers=headers)
	page_text = response.text
	with open('./pages/%s_%s.html'%(word,page),'w',encoding='utf-8') as fp:
		fp.write(page_text)







