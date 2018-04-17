# -*- coding: utf-8 -*-
"""
__title__ = '14 回调函数.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.05'
"""
from concurrent.futures import ThreadPoolExecutor
import requests
import os
import time
from threading import currentThread
def get_page(url):
    print('%s:<%s> is getting [%s]' %(currentThread().getName(),os.getpid(),url))
    response=requests.get(url)
    time.sleep(2)
    return {'url':url,'text':response.text}
def parse_page(res):
    res=res.result()
    print('%s:<%s> parse [%s]' %(currentThread().getName(),os.getpid(),res['url']))
    with open('db.txt','a') as f:
        parse_res='url:%s size:%s\n' %(res['url'],len(res['text']))
        f.write(parse_res)
if __name__ == '__main__':
    # p=ProcessPoolExecutor()
    p=ThreadPoolExecutor()
    urls = [
        'https://www.baidu.com',
        'http://www.openstack.org',
        'https://www.python.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]

    for url in urls:
        # multiprocessing.pool_obj.apply_async(get_page,args=(url,),callback=parse_page)
        p.submit(get_page, url).add_done_callback(parse_page)  # 此时回调函数拿到的值是一个对象，因此 要在回调函数里面去result,获取。
    p.shutdown()
    print('主',os.getpid())











