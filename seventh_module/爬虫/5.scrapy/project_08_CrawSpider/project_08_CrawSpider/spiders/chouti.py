# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor # LinkExtractor 连接提取器
from scrapy.spiders import CrawlSpider, Rule    # Rule 规则解析器


class ChoutiSpider(CrawlSpider):
	name = 'chouti'
	# allowed_domains = ['dig.chouti.com']
	start_urls = ['https://dig.chouti.com/']

	# 实例化了一个链接提取器对象
	# 链接提取器：用来提取指定的链接(url)
	# allow 参数：赋值一个正则表达式
	# allow的作用：链接提取器就可以根据正则表达式在页面中提取指定的链接内容
	# 提取到的链接会全部交给规则解析器
	link = LinkExtractor(allow=r'/all/hot/recent/\d+')

	rules = (
		# 实例化了一个规则解析器对象
		# 规则解析器接收了链接提取器发送的链接后，就会对这些连接发起请求，获取链接对应的页面内容，就会根据指定的规则对页面内容中指定的数据值进行解析
		# callback：指定一个解析规则(方法/函数)
		# follow参数：是否将链接提取继续作用到链接提取器提取出的链接所表示的页面当中
		Rule(link, callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		print(response)