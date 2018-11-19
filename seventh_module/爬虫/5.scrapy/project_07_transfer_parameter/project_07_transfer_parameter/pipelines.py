# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Project07TransferParameterPipeline(object):

	fp = None
	def open_spider(self,spider):
		print('开始爬虫')
		self.fp = open('movie.txt','w',encoding='utf-8')

	def process_item(self, item, spider):
		detail = item['movie_title']+':'+item['movie_type']+':'+item['movie_director']+':'+item['movie_language']+':'+item['movie_length']+'\n\n\n\n'
		self.fp.write(detail)
		return item


	def close_spider(self,spider):
		print('结束爬虫')
		self.fp.close()