from django.urls import re_path
from app02 import views

urlpatterns = [

	re_path(r'index/',views.index,name="index"),
]







