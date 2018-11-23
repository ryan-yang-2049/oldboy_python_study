# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MeizituSpider(CrawlSpider):
	name = 'meizitu'
	# allowed_domains = ['www.mzitu.com']
	start_urls = ['https://www.mzitu.com/158446']
	link = LinkExtractor(allow=r'www.mzitu.com/158446/\d+')
	rules = (
		Rule(link, callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		li_list = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
		print(li_list)
		# https://i.meizitu.net/2018/11/13a05.jpg
