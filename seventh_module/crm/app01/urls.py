
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
]
