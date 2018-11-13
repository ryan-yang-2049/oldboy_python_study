# -*- coding: utf-8 -*-

# __title__ = '2.xpath应用1.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.09'


from lxml import  etree
# xpath函数返回的总是一个列表

# 创建 etree 对象进行指定数据解析
tree = etree.parse('./text.html')

#属性定位：根据指定的属性定位到指定的节点标签
res1 = tree.xpath('//div[@class="song"]')

# 层级&索引定位
#    # 找到class属性值为tang的div的直系子标签ul下的第二个子标签li下的直系子标签a
res2 = tree.xpath('//div[@class="tang"]/ul/li[2]/a')

# 逻辑定位：
	# 找到href属性值为空且class属性值为du的a标签
res3 = tree.xpath('//a[@href="" and @class="du"]')

# 模糊匹配
# contains 包含
# starts-with 以什么开始
res4 = tree.xpath('//div[contains(@class,"ng")]')
res5 = tree.xpath('//div[starts-with(@class,"ta")]')


# 取文本
#    # /  表示获取某个标签下的文本内容
#    # // 表示获取某个标签下的文本内容和所有子标签的文本内容
res6 = tree.xpath('//div[@class="song"]/p[1]/text()')
res7 = tree.xpath('//div[@class="tang"]//text()')

# 取属性
res8 = tree.xpath('//div[@class="tang"]//li[2]/a/@href')





