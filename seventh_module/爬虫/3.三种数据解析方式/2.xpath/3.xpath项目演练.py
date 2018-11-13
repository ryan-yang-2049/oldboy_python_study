# -*- coding: utf-8 -*-

# __title__ = '3.xpath.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.09'


# 需求：使用xpath 对段子王中的段子内容和标题进行解析,以及持久化存储

import requests
from lxml import etree
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}

# 指定url
url = 'https://ishuo.cn/joke'
# 发起请求
response = requests.get(url=url,headers=headers)

# 获取页面内容
page_text = response.text

# 数据解析
tree = etree.HTML(page_text)
# 获取所有的li标签（段子内容和标题都被包含在li标签中）
content_list = tree.xpath('//div[@id="list"]/ul/li') #res : [<Element li at 0x181cd3eeac8>, ....]

#注意：Element类型的对象可以继续调用xpath函数，对该对象表示的局部内容进行指定的解析
for li in content_list:
	content = li.xpath('./div[@class="content"]/text()')[0]
	title = li.xpath('./div[@class="info"]/a/text()')[0]
	print(title,"====>",content)
#持久化存储
	with open('./duanzi.txt','a+',encoding='utf-8') as fp:
		fp.write("%s==>: %s"%(title,content)+"\n\n")






