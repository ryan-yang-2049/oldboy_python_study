"""prev_luffy_stark URL Configuration

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
#
# urlpatterns = [
#     url(r'^web/', include('app01.urls')),
# ]
from django.conf.urls import url,include
from app01 import views

urlpatterns = [
	url(r'^web/', ([
		           url(r'^index/', views.index),
		           url(r'^home/', views.home),
		           ], None, None)),
]
"""
web/index/   -->app01.views.index
web/home/   -->app01.views.home

from app01 import urls
urlpatterns = [
    url(r'^web/', (urls, app_name, namespace)),
]


"""







