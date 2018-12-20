# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.14'
from django.shortcuts import HttpResponse
from django.conf.urls import url
from django.utils.safestring import mark_safe


from stark.service.v1 import site, StarkHandler,get_choice_text
from app01 import models


class DepartHandler(StarkHandler):
	list_display = ['id', 'title', StarkHandler.display_edit,StarkHandler.display_del]


# site.registry(models.Depart, DepartHandler, prev='public01')
site.registry(models.Depart, DepartHandler)


class UserInfoHandler(StarkHandler):
	per_page_num = 1
	# 定制页面的列
	list_display = ['name',
	                get_choice_text('性别', 'gender'),
	                get_choice_text('班级', 'classes'),
	                # 'gender','classes',
	                'age', 'email', 'depart',
	                StarkHandler.display_edit,
	                StarkHandler.display_del]



site.registry(models.UserInfo, UserInfoHandler)
