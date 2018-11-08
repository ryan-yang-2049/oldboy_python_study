# -*- coding: utf-8 -*-

# __title__ = '1.练习.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.08'

import re

#提取 python
key = 'javapythonc++php'
res = re.findall('python',key)

# 提取 hello world  ():分组 ,[]:第几个元素
key = '<html><h1>hello world</h1></html>'
res1 = re.findall('<h1>(hello world)</h1>',key)[0]


# 提取170
string = '我喜欢身高为170的女孩'
print(re.findall('\d+',string)[0])


# 提取http://  和 https://
key = 'http://www.baidu.com and https://python.com'
print(re.findall('https?',key))
print(re.findall('https{0,1}',key))

# 提取  'hit.'
key = 'bobo@hit.edu.com'
print(re.findall('h.*\.',key))  # 贪婪模式:根据正则表达式尽可能多的提取出数据
print(re.findall('h.*?\.',key))  # 非贪婪模式： ?

# 匹配sas 和saas
key = 'saas and sas and saaas'
print(re.findall('sa{1,2}s',key))

# 匹配出 i 开头的行
# re.S : 基于单行匹配
# re.M : 基于多行匹配
string = '''
fail in love with you
i love you very much
i love she
'''
print(re.findall('^i.*',string,re.M))

# 匹配全部行
string = '''<div>静夜思
床前明月光
疑是地上霜
举头望明月
低头思故乡
</div>'''
print(re.findall('<div>(.*)</div>',string,re.S))
















