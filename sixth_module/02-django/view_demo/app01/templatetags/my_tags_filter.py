# -*- coding: utf-8 -*-

# __title__ = 'my_tags_filter.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.06.22'


from django import  template

# register 名称不可修改
register=template.Library()

# 自定义过滤器只能有两个参数
@register.filter
def multi_filter(x,y):

	return x*y


# 自定义标签可以有多个参数
@register.simple_tag
def multi_tag(x,y):

	return x*y

