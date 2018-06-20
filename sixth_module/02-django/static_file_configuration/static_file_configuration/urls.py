"""static_file_configuration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path,re_path
# # path django===2.0.*
# # re_path django===1.0.*
# from app01 import  views            #导入对应应用的视图
# urlpatterns = [
#     path('admin/', admin.site.urls),
# 	path('timer/',views.timer),     #添加路由转发
# 	# 路由配置： 路径----> 视图函数
# 	re_path(r'^articles/2003/$', views.special_case_2003),  #special_case_2003(request) request是请求对象
# 	# 只要url里面有个正则分组，它就会作为一个位置参数，就要多传一个参数到对应的视图函数里面
# 	re_path(r'^articles/([0-9]{4})/$', views.year_archive),
# 	re_path(r'^articles/([0-9]{4})/([1-9]{1}|1[0-2]{1})/$', views.month_archive),
# 	# re_path(r'^articles/([0-9]{4})/([1-9]{1}|1[0-2]{1})/([0-9]+)/$', views.article_detail),
# ]
# -------------------------------------分组-------------------------------
# from django.contrib import admin
# from django.urls import path,re_path
#
# from app01 import  views
# urlpatterns = [
#     path('admin/', admin.site.urls),
# 	path('timer/',views.timer),     #添加路由转发
#
# 	re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[1-9]{1}|1[0-2]{1})/(?P<day>[1-9]{1}|1[0-9]{1}|2[0-9]{1}|3[0-1]{1})/$', views.article_detail),
# ]


from django.contrib import admin
from django.urls import path,re_path,include
from app01 import  views            #导入对应应用的视图


urlpatterns = [
    path('admin/', admin.site.urls),
	path('timer/',views.timer),     #添加路由转发
	path('login/',views.login,name="Login"),
	path('app01/',include('app01.urls'))
]












