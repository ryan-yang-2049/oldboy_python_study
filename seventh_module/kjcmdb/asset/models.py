from django.db import models
from rbac.models import UserInfo as RbacUserInfo


class Department(models.Model):
	"""
	登陆用户部门表
	"""
	title = models.CharField(verbose_name='部门名称', max_length=32)
	pid = models.ForeignKey(verbose_name='关联部门', to='Department', null=True, blank=True, related_name='parents',
	                        help_text='对于一个部门,可以选择一个上级部门')

	def __str__(self):
		return self.title


class UserInfo(RbacUserInfo):
	"""
	登陆用户表
	"""
	nickname = models.CharField(verbose_name="姓名", max_length=16)
	phone = models.CharField(verbose_name="手机号", max_length=32)
	gender_choice = (
		(1, '男'),
		(2, '女'),
	)
	gender = models.IntegerField(verbose_name="性别", choices=gender_choice, default=1)
	depart = models.ForeignKey(verbose_name='部门', to="Department")

	def __str__(self):
		return self.nickname


class Machine(models.Model):
	"""
	虚拟机
	"""
	host = models.CharField(verbose_name='主机名称', max_length=32)
	intranet = models.GenericIPAddressField(verbose_name='内网IP', db_index=True)
	external = models.GenericIPAddressField(verbose_name='外网IP', null=True, blank=True)
	specification = models.CharField(verbose_name='规格', max_length=32, null=True, blank=True, default="4C8G")
	system = models.CharField(verbose_name='操作系统', max_length=32, null=True, blank=True)
	system_satus = (
		(1, '使用中'),
		(2, '待删除'),
	)
	status = models.IntegerField(verbose_name='状态', choices=system_satus, default=1)
	principal = models.CharField(verbose_name='负责人', max_length=32, null=True, blank=True)
	supplier_choice = (
		(1, '本地机房'),
		(2, '阿里云'),
	)
	supplier = models.IntegerField(verbose_name='供应商', choices=supplier_choice, default=1)
	remark = models.TextField(verbose_name='备注', blank=True, null=True)

	def __str__(self):
		return self.intranet

class DeployService(models.Model):
	''' 部署的 服务 or 应用信息'''
	name = models.CharField(verbose_name='服务名称', max_length=32)
	deployip = models.ManyToManyField(verbose_name='部署地址', to='Machine')
	deployport = models.IntegerField(verbose_name='部署端口')
	env_choice = (
		(1, '生产环境'),
		(2, '准生产环境'),
		(3, '测试环境'),
		(4, '开发环境'),
	)
	env = models.IntegerField(verbose_name='部署环境', choices=env_choice)


class EmployeeDepartment(models.Model):
	"""
	员工部门表
	"""
	title = models.CharField(verbose_name='部门名称', max_length=32)

	def __str__(self):
		return self.title

class Employee(models.Model):
	"""
	员工表
	"""
	name = models.CharField(verbose_name='姓名', max_length=32)
	depart = models.ForeignKey(verbose_name='部门', to=EmployeeDepartment)

	def __str__(self):
		return self.name


class FixPhone(models.Model):
	user = models.CharField(verbose_name='使用者', max_length=32)
	depart = models.CharField(verbose_name='所属部门',max_length=32)
	extension = models.IntegerField(verbose_name='分机号')
	straight_line = models.IntegerField(verbose_name='直线号码', default=38959191,null=True, blank=True)


class OfficeEquipment(models.Model):
	asset_code = models.CharField(verbose_name='资产编码', max_length=32)
	assrt_status = (
		(1, '闲置'),
		(2, '使用中'),
		(3, '报废'),
	)
	status = models.IntegerField(verbose_name='设备状态', choices=assrt_status, default=1)
	type_choice = (
		(1, '笔记本'),
		(2, '台式机'),
		(3, '显示器'),
		(4, '鼠标'),
		(5, 'IPAD'),
		(6, '服务器'),
		(7, '投影仪'),
		(7, '手机'),
	)
	types = models.IntegerField(verbose_name='设备类型', choices=type_choice, default=1)
	department = models.ForeignKey(verbose_name='使用部门', to=EmployeeDepartment, null=True, blank=True)
	sn = models.CharField(verbose_name='序列号', max_length=128, null=True, blank=True)
	buydate = models.DateField(verbose_name='购买日期', max_length=128, auto_now_add=True)
	warrantydate = models.DateField(verbose_name='保修日期', null=True, blank=True)
	user = models.ForeignKey(verbose_name='使用者', to='Employee', null=True, blank=True)
	cpu = models.CharField(verbose_name='cpu', max_length=32, null=True, blank=True)
	mem = models.CharField(verbose_name='内存', max_length=32, null=True, blank=True)
	system = models.CharField(verbose_name='系统', max_length=32, null=True, blank=True)
	remark = models.TextField(verbose_name='备注', blank=True, null=True)




