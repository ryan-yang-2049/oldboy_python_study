
1.创建一个django project 并创建三个app[01-02]以及stark
	python3 manage.py startapp app01	# 业务逻辑
	python3 manage.py startapp app02	# 业务逻辑
	python3 manage.py startapp stark	# Stark组件的产出

2.创建基础业务表
	app01:
		
		class Depart(models.Model):
			"""
			部门表
			"""
			title = models.CharField(verbose_name='部门名称',max_length=32)
			
		class UserInfo(models.Model):
			"""
			用户表
			"""
			name = models.CharField(verbose_name='姓名',max_length=32)
			age = models.CharField(verbose_name='年龄',max_length=32)
			email = models.CharField(verbose_name='邮箱',max_length=32)
			depart = models.ForeignKey(verbose_name='部门',to=Depart)

	
	app02:
		class Host(models.Model):
			"""
			主机表
			"""
			host = models.CharField(verbose_name='主机名',max_length=32)
			ip = models.GenericIPAddressField(verbose_name='IP',protocol='both')    # protocol='both' 表示既支持IPV4 也支持IPV6





































	
	