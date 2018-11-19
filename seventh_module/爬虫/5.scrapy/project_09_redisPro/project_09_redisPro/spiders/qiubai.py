# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
class QiubaiSpider(RedisCrawlSpider):

	name = 'qiubai'
	# 调度器队列的名称
	redis_key = 'qiubaispider' # 该行代码跟start_urls 含义是一样的
	rules = (
		Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		pass