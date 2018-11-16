# -*- coding: utf-8 -*-
import scrapy
class DoubanSpider(scrapy.Spider):
	name = 'douban'
	# allowed_domains = ['www.douban.com']
	start_urls = ['https://accounts.douban.com/login']

	# 重写 start_requests方法
	def start_requests(self):
		#将请求参数封装到字典中
		data = {
			'source': 'movie',
			'redir': 'https://movie.douban.com/',
			'form_email': '461580544@qq.com',
			'form_password': 'Ryan!@99',
			'login': '登录'
		}
		for url in self.start_urls:
			yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse)

	# 针对个人主页页面数据进行解析操作
	def parseBySecondPage(self,response):
		fp = open('second.html','w',encoding='utf-8')
		fp.write(response.text)
		print('写入成功')
		fp.close()

	def parse(self, response):
		# 登陆成功后的页面数据进行存储
		fp = open('main.html','w',encoding='utf-8')
		fp.write(response.text)
		fp.close()

		# 获取当前用户的个人主页的页面数据
		url = 'https://www.douban.com/people/84385895/'
		yield scrapy.Request(url=url,callback=self.parseBySecondPage)











