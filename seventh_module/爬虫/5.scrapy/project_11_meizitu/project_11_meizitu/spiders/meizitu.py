# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MeizituSpider(CrawlSpider):
	name = 'meizitu'
	# allowed_domains = ['www.mzitu.com']
	start_urls = ['https://www.mzitu.com/']
	link = LinkExtractor(allow=r'https://www.mzitu.com/page/\d+/')
	rules = (
		Rule(link, callback='parse_item', follow=False),
	)

	def parse_item(self, response):
		link_url = response.xpath('//*[@id="pins"]/li')
		# print("link_url==================>",link_url)
		for link in link_url:
			link_son_url = link.xpath('./a/@href').extract_first()
			print("link_son_url==================>",link_son_url)


		# li_list = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
		# print("===========>",li_list)
		# https://i.meizitu.net/2018/11/13a05.jpg
