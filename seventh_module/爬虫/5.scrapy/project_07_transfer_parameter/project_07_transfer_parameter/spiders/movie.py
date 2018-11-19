# -*- coding: utf-8 -*-
import scrapy
from project_07_transfer_parameter.items import Project07TransferParameterItem

class MovieSpider(scrapy.Spider):
	name = 'movie'
	# allowed_domains = ['www.id97.com']
	start_urls = ['http://www.55xia.com/movie']
	# 用于解析二级子页面的数据值
	def parse_by_seconde_page(self,response):
		movie_director = response.xpath("//table/tbody/tr[1]/td[2]/a/text()").extract_first()
		movie_language = response.xpath("//table/tbody/tr[6]/td[2]/text()").extract_first()
		movie_length = response.xpath("//table/tbody/tr[8]/td[2]/text()").extract_first()
		# 取出Request 方法的meta参数传递过来的字典
		item = response.meta['item']
		item['movie_director'] = movie_director
		item['movie_language'] = movie_language
		item['movie_length'] = movie_length
		yield item

	def parse(self, response):
		# 名称，类型，导演，语言，片长
		div_list = response.xpath("/html/body/div[1]/div[1]/div[2]/div")
		for div in div_list:
			movie_title = div.xpath('.//div[@class="meta"]/h1/a/@title').extract_first()
			movie_url = div.xpath('.//div[@class="meta"]/h1/a/@href').extract_first()
			movie_url = "http:"+str(movie_url)
			movie_type = div.xpath('.//div[@class="meta"]/div[@class="otherinfo"]//text()').extract()
			movie_type = " ".join(movie_type)
			print(movie_type)
			# 创建items对象
			item = Project07TransferParameterItem()
			item['movie_title'] = movie_title
			item['movie_type'] = movie_type
			# 问题：如果将剩下的电影详情数据存储到item对象(meta)
			# 需要对movie_url 发起请求，获取页面数据，进行指定数据解析
			# meta 参数只可以赋值一个字典(将item对象先封装到字典中)，meta会作为参数传递到回调函数中
			yield scrapy.Request(url=movie_url,callback=self.parse_by_seconde_page,meta={'item':item})







