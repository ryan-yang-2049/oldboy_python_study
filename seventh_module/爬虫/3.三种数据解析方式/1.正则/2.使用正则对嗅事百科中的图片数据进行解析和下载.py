# -*- coding: utf-8 -*-

# __title__ = '2.使用正则对嗅事百科中的图片数据进行解析和下载.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.08'

import requests
import re
import os

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}

url = 'https://www.qiushibaike.com/pic/'

# 发起请求
response = requests.get(url=url,headers=headers)

# 获取页面数据
page_text = response.text

# 数据解析
'''
	<div class="thumb">
		<a href="/article/121233049" target="_blank">
			<img src="//pic.qiushibaike.com/system/pictures/12123/121233049/medium/MWP8786DCYZW62DK.jpg" alt="你若挣开束缚">
		</a>
	</div>
'''
# 该列表中存储的就是当前页面源码中所有的图片链接
img_list = re.findall('<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>',page_text,re.S)

# 创建储存图片的文件夹
if not os.path.exists('./data_storage/'):
	os.mkdir('./data_storage')

for url in img_list:
	# 将图片url进行拼接，拼接成一个完整的url
	image_url = 'https:' + url

	#持久化存储：存储图片的数据，并不是url
	# 获取图片二进制数据值
	img_content = requests.get(url=image_url,headers=headers).content
	img_name = url.split('/')[-1]
	with open('./data_storage/%s'%img_name,'wb') as fp:
		fp.write(img_content)
		print("%s 写入成功"%img_name)

