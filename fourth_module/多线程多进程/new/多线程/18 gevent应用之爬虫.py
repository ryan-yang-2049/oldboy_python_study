# -*- coding: utf-8 -*-
"""
__title__ = '18 gevent应用之爬虫.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.05'
"""

from gevent import monkey;monkey.patch_all()
import gevent
import requests
import time

def get_page(url):
    print('GET: %s' %url)
    response=requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' %(len(response.text),url))


start_time=time.time()

# 串行 4s多
# get_page('https://www.python.org/')
# get_page('https://www.yahoo.com/')
# get_page('https://github.com/')

# 并行（异步） run time is 3s 多
g1=gevent.spawn(get_page, 'https://www.python.org/')
g2=gevent.spawn(get_page, 'https://www.yahoo.com/')
g3=gevent.spawn(get_page, 'https://github.com/')
#
gevent.joinall([g1,g2,g3])
stop_time=time.time()
print('run time is %s' %(stop_time-start_time))

