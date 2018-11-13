# -*- coding: utf-8 -*-

# __title__ = '1.常用xpath.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.09'

'''
属性定位：
	#找到class属性值为song的div标签
	//div[@class="song"]

层级&索引定位
	# 找到class属性值为tang的div的直系子标签ul下的第二个子标签li下的直系子标签a
	//div[@class="tang"]/ul/li[2]/a

模糊匹配
	//div[contains(@class,"ng")]
	//div[starts-with(@class,"ta")]

取文本
	# /表示获取某个标签下的文本内容
	# // 表示获取某个标签下的文本内容和所有子标签的文本内容
	//div[@class="song"]/p[1]/text()
	//div[@class="tang"]//text()

取属性
	//div[@cclass="tang"]//li[2]/a/@href
'''










