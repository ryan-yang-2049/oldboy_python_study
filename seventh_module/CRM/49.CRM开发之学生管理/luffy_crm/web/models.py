from django.db import models
from rbac.models import UserInfo as RbacUserInfo


class School(models.Model):
	"""
	校区表:
	如：
		北京昌平校区
		上海浦东校区
		深圳南山校区
	"""
	title = models.CharField(verbose_name='校区名称', max_length=32)

	def __str__(self):
		return self.title


class Department(models.Model):
	"""
	部门表
	"""

	title = models.CharField(verbose_name='部门名称', max_length=32)

	def __str__(self):
		return self.title


class UserInfo(RbacUserInfo):
	"""
	员工表
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


class Course(models.Model):
	"""
	课程表
	如：
		Linux基础
		Linux架构师
		Python自动化
		Python全栈
	"""
	name = models.CharField(verbose_name='课程名称', max_length=32)

	def __str__(self):
		return self.name


class ClassList(models.Model):
	"""
	班级表
	如：
		Python全栈  面授班  5期  10000  2017-11-11  2018-5-11
	"""
	school = models.ForeignKey(verbose_name='校区', to='School')
	course = models.ForeignKey(verbose_name='课程名称', to='Course')
	semester = models.PositiveIntegerField(verbose_name="班级(期)")
	price = models.PositiveIntegerField(verbose_name="学费")
	start_date = models.DateField(verbose_name="开班日期")
	graduate_date = models.DateField(verbose_name="结业日期", null=True, blank=True)
	class_teacher = models.ForeignKey(verbose_name='班主任', to='UserInfo', related_name='classes',
	                                  limit_choices_to={'depart__title': '教质部'})
	tech_teachers = models.ManyToManyField(verbose_name='任课老师', to='UserInfo', related_name='teach_classes', blank=True,
	                                       limit_choices_to={'depart__title__in': ['Linux教学部', 'Python教学部']})
	memo = models.TextField(verbose_name='说明', max_length=255, blank=True, null=True)

	def __str__(self):
		return "{0}({1}期)".format(self.course.name, self.semester)


class Customer(models.Model):
	"""
	客户表
	"""
	name = models.CharField(verbose_name='姓名', max_length=32)
	qq = models.CharField(verbose_name='联系方式', max_length=64, unique=True, help_text='QQ号/微信/手机号')
	status_choices = [
		(1, "已报名"),
		(2, "未报名")
	]
	status = models.IntegerField(verbose_name="状态", choices=status_choices, default=2)
	gender_choices = ((1, '男'), (2, '女'))
	gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)

	source_choices = [
		(1, "qq群"),
		(2, "内部转介绍"),
		(3, "官方网站"),
		(4, "百度推广"),
		(5, "360推广"),
		(6, "搜狗推广"),
		(7, "腾讯课堂"),
		(8, "广点通"),
		(9, "高校宣讲"),
		(10, "渠道代理"),
		(11, "51cto"),
		(12, "智汇推"),
		(13, "网盟"),
		(14, "DSP"),
		(15, "SEO"),
		(16, "其它"),
	]
	source = models.SmallIntegerField('客户来源', choices=source_choices, default=1)

	referral_from = models.ForeignKey(
		'self',
		blank=True,
		null=True,
		verbose_name="转介绍自学员",
		help_text="若此客户是转介绍自内部学员,请在此处选择内部学员姓名",
		related_name="internal_referral"
	)

	course = models.ManyToManyField(verbose_name="咨询课程", to="Course")
	consultant = models.ForeignKey(verbose_name="课程顾问", to='UserInfo', related_name='consultant',
	                               null=True, blank=True,
	                               limit_choices_to={'depart__title': '销售部'})
	education_choices = (
		(1, '重点大学'),
		(2, '普通本科'),
		(3, '独立院校'),
		(4, '民办本科'),
		(5, '大专'),
		(6, '民办专科'),
		(7, '高中'),
		(8, '其他')
	)
	education = models.IntegerField(verbose_name='学历', choices=education_choices, blank=True, null=True, )
	graduation_school = models.CharField(verbose_name='毕业学校', max_length=64, blank=True, null=True)
	major = models.CharField(verbose_name='所学专业', max_length=64, blank=True, null=True)

	experience_choices = [
		(1, '在校生'),
		(2, '应届毕业'),
		(3, '半年以内'),
		(4, '半年至一年'),
		(5, '一年至三年'),
		(6, '三年至五年'),
		(7, '五年以上'),
	]
	experience = models.IntegerField(verbose_name='工作经验', blank=True, null=True, choices=experience_choices)
	work_status_choices = [
		(1, '在职'),
		(2, '无业')
	]
	work_status = models.IntegerField(verbose_name="职业状态", choices=work_status_choices, default=1, blank=True,
	                                  null=True)
	company = models.CharField(verbose_name="目前就职公司", max_length=64, blank=True, null=True)
	salary = models.CharField(verbose_name="当前薪资", max_length=64, blank=True, null=True)

	date = models.DateField(verbose_name="咨询日期", auto_now_add=True)
	last_consult_date = models.DateField(verbose_name="最后跟进日期", auto_now_add=True)

	def __str__(self):
		return "姓名:{0},联系方式:{1}".format(self.name, self.qq, )


class ConsultRecord(models.Model):
	"""
	客户跟进记录
	"""
	customer = models.ForeignKey(verbose_name="所咨询客户", to='Customer')
	consultant = models.ForeignKey(verbose_name="跟踪人", to='UserInfo')
	note = models.TextField(verbose_name="跟进内容")
	date = models.DateField(verbose_name="跟进日期", auto_now_add=True)


class PaymentRecord(models.Model):
	"""
	缴费申请
	"""
	customer = models.ForeignKey(Customer, verbose_name="客户")
	consultant = models.ForeignKey(verbose_name="课程顾问", to='UserInfo', help_text="谁签的单就选谁")
	pay_type_choices = [
		(1, "报名费"),
		(2, "学费"),
		(3, "退学"),
		(4, "其他"),
	]
	pay_type = models.IntegerField(verbose_name="费用类型", choices=pay_type_choices, default=1)
	paid_fee = models.IntegerField(verbose_name="金额", default=0)
	class_list = models.ForeignKey(verbose_name="申请班级", to="ClassList")
	apply_date = models.DateTimeField(verbose_name="申请日期", auto_now_add=True)

	confirm_status_choices = (
		(1, '申请中'),
		(2, '已确认'),
		(3, '已驳回'),
	)
	confirm_status = models.IntegerField(verbose_name="确认状态", choices=confirm_status_choices, default=1)
	confirm_date = models.DateTimeField(verbose_name="确认日期", null=True, blank=True)
	confirm_user = models.ForeignKey(verbose_name="审批人", to='UserInfo', related_name='confirms', null=True, blank=True)

	note = models.TextField(verbose_name="备注", blank=True, null=True)


class Student(models.Model):
	"""
	学生表
	"""
	customer = models.OneToOneField(verbose_name='客户信息', to='Customer')
	qq = models.CharField(verbose_name='QQ号', max_length=32)
	mobile = models.CharField(verbose_name='手机号', max_length=32)
	emergency_contract = models.CharField(verbose_name='紧急联系人电话', max_length=32)
	class_list = models.ManyToManyField(verbose_name="已报班级", to='ClassList', blank=True)
	student_status_choices = [
		(1, "申请中"),
		(2, "在读"),
		(3, "毕业"),
		(4, "退学")
	]
	student_status = models.IntegerField(verbose_name="学员状态", choices=student_status_choices, default=1)
	memo = models.TextField(verbose_name='备注', max_length=255, blank=True, null=True)

	def __str__(self):
		return self.customer.name
