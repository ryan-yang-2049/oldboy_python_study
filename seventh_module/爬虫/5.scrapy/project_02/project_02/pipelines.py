# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道
# class Project02Pipeline(object):
# 	fp = None
# 	# 整个爬虫过程中，该方法只会在开始爬虫的时候被调用一次
# 	def open_spider(self,spider):
# 		print('开始爬虫')
# 		self.fp = open('./qiubai_pipe.txt', 'w', encoding='utf-8')
#
#
# 	# 该方法就可以接收爬虫文件中提交过来的item对象，并且对item对象中存储的页面数据进行持久化存储
# 	# 参数：  items 表示的就时接收到的item对象
# 	# 每当爬虫文件向管道提交一次item，则该方法就会被执行一次
# 	def process_item(self, item, spider):
# 		# 取出item对象中存储的数据值
# 		author = item['author']
# 		content = item['content']
#
# 		# 持久化存储操作
#
# 		self.fp.write(author+":"+content+'\n\n\n')
# 		return item
#
# 	# 该方法只有在爬虫结束的时候被调用一次
# 	def close_spider(self,spider):
# 		print('爬虫结束')
# 		self.fp.close()

# mysql数据库
# import pymysql
# class Project02Pipeline(object):
# 	conn = None
# 	cursor = None
# 	def open_spider(self,spider):
# 		print('开始爬虫')
# 		# 连接数据库
# 		self.conn = pymysql.connect(host='101.132.161.180', port=3306, user='root', passwd='123456', db='qiubai',charset="utf8")
#
# 	# 编写向数据库中存储数据的相关代码
# 	def process_item(self, item, spider):
# 		# 1.连接数据库
# 		# 2.执行sql语句
# 		sql = 'insert into qiubai values("%s","%s")'%(item['author'],item['content'])
# 		self.cursor = self.conn.cursor()
# 		try:
# 			self.cursor.execute(sql)
# 			self.conn.commit()
# 		except Exception as e:
# 			print(e)
# 			self.conn.rollback()
# 		# 3.提交事务
#
# 	def close_spider(self,spider):
# 		print("爬虫结束")
# 		self.cursor.close()
# 		self.conn.close()

# redis数据库
import redis
class Project02Pipeline(object):
	conn = None
	def open_spider(self,spider):
		print('开始爬虫--redis')
		# self.conn = redis.Redis(host='101.132.45.51',port=6379,encoding='utf-8')
		# print(self.conn)
		# # self.conn.lpush("num",11,22,33,44 )
	def process_item(self, item, spider):
		# dic = {
		# 	'author':item['author'],
		# 	'content':item['content']
		# }
		# self.conn.lpush("data_qiubai_string",str(dic))
		print('数据已经写入到redis中')
		print('前面案例已经实现,copy即可')
		return item


# 将数据值存储到本地磁盘中
class QiubaiByFiles(object):
	def open_spider(self,spider):
		print('开始爬虫--磁盘文件')
	def process_item(self,item,spider):
		print('数据已经写入指定的操盘')
		print('前面案例已经实现,copy即可')
		return item


# 将数据值存储到MySQL数据库中
class QiubaiByMysql(object):
	def open_spider(self,spider):
		print('开始爬虫--mysql')
	def process_item(self, item, spider):
		print('数据已经写入到mysql数据库')
		print('前面案例已经实现,copy即可')
		return item