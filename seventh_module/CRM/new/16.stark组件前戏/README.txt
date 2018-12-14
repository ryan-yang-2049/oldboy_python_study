视频 59-64
stark组件：
	介绍：
		stark组件，是一个帮助开发者快速实现数据库表的增删改查
	
	目标：
		10秒钟 完成一张表的增删改查
	
	
	前戏：
		1.django 项目启动时，自定义执行某个py文件
			django项目启动时, 且在读取项目中路由之前执行某个py文件
			1.1 创建一个django 项目 prev_luffy_stark
			1.2 创建两个app：
				python3 manage.py startapp app01
				python3 manage.py startapp app02
			1.3 注册APP
				
				INSTALLED_APPS = [
					....
					'app01.apps.App01Config',
					'app02.apps.App02Config',
				]
			
			1.4 在任意app的apps.py中的Config类中定义ready方法，并调用autodiscover_modules
				from django.apps import AppConfig
				from django.utils.module_loading import autodiscover_modules

				class App01Config(AppConfig):
					name = 'app01'

					def ready(self):
						autodiscover_modules('xxxx')
				django启动时，就会去已注册的所有app的目录下,找到 xxxx.py 的py文件,并自动导入。
			
			1.5 如果执行两次，是因为django内部自动重启导致
				python3 manage.py runserver 127.0.0.1:8001 --noreload    只执行一遍
				
			提示：
				如果 xxxx.py 执行的代码向 “某个神奇的地方” 放入了一些值。之后的路由加载时，可以去“某个神奇的地方” 读取到原来设置的值
		
		
		2.单例模式
			单：一个。
			例：实例，对象。
			模式：方法。
			
			通过利用 python模块导入的特性：在python中，如果已经导入过的文件再次被重新导入时，python不会重新在解释一遍，而是选择从内存中直接将原来导入的值拿来用
			utils.py
				class AdminSite(object):
					pass
				site = AdminSite()  # 为AdminSite类创建了一个对象（实例）
			
			commons.py
				import utils
				print(utils.site)
			
			app.py
				import utils
				print(utils.site)   # <utils.AdminSite object at 0x0000021C493481D0>
				# import utils
				# print(utils.site)   # <utils.AdminSite object at 0x0000021C493481D0>
				import commons
				-------------------------------------------------------------------------------------
				执行app.py 的结果是：
					<utils.AdminSite object at 0x000001910513F358>
					<utils.AdminSite object at 0x000001910513F358>
				-------------------------------------------------------------------------------------
			
			提示: 
				如果以后存在一个单例模式的对象，可以现在此对象中放入一个值，然后在其他的文件中导入该对象。通过对象再次将值获取到。
				utils.py
					class AdminSite(object):
						pass
					site = AdminSite()  # 为AdminSite类创建了一个对象（实例）
				
				commons.py
					import utils
					print(utils.site)
				
				app.py
					import utils
					utils.site.name="ryan"   # <utils.AdminSite object at 0x0000021C493481D0>
					# import utils
					# print(utils.site)   # <utils.AdminSite object at 0x0000021C493481D0>
					import commons
				-------------------------------------------------------------------------------------
				执行app.py 的结果是：
						ryan
				-------------------------------------------------------------------------------------
			
		3.django路由分发的本质include
			方式一：
				from django.conf.urls import url,include
				urlpatterns = [
					url(r'^web/', include('app01.urls')),
				]
			方式二：
				include函数主要返回三个元素的元组。
				from app01 import urls
				urlpatterns = [
					url(r'^web/', (urls, app_name, namespace)),	# 第一个参数是urls文件对象，通过此对象可以获取urls.patterns获取分发的路由
				]

				在源码内部，读取路由前"(urls, app_name, namespace)"：
					如果第一个参数有 urls.patterns属性，那么子路由就从该属性中获取。
					如果第一个参数无 urls.patterns属性，那么子路由就是第一个参数 urls
			方式三：
				include函数主要返回三个元素的元组。
				from app01 import urls
				urlpatterns = [
					url(r'^web/', ([
						    url(r'^index/', views.index),
							url(r'^home/', views.home),
							], app_name, namespace)),	# 第一个参数是urls文件对象，通过此对象可以获取urls.patterns获取分发的路由
				]
		
				例如：
					from django.conf.urls import url,include
					from app01 import views

					urlpatterns = [
						url(r'^web/', ([
									   url(r'^index/', views.index),
									   url(r'^home/', views.home),
									   ], None, None)),
]
		
		
			include分发的本质就是返回一个： return (urlconf_module, app_name, namespace)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	