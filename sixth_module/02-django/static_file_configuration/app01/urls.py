# -*- coding: utf-8 -*-

# __title__ = 'urls.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.06.20'



from django.contrib import admin
from django.urls import path,re_path
from app01 import  views            #导入对应应用的视图


urlpatterns = [
	re_path(r'^articles/2003/$', views.special_case_2003,name='s_c_2003'),
	re_path(r'^articles/([0-9]{4})/$',views.year_archive,name='y_a'),
	re_path(r'^articles/([0-9]{4})/([1-9]{1}|1[0-2]{1})/$', views.month_archive),
	re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[1-9]{1}|1[0-2]{1})/(?P<day>[1-9]{1}|1[0-9]{1}|2[0-9]{1}|3[0-1]{1})/$', views.article_detail),
]









