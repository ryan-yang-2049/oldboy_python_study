from django.urls import re_path
from app01 import views

urlpatterns = [
	# 路由配置：  路径-----> 视图函数
	re_path(r'^articles/2003/$', views.special_case_2003),
	re_path(r'^articles/([0-9]{4})/$', views.year_archive),
	re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
	# 有名分组(?P<名称>正则)
	re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{1,2})/$', views.article_detail),
]







