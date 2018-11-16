# -*- coding: utf-8 -*-
import scrapy
# 需求：百度翻译中指定词条对应的翻译结果进行获取
class PostdemoSpider(scrapy.Spider):
	name = 'postDemo'
	# allowed_domains = ['www.baidu.com']
	start_urls = ['https://fanyi.baidu.com/sug']
	# 2.第二种发起post的方法:FormRequest()可以发起post请求(推荐)
	def start_requests(self):
		print('start_requests')
		# post 的请求参数
		data = {
			'kw':'dog',
		}
		for url in self.start_urls:
			# formdata : 请求参数对应的字典
			yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse,encoding='gbk')
	def parse(self, response):
		print(response.text)
