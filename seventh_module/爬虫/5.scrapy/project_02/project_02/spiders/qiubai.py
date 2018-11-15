# -*- coding: utf-8 -*-
import scrapy
from project_02.items import Project02Item
class QiubaiSpider(scrapy.Spider):
	name = 'qiubai'
	# allowed_domains = ['www.qiushibaike.com/text']
	start_urls = ['https://www.qiushibaike.com/text/']

	def parse(self, response):
		# 建议使用xpath进行指定内容的解析(框架继承了xpath解析的接口)
		# 解析段子的内容和作者
		div_list = response.xpath('//div[@id="content-left"]/div')
		# 存储解析到的页面数据
		data_list = []
		for div in div_list:

			#xpath 解析到的指定内容被存储到了 Selector对象中
			# extract() 该方法可以将Selector对象中存储的数据值拿到
			# author = div.xpath('./div/a[2]/h2/text()').extract()[0]
			# extract_first()  == extract()[0]
			author = div.xpath('./div/a[2]/h2/text()').extract_first()
			content = div.xpath('.//div[@class="content"]/span/text()').extract_first()

			# 1.将解析到的数据值(author 和content) 存储到items对象中
			item = Project02Item()
			item['author'] = author
			item['content'] = content
			# 2.使用yield关键字将items提交给管道文件进行处理
			yield  item
















