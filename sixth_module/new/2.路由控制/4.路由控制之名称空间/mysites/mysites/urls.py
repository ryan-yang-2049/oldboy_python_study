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
from django.urls import path,re_path,include

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),

	# namespace
	# re_path(r'^app01/',include(('app01.urls',"index01"),namespace="app01")),
	# re_path(r'^app02/',include(('app02.urls',"index02"),namespace="app02")),
	# re_path(r'^app01/', include(('app01.urls', "app01"))),
	# re_path(r'^app02/', include(('app02.urls', "app02"))),
	re_path(r'^app01/', include(('app01.urls', "index01"))),
	re_path(r'^app02/', include(('app02.urls', "index02"))),


]
