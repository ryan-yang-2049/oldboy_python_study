# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from project_09_redisPro.items import Project09RedisproItem

class QiubaiSpider(RedisCrawlSpider):
	name = 'qiubai'
	# 调度器队列的名称
	redis_key = 'qiubaispider' # 该行代码跟start_urls 含义是一样的
	link = LinkExtractor(allow=r'/pic/page/\d+')
	rules = (
		Rule(link, callback='parse_item', follow=True),
	)
	def parse_item(self, response):
		div_list = response.xpath('//div[@id="content-left"]/div')
		for div in div_list:
			img_url = "https:"+div.xpath('.//div[@class="thumb"]/a/img/@src').extract_first()
			item = Project09RedisproItem()
			item['img_url'] = img_url

			yield item



