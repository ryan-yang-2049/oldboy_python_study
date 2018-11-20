# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JiandanSpider(CrawlSpider):
	name = 'jiandan'
	# allowed_domains = ['jandan.net/ooxx']
	start_urls = ['http://jandan.net/ooxx/']
	link = LinkExtractor(allow=r'//jandan.net/ooxx/page-\d+#comments')
	rules = (
		Rule(link, callback='parse_item', follow=False),
	)

	def parse_item(self, response):
		li_list = response.xpath('//ol[@class="commentlist"]/li')
		for li in li_list:
			img_url = li.xpath('.//div/div/div[@class="text"]/p/img/@src').extract_first()
			print(img_url)
