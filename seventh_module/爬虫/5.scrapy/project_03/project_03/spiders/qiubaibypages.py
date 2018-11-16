# -*- coding: utf-8 -*-
import scrapy
from project_03.items import Project03Item
class QiubaibypagesSpider(scrapy.Spider):
	name = 'qiubaibypages'
	# allowed_domains = ['www.qiushibaike.com/text']
	start_urls = ['https://www.qiushibaike.com/text/']
	# 设计一个通用的url模板
	url = 'https://www.qiushibaike.com/text/page/%d/'
	pageNum = 1
	def parse(self, response):
		div_list = response.xpath('//*[@id="content-left"]/div')
		data_list = []
		for div in div_list:
			author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
			content_list = div.xpath('.//div[@class="content"]/span/text()').extract()
			content = "\n".join(content_list)   # 因为此处要是获取到列表是多个值，那么只会获取第一个列表里面的值
			item = Project03Item()
			item['author'] = author
			item['content'] = content
			yield  item
		# 请求的手动发送
		if self.pageNum < 13:
			self.pageNum += 1
			new_url = format(self.url % self.pageNum)
			# 回调函数 callback ：将请求获取到的页面数据进行解析
			yield scrapy.Request(url=new_url,callback=self.parse)