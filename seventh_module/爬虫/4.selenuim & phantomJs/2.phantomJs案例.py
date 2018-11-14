# -*- coding: utf-8 -*-

# __title__ = '2.phantomJs案例.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.14'


from selenium import  webdriver
# 创建浏览器  executable_path :驱动程序路径
bro = webdriver.PhantomJS(executable_path='./driver/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# 打开浏览器
bro.get('https://www.baidu.com')

# 截屏
bro.save_screenshot('./1.png')
# 让百度进行指定词条的一个搜索
text = bro.find_element_by_id('kw') # 定位到输入词条的inupt文本框
# 输入关键字到 input框
text.send_keys('python django')
bro.save_screenshot('./2.png')

bro.quit()







