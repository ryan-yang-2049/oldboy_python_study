from django.contrib import admin

# Register your models here.
from app01 import models

admin.site.register(models.UserInfo)  # 创建了4个URL

'''
创建的4个url:
	http://127.0.0.1:8000/admin/app01/userinfo/
	http://127.0.0.1:8000/admin/app01/userinfo/add/
	http://127.0.0.1:8000/admin/app01/userinfo/1/change/
	http://127.0.0.1:8000/admin/app01/userinfo/1/delete/
'''