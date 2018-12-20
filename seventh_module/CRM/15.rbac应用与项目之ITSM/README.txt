提示：此django 应用主要是写一个根据RBAC权限控制的小练习，用于熟练使用RBAC，并记录操作步骤，以便以后方便使用


1.将rbac组件拷贝到项目中。(用于13目录的rbac代码，此小项目写完以后，就直接参照此文档以及此项目下的RBAC使用即可)
注册APP：settings.py中
	INSTALLED_APPS = [
		...
		'rbac.apps.RbacConfig',
	]


2.配置与删除
	2.1rbac/migrations 目录中的数据库迁移记录删除，只留下 __init__.py 文件即可。
	
	2.2 并且删除rbac/admin.py下的admin的注册
		from rbac import models

		admin.site.register(models.Permission)
		admin.site.register(models.UserInfo)
		admin.site.register(models.Role)
	2.3 删除rbac/urls.py 中关于用户管理的删除掉
		# url(r'^user/list/', user.user_list, name='user_list'),
		# url(r'^user/add/', user.user_add, name='user_add'),
		# url(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),
		# url(r'^user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),
		# url(r'^user/reset/password/(?P<pk>\d+)/$', user.user_reset_pwd, name='user_reset_pwd'),


3.业务系统中用户表结构的设计
"本人想法，可否用django自带的userinfo 然后，在rabc中添加想要的字段，在把rbac的表作为一个虚拟表，然后在到业务表中去继承(后面在尝试)"

	rbac/models.py 下面的UserInfo表
		class UserInfo(models.Model):
			"""
			用户表
			"""
			name = models.CharField(verbose_name='用户名', max_length=32)
			password = models.CharField(verbose_name='密码', max_length=64)
			email = models.CharField(verbose_name='邮箱', max_length=32)
			roles = models.ManyToManyField(verbose_name='拥有的所有角色', to=Role, blank=True)

			def __str__(self):
				return self.name

			class Meta:
				# 抽象方法,django以后在做迁移的时候，就不会再为rbac的这张UrseInfo表创建相关表结构和数据了
				# 此类可以作为 “父类”,被其他User表继承
				abstract = True
		严重提示： 这里要注意的是roles字段，创建的该表必须在Role表下面，因为，如果此表在Role表上面，那么在roles字段里面应该写成 to='Role' ,但是在别的项目中就会找不到该表。因此，此处会把这个Role的对象一起继承给子类
	
	cmdb/models.py  下面的用户表：
		此时就要去继承RbacUserInfo中的用户表
		from rbac.models import UserInfo as RbacUserInfo
		class UserInfo(RbacUserInfo):
			"""
			用户表
			"""
			phone = models.CharField(verbose_name='手机号', max_length=32)
			level_choices = (
				(1, 'T1'),
				(2, 'T2'),
				(3, 'T3'),
			)
			level = models.IntegerField(verbose_name='级别', choices=level_choices)
			depart = models.ForeignKey(verbose_name='部门', to='Department')

4.将业务中的用户表，以字符串的形式写到settings.py的配置文件中
	settings.py
		# 业务中的用户表
		RBAC_USER_MODLE_CLASS = "cmdb.models.UserInfo"	# 用于在rbac分配权限时，读取业务表中的用户信息
	在RBAC的menu路径下有使用到用户表，因此，在rbac/views/menu.py中，修改如下两处：
		from django.utils.module_loading import import_string
		from django.conf import settings
		user_model_calss = import_string(settings.RBAC_USER_MODLE_CLASS)	# 根据字符串的形式导入这个类
		user_object = user_model_calss.objects.filter(id=user_id).first()
		all_user_list = user_model_calss.objects.all()
	
5.在rbac下面放一个layout.html 模板文件，并引入静态文件
	templates下放入模板文件：layout.html 
	static下的静态目录：
			css	
			imgs
			js
			plugins

