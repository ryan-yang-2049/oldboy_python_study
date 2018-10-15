"""mysites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timer/', views.timer),

	# 路由配置：  路径-----> 视图函数
	re_path(r'^articles/2003/$', views.special_case_2003),
	re_path(r'^articles/([0-9]{4})/$', views.year_archive),
	re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
	# 有名分组(?P<名称>正则)
	re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{1,2})/$', views.article_detail),
]
