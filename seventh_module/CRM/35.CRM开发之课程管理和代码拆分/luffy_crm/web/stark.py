# -*- coding: utf-8 -*-
# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.24'


from stark.service.v1 import site
from web import models
from web.views import school, depart, userinfo, course

site.registry(models.School, school.SchoolHandler)

site.registry(models.Department, depart.DepartmentHandler)

site.registry(models.UserInfo, userinfo.UserInfoHandler)

site.registry(models.Course, course.CourseHandler)
