from django.db import models

class Permission(models.Model):
	"""
	权限表
	"""
	title = models.CharField(verbose_name="标题",max_length=32)
	url = models.CharField(verbose_name="含正则的URL",max_length=128)

	def __str__(self):
		return self.title

class Role(models.Model):
	"""
	角色
	"""
	title = models.CharField(verbose_name="角色名称",max_length=32)
	permissions =models.ManyToManyField(verbose_name="拥有的所有权限",to="Permission",blank=True)

	def __str__(self):
		return self.title


class UserInfo(models.Model):
	"""
	用户表
	"""
	name = models.CharField(verbose_name='用户名',max_length=32)
	password = models.CharField(verbose_name="密码",max_length=64)
	email = models.CharField(verbose_name="邮箱",max_length=32)
	roles = models.ManyToManyField(verbose_name="拥有的所有角色",to='Role',blank=True)

	def __str__(self):
		return self.name


"""
current_user =models.UserInfo.objects.filter(name=user,password=pwd).first()

# 获取当前用户所有角色
role_list = current_user.roles.all()

# 获取当前用户所有的权限（连表跨表查询）
permission_list = current_user.roles.all().values("permissions__url","permission__id").distinct()

# 获取当前用户所有的权限并且permission 不为空
permission_list = current_user.roles.filter(permissions__isnull=False).values("permissions__url","permission__id").distinct()

# 问题一：
	1.一个用户是否可以拥有多个角色？是
	2.一个角色是否可以拥有多个权限？是
	
		CEO：
			/index/
			/order/
		总监：
			/index/
			/customer/
		销售：
			/user/
			/add_user/
		
		当一个用户同事拥有上面三个角色，那么 /index/ 就重复了，因此就需要去重
		
# 问题二：
		CEO：
			/index/
			/order/
		总监：
			/index/
			/customer/
		销售：
			/user/
			/add_user/
		金牌讲师：
			无url   "null"
"""