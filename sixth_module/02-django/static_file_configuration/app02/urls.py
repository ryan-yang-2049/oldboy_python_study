# -*- coding: utf-8 -*-

# __title__ = 'urls.py.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.06.21'



from django.urls import path,re_path
from app02 import  views            #导入对应应用的视图


urlpatterns = [
	re_path("index/",views.index,name="index")
]









