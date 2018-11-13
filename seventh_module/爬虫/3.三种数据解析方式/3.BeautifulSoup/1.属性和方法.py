# -*- coding: utf-8 -*-

# __title__ = 'ceshi.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.09'


from bs4 import BeautifulSoup
soup = BeautifulSoup(open('text.html','rb'),'lxml')
# 找到第一个符合要求的 head,div标签
res1 = soup.head
res2 = soup.div
# 获取标签属性 第一个
res3 = soup.a.attrs
res4 = soup.a.attrs['href'] # 获取指定属性值
res5 = soup.a['href']   # 获取指定属性值

# 获取内容
res6 = soup.p.string
res7 = soup.p.text
res8 = soup.p.get_text()

# find：找到第一个符合要求的标签
find1 = soup.find('div',class_='song')

# find_All：找到所有符合要求的标签,限制前两个
findall_1 = soup.find_all('a',limit=2)

# 根据选择器选择指定的内容
# select函数的层级选择器
select1 = soup.select('div > img') # 只能是子标签
select2 = soup.select('div li') # div下的所有li标签
select3 = soup.select('div > ul li') # div子标签下的所有li标签
select4 = soup.select('.tang > ul .aaaa > li #feng')
print(select4)






















