# -*- coding: utf-8 -*-

# __title__ = '1.ex01.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.14'

# 编码流程
from selenium import webdriver
import time
# 创建一个浏览器对象  executable_path:浏览器的驱动
bro = webdriver.Chrome(executable_path='./driver/chromedriver.exe')

# get方法可以指定一个url，让浏览器进行请求

# url = 'http://pic.hao123.com/album/qingdannvzi'
url = 'https://www.baidu.com'
bro.get(url=url)

time.sleep(1)

'''
#使用下面的方法，查找指定的元素进行操作即可
    find_element_by_id            根据id找节点
    find_elements_by_name         根据name找
    find_elements_by_xpath        根据xpath查找
    find_elements_by_tag_name     根据标签名找
    find_elements_by_class_name   根据class名字查找
'''
# 让百度进行指定词条的一个搜索
text = bro.find_element_by_id('kw') # 定位到输入词条的inupt文本框
# 输入关键字到 input框
text.send_keys('python selenium')
time.sleep(1)
# 定位到"百度一下"的搜索按钮，并点击
button = bro.find_element_by_id('su')
button.click() # click表示点击操作
time.sleep(3)

# 关闭浏览器
bro.quit()





