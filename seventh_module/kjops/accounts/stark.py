# -*- coding: utf-8 -*-

from stark.service.v1 import  site

from accounts import models
from accounts.views.depart import DepartmentHandler
from accounts.views.userinfo import UserInfoHandler

# 部门管理
site.registry(models.Department,DepartmentHandler)

# 用户管理
site.registry(models.UserInfo,UserInfoHandler)













