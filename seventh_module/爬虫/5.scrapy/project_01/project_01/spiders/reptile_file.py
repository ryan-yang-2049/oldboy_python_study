# -*- coding: utf-8 -*-
import scrapy

class ReptileFileSpider(scrapy.Spider):
	# 爬虫文件的名称: 可以通过爬虫文件的名称可以指定的定位到某一个具体的爬虫文件
	name = 'reptile_file'
	# 允许的域名: 只可以爬取指定域名下的页面数据 例如：www.qiushibaike.com/1.html www.qiushibaike.com/2.html等，可以写多个域名
	allowed_domains = ['www.qiushibaike.com']
	# 起始url：当前工程将要爬取得页面所对应的url。此url必须和allowed_domains 里面存在
	# start_urls = ['http://www.qiushibaike.com/','http://www.qiushibaike.com/1.html'] 这个是允许的
	start_urls = ['http://www.qiushibaike.com/']

	# 解析方法：对获取页面的数据进行指定内容的解析
	# response ：根据起始url列表发起请求，请求成功后返回的响应对象
	# parse 方法的返回值：必须为迭代器对象或者空对象
	def parse(self, response):
		print(response.text)   # 获取响应对象中的页面数据。
		print('执行结束')