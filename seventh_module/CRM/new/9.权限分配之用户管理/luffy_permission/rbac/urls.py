# -*- coding: utf-8 -*-

# __title__ = 'urls.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.11.29'


from django.conf.urls import url,include
from django.contrib import admin
from rbac.views import role,user

urlpatterns = [
    url(r'^role/list/', role.role_list,name='role_list'),
    url(r'^role/add/', role.role_add,name='role_add'),
    url(r'^role/edit/(?P<pk>\d+)/$', role.role_edit,name='role_edit'),  # rbac:role_eid
    url(r'^role/del/(?P<pk>\d+)/$', role.role_del,name='role_del'),  # rbac:role_eid

	url(r'^user/list/', user.user_list, name='user_list'),
	url(r'^user/add/', user.user_add, name='user_add'),
	url(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),  # rbac:role_eid
	url(r'^user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),  # rbac:role_eid

]






