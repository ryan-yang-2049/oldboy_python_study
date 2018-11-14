# -*- coding: utf-8 -*-

# __title__ = '3.实战3.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.14'

from selenium import webdriver
import time
# 创建浏览器对象  executable_path :驱动程序路径
bro = webdriver.PhantomJS(executable_path='./driver/phantomjs-2.1.1-windows/bin/phantomjs.exe')
url = 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action='
bro.get(url=url)
time.sleep(1)
bro.save_screenshot('./3-1.png')
# 编写JS代码：让页面中的滚轮向下滑动(底部或者指定px)

js = 'window.scrollTo(0,document.body.scrollHeight)'

# 如何让浏览器执行js代码
bro.execute_script(js)
time.sleep(5)
bro.save_screenshot('./3-3.png')
# 获取加载数据后的页面。page_source：获取浏览器档期按的页面数据
page_text = bro.page_source


print(page_text)