6.先关闭layout.html中用到的权限。等代码完成以后在加回来
		<div class="pg-body">
			<div class="left-menu">
				<div class="menu-body">
		{#            {% multi_menu request %}#}
				</div>
			</div>
			<div class="right-body">
				<div>
		{#            {% breadcrumb request %}#}
				</div>
				{% block content %} {% endblock %}
			</div>
		</div>

7.业务逻辑开发
	将所有的路由都要设置一个别名"name" ,因为，在rbac中会根据整个项目的url 进行自动发现
	
	7.1 用户表和主机表的增删改查
		- 用户表的增删改查
			1.ITSM/urls.py
				url(r'cmdb/',include('cmdb.urls',namespace='cmdb')),
			
			2.cmdb/urls.py
				url(r'^user/list/$', user.user_list, name='user_list'),
				url(r'^user/add/$', user.user_add, name='user_add'),
				url(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),
				url(r'^user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),
				url(r'^user/reset/password/(?P<pk>\d+)/$', user.user_reset_pwd, name='user_reset_pwd'),
			
			3.cmdb/views.py/user.py
				查看代码中的py代码
				注意，在menu_list.html中要注意的是：{% memory_url request 'cmdb:user_add' %}
					<a class="btn btn-default" href="{% memory_url request 'cmdb:user_add' %}">
						<i class="fa fa-plus-square" aria-hidden="true"></i> 添加用户
					</a>
		- 主机表的增删改查
			1.cmdb/urls.py
				url(r'^host/list/$', host.host_list, name='host_list'),
				url(r'^host/add/$', host.host_add, name='host_add'),
				url(r'^host/edit/(?P<pk>\d+)/$', host.host_edit, name='host_edit'),
				url(r'^host/del/(?P<pk>\d+)/$', host.host_del, name='host_del'),
			2.cmdb/views.py/host.py
				代码查看host.py文件即可
				也要注意 html文件中的  {% memory_url request 'cmdb:host_add' %}等
			
8.权限的应用

	8.1 创建以及权限菜单
		http://127.0.0.1:8000/rbac/menu/list/
		8.1.1 创建一级权限菜单：
					权限管理
					用户管理
					主机管理
		8.1.2 点击批量操作为一级权限菜单添加二级权限菜单以及非菜单权限

		8.1.3 添加角色
		8.1.4 添加用户
		8.1.5 为角色分配权限
		8.1.6 为用户分配角色
		

	
	8.2 增加layout.html中用到的权限（菜单和导航条，目的是为了动态生成菜单和导航条）
		<div class="pg-body">
			<div class="left-menu">
				<div class="menu-body">
					{% multi_menu request %}
				</div>
			</div>
			<div class="right-body">
				<div>
					{% breadcrumb request %}
				</div>
				{% block content %} {% endblock %}
			</div>
		</div>	
	
	
	8.3 中间件应用上
		MIDDLEWARE = [
			...
			'rbac.middlewares.rbac.RbacMiddleware',
		]
		
	8.4 白名单处理，在settings.py 中添加
		# 白名单
		VALID_URL_LIST = [
			'/login/',
			'/admin/.*'
		]
					
	8.5 权限初始化 settings.py 添加以下配置
		# 权限在Session中存储的key
		PERMISSION_SESSION_KEY = "luffy_permission_url_list_key"
		# 菜单在Session中存储的key
		MENU_SESSION_KEY = "luffy_permission_menu_key"

	8.6 批量操作权限时，自动发现路由中所有的URL时，应该排除的URL
		# 自动化发现路由中URL时，排除的URL
		AUTO_DISCOVER_EXCLUDE = [
			'/admin/.*',
			# '/login/',
			# '/logout/',
			# '/index/',
		]
	
	
	8.7 用户登陆逻辑
		写完用户登录权限，对于 /index/,/login/,/logout/ 三个是否分配权限？
		方案一：
			将 /index/,/logout/ 录入数据库，以后每个用户都分配该权限

		方案二: （推荐）
			默认用户登录后，都能访问 /index/ 和 /login/

			AUTO_DISCOVER_EXCLUDE = [
				'/admin/.*',
				'/login/',
				'/logout/',
				'/cmdb/index/',
			]
			增加的代码在 中间件中
			# 此处判断是否权限的url ： 登录成功无需权限就可访问的判断
			for url in settings.NO_PERMISSION_LIST:
				if re.match(url,request.path_info):
					request.current_selected_permission = 0
					request.breadcrumb = url_record

					return None



		# 白名单 表示不经过中间件的权限验证，直接就可以访问
		VALID_URL_LIST = [
			'/login/',
			'/admin/.*'
		]

		# 需要登录但无需权限的URL
		NO_PERMISSION_LIST = [
			'/index/',
			'/logout/',
			'/cmdb/index/',
		]

		# 自动化发现路由中URL时，排除的URL
		AUTO_DISCOVER_EXCLUDE = [
			'/admin/.*',
			'/login/',
			'/logout',
			'/cmdb/index/',

		]

		
		
到此处的目录：rbac权限基本完成。应用参照这个项目即可。
优化点：
	1.用户表是否可以使用django自带的用户表。
	2.某些跨应用调用的是否可以全部使用 如下方式进行调用
		from django.utils.module_loading import import_string
		from django.conf import settings
		user_model_calss = import_string(settings.RBAC_USER_MODLE_CLASS)
		user_object = user_model_calss.objects.filter(id=user_id).first()
		
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		