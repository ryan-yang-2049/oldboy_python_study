# -*- coding: utf-8 -*-

# __title__ = 'mzitu.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.11'


import requests
from lxml import etree
import os


def download_img(img_url_referer_url):
	# print("fuck, 你还来不来")
	(img_url, referer) = img_url_referer_url
	print('Downloading ......' + img_url)
	headers = {
		# 'Cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c = 1534726766;Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c = 1534727069',
		'referer': referer,
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	}
	# print(headers)
	if os.path.exists('download'):
		pass
	else:
		os.mkdir('download')
	filename = 'download/' + img_url.split('/')[-1]
	# request.urlretrieve(img_url, filename)
	response = requests.get(img_url, headers=headers)
	with open(filename, 'wb') as f:
		f.write(response.content)


def parse_detailed_page(url_href, queue):
	# for i in range(1, )
	response = requests.get(url_href)
	html_ele = etree.HTML(response.text)
	max_page = html_ele.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]
	# print(max_page)
	for i in range(1, int(max_page) + 1):
		page_url = url_href + '/' + str(i)
		response = requests.get(page_url)
		html_ele = etree.HTML(response.text)
		img_url = html_ele.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
		# print(img_url)
		# download_img(img_url, url_href)
		queue.put((img_url, url_href))


def get_all_image_url(queue):
	url = 'http://www.mzitu.com/'
	response = requests.get(url)

	# with open('mzitu.html', 'wb') as f:
	#     f.write(response.content)

	html_ele = etree.HTML(response.text)
	href_list = html_ele.xpath('//ul[@id="pins"]/li/a/@href')
	for href in href_list:
		# print(href)
		parse_detailed_page(href, queue)


if __name__ == '__main__':
	# 创建一线程或者进程
	import multiprocessing
	from multiprocessing import Queue, Pool

	# 以下三行主要是获取image的url, 放到我们的queue中
	q = Queue()
	p = multiprocessing.Process(target=get_all_image_url, args=(q,))
	p.start()

	download_pool = Pool(5)
	for i in range(0, 2000):
		image_url_referer_url = q.get()
		print(image_url_referer_url)
		download_pool.apply_async(download_img, (image_url_referer_url,))

	download_pool.close()
	download_pool.join()
	# 程序最后退出前进行join
	p.join()









