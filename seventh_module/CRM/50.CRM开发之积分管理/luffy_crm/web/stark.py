# -*- coding: utf-8 -*-
# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.24'


from stark.service.v1 import site
from web import models
from web.views import school, depart, userinfo, course, classs_list, public_customer, private_customer, consult_record, \
	payment_record, check_payment_record, student,score_record

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

# 缴费记录
site.registry(models.PaymentRecord, payment_record.PaymentRecordHandler)

# 缴费审批
site.registry(models.PaymentRecord, check_payment_record.CheckPaymentRecordHandler, prev='check')

# 学生管理
site.registry(models.Student, student.StudentHandler)

# 积分管理
site.registry(models.ScoreRecord, score_record.ScoreRecordHandler)
