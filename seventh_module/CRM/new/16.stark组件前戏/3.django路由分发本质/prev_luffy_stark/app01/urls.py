# -*- coding: utf-8 -*-

from django.conf.urls import url,include
from app01 import views



urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^home/', views.home),
]











