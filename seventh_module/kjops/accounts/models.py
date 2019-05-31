from django.db import models
from rbac.models import UserInfo as RbacUserInfo

class Department(models.Model):
	"""
	部门表
	"""
	title = models.CharField(verbose_name='部门名称', max_length=32)

	def __str__(self):
		return self.title



class UserInfo(RbacUserInfo):
	"""
	用户表
	"""
	nickname = models.CharField(verbose_name="姓名",max_length=32)
	status_choice = (
		(1,'启用'),
		(2,'禁用'),
	)
	status = models.BooleanField(verbose_name="状态",choices=status_choice,default=1)
	gender_choice = (
		(1,'男'),
		(2,'女'),
	)
	gender = models.IntegerField(verbose_name="性别",choices=gender_choice,default=1)

	depart = models.ForeignKey(verbose_name='部门',to='Department')

	def __str__(self):
		return self.nickname

