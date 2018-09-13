"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from django.shortcuts import HttpResponse
#
#
# from app01 import models as  m1
# from app02 import models as  m2
#
# def index(request):
# 	print(m1.UserInfo,m1.UserInfo._meta.app_label,m1.UserInfo._meta.model_name)
# 	print(m2.Role,m2.Role._meta.app_label,m2.Role._meta.model_name)
# 	# 获取当前models类所在app名称、以及小写类名
# 	_registry = {
# 		m1.UserInfo :'1',
# 		m2.Role :'2',
# 	}
# 	for k,v in _registry.items():
# 		print(k._meta.app_label,k._meta.model_name)
#
#
# 	return HttpResponse('OK.....')

from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	# url(r'^rbac/',include('app01.urls',namespace='rbac')),
	url(r'rbac/',([
		url(r'login/',views.login),
		url(r'logout/',views.logout),
	],None,'rbac'))
]
