
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




视频66  stark组件开发之自动生成URL
		1.对以上三张表做增删改查
			a.分析
				- 为每张表创建4个url
				- 为每张表创建4个视图函数
					app01/models.py
						Depart
							/app01/depart/list/
							/app01/depart/add/
							/app01/depart/edit/(\d+)/
							/app01/depart/del/(\d+)/
						
						UserInfo
							/app01/userinfo/list/
							/app01/userinfo/add/
							/app01/userinfo/edit/(\d+)/
							/app01/userinfo/del/(\d+)/
						
					app02/models.py
						Host
							/app02/host/list/
							/app02/host/add/
							/app02/host/edit/(\d+)/
							/app02/host/del/(\d+)/
				提示：如果自己写的话，那就是3张表对应12个url和12个视图函数		
				
			b.为app中的每个model类自动创建URL以及相关视图函数
				
			





























	
	