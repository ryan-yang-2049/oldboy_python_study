# -*- coding: utf-8 -*-

# __title__ = 'urls.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.29'


from django.conf.urls import url,include
from django.contrib import admin
from rbac.views import role
urlpatterns = [
    url(r'^role/list/', role.role_list,name='role_list'),
    url(r'^role/add/', role.role_add,name='role_add'),

]






