# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2017.12.27'
"""

'''
用于添加的blog的目录地址
<ol>
<li><a style="text-decoration:none;color: #000000; line-height: 20px; font-family: 楷体; font-size: 20px;" href="http://www.cnblogs.com/keep-going2099/articles/8134851.html" target="_blank">python 编码格式 </a></li>
<li><a  style="text-decoration:none;color: #000000; line-height: 20px; font-family: 楷体; font-size: 20px;" href="https://foofish.net" target="_blank">python之禅</a></li>
</ol>
'''

import io,sys,os
def add_blog_url(url,info):
    add_content = '<li><a  style="text-decoration:none;color: #000000; line-height: 20px; font-family: 楷体; font-size: 20px;" href="%s" target="_blank">%s</a></li>'%(url,info)
    li_content = []
    with io.open("blog_url.html", 'r', encoding='utf-8') as  read_file, io.open("new_blog_url.html", 'w',encoding='utf-8') as write_file:
        content = read_file.read()
        post = content.find('</ol>')
        if post != -1:
            content = content[:post] + add_content+'\n' + content[post:]
        '''
        这里就相当于字符串的切片操作，find的意思是，如果找不到就返回-1，找到返回查找的字符串的位置。
        content = content[:post] + add_content + content[post:]
        content[:post] ：读取的是查找内容之前内容
        add_content ： 表示要添加的内容
        content[post:] ：表示查找内容之后的
        '''
        write_file.write(content)
        # os.rename('blog_url.html','bak_blog_url.html')
    os.remove('blog_url.html')
    os.rename('new_blog_url.html','blog_url.html')


if __name__ == '__main__':
    while True:
        url = input("输入网址,退出（Q）：").strip()
        if url == 'Q':break
        if len(url) == 0:continue
        if  url.startswith("http://") or url.startswith("https://"):
            info = input("输入网站信息：").strip()
            add_blog_url(url,info)
        else:
            print("必须是http:// 或者https:// 开头才能访问,")
            continue





















