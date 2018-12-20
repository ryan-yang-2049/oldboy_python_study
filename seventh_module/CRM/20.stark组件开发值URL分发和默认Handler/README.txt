视频 68
app01/stark.py
	class DepartHandler(StarkHandler):

		# 预留的钩子函数，用于单独的对象添加额外的URL
		def extra_urls(self):
			"""
			额外的增加URL
			:return:
			"""
			extar_patterns = [
				url(r'^detail/(\d+)/$', self.detail_view),
			]
			"""
			除了默认的URL,还新增了一个URL
					^stark/ app01/depart/ ^list/$
					^stark/ app01/depart/ ^add/$
					^stark/ app01/depart/ ^change/$
					^stark/ app01/depart/ ^del/$
					^stark/ app01/depart/ ^detail/(\d+)/$
			"""
			return extar_patterns

		def detail_view(self, request, pk):
			return HttpResponse("详情页面")

	site.registry(models.Depart, DepartHandler)

	class UserInfoHandler(StarkHandler):
		# 对于某个对象需要减少几个URL,那就单独写这个函数并加上需要的URL即可
		def get_urls(self):
			"""
			修改父类 StarkHandler 默认的URL
			:return:
			"""
			patterns = [
				url(r'^list/$', self.changelist_view),
				url(r'^add/$', self.add_view),
			]
			"""
			就剩下两个URL：
				^stark/ app01/userinfo/ ^list/$
				^stark/ app01/userinfo/ ^add/$
			"""
			return patterns

	site.registry(models.UserInfo, UserInfoHandler)

	"""
	URL加前缀
	site.registry(models.UserInfo,prev='private')
	site.registry(models.UserInfo,prev='public')
	这样就会生成8个带前缀的url
		^stark/ app01/userinfo/private/list/$
		^stark/ app01/userinfo/private/add/$
		^stark/ app01/userinfo/private/change/(\d+)/$
		^stark/ app01/userinfo/private/del/(\d+)/$
		
		^stark/ app01/userinfo/public/list/$
		^stark/ app01/userinfo/public/add/$
		^stark/ app01/userinfo/public/change/(\d+)/$
		^stark/ app01/userinfo/public/del/(\d+)/$


	site.registry(models.UserInfo)
	如果不写，就只有4个URL
		^stark/ app01/userinfo/list/$
		^stark/ app01/userinfo/add/$
		^stark/ app01/userinfo/change/(\d+)/$
		^stark/ app01/userinfo/del/(\d+)/$
"""

stark/service/v1.py
	class StarkHandler(object):
		def __init__(self, model_class):
			self.model_class = model_class  # 此时的model_class 是一个对象

		def changelist_view(self, request):
			"""
			列表页面
			:param request:
			:return:
			"""
			data_list = self.model_class.objects.all()
			# print(data_list)
			return render(request, 'stark/changelist.html', locals())

		def add_view(self, request):
			"""
			添加页面
			:param request:
			:return:
			"""
			return HttpResponse('添加页面')

		def change_view(self, request, pk):
			"""
			编辑页面
			:param request:
			:return:
			"""
			return HttpResponse('编辑页面')

		def delete_view(self, request, pk):
			"""
			删除页面
			:param request:
			:param pk:
			:return:
			"""
			return HttpResponse('删除页面')

		def get_urls(self):
			patterns = [
				url(r'^list/$', self.changelist_view),
				url(r'^add/$', self.add_view),
				url(r'^change/$', self.change_view),
				url(r'^del/$', self.delete_view),
			]
			patterns.extend(self.extra_urls())
			return patterns

		def extra_urls(self):
			return []

	class StarkSite(object):
		def __init__(self):
			self._registry = []
			self.app_name = 'stark'
			self.namespace = 'stark'

		def registry(self, model_class, handler_calss=None, prev=None):
			"""

			:param model_class: 是调用此方法的app中的 models中相关的类  例如：models.UserInfo
			:param handler_calss: 处理请求的视图函数所在的类
			:param prev: 生成 url 的前缀
			:return:
			"""
			if not handler_calss:
				handler_calss = StarkHandler  # StarkHandler 就是上面创建的类

			self._registry.append({'model_class': model_class, 'handler': handler_calss(model_class), 'prev': prev})
			"""
			site._registry = [
				{'prev':None,'model_class': <class 'app01.models.Depart'>, 'handler': DepartHandler(models.Depart)对象中有一个model_class=models.Depart},
				{'prev':private,'model_class': <class 'app01.models.UserInfo'>, 'handler': StarkHandler(models.UserInfo)对象中有一个model_class=models.UserInfo},    
				{'prev':None,'model_class': <class 'app02.models.Host'>, 'handler': StarkHandler(models.Host)对象中有一个model_class=models.Host}
				]
			"""

		def get_urls(self):
			patterns = []
			for item in self._registry:
				model_class = item['model_class']
				handler = item['handler']  # 此时的handler 其实是一个对象；例如：StarkHandler(models.UserInfo) 对象
				prev = item['prev']
				app_label, model_name = model_class._meta.app_label, model_class._meta.model_name
				# app_label 表示项目下某个应用的名称  ：app01
				# model_name 表示应用的表名称(小写) ：depart
				if prev:  # url中带前缀的
					# patterns.append(url(r'%s/%s/%s/list/$' % (app_label, model_name, prev), handler.changelist_view))
					# patterns.append(url(r'%s/%s/%s/add/$' % (app_label, model_name, prev), handler.add_view))
					# patterns.append(url(r'%s/%s/%s/change/(\d+)/$' % (app_label, model_name, prev), handler.change_view))
					# patterns.append(url(r'%s/%s/%s/del/(\d+)/$' % (app_label, model_name, prev), handler.delete_view))
					patterns.append(url(r'%s/%s/%s/' % (app_label, model_name, prev), (handler.get_urls(), None, None)))

				else:  # url中不带前缀的
					patterns.append(url(r'%s/%s/' % (app_label, model_name), (handler.get_urls(), None, None)))

			return patterns

		def urls(self):
			return self.get_urls(), self.app_name, self.namespace

	site = StarkSite()

1.到这里其实可以明显的感觉到，所有的应用都基于 include的原理在进行url的增删改查。
2.类的继承，以及实例化后读取类的方法时：先查看子类里面是否有这个函数，然后在到父类里面查看是否有这个函数
3.钩子函数，可以动态的添加
4.类的继承，可以减少URL的个数
5.对象的实例化，可以多增加几个URL，例如：给URL加前缀，
		
