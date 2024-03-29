# -*- coding: utf-8 -*-
# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.24'


from stark.service.v1 import site
from web import models
from web.views import school, depart, userinfo, course, classs_list, public_customer, private_customer, consult_record

# 校区管理
site.registry(models.School, school.SchoolHandler)
# 部门管理
site.registry(models.Department, depart.DepartmentHandler)
# 用户管理
site.registry(models.UserInfo, userinfo.UserInfoHandler)
# 课程管理
site.registry(models.Course, course.CourseHandler)
# 班级管理
site.registry(models.ClassList, classs_list.ClassListHandler)
# 公共客户管理
site.registry(models.Customer, public_customer.PublicCustomerHandler, prev='pub')
# 私有客户管理
site.registry(models.Customer, private_customer.PrivateCustomerHandler, prev='priv')
# 跟进记录管理
site.registry(models.ConsultRecord, consult_record.ConsultRecordHandler)
