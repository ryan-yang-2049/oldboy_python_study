# -*- coding: utf-8 -*-

# __title__ = 'urls.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.12'

from django.conf.urls import url,include
from cmdb.views import account,user,host

urlpatterns = [
	# url(r'^login/$', account.login, name='login'),
	# url(r'^logout/$', account.logout, name='logout'),
	url(r'^index/$', account.index, name='index'),

	url(r'^user/list/$', user.user_list, name='user_list'),
	url(r'^user/add/$', user.user_add, name='user_add'),
	url(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),
	url(r'^user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),
	url(r'^user/reset/password/(?P<pk>\d+)/$', user.user_reset_pwd, name='user_reset_pwd'),
	#
	url(r'^host/list/$', host.host_list, name='host_list'),
	url(r'^host/add/$', host.host_add, name='host_add'),
	url(r'^host/edit/(?P<pk>\d+)/$', host.host_edit, name='host_edit'),
	url(r'^host/del/(?P<pk>\d+)/$', host.host_del, name='host_del'),


]






