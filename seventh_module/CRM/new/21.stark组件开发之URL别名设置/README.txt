视频 69 URL别名设置

捋一下实现思路
	- 动态生成URL
	
	- 将试图提取到基类中
	
	- URL分发扩展 & URL前缀(后缀)

	- 为URL别名设置
			def get_url_name(self, param):
				app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
				if self.prev:
					return '%s_%s_%s_%s' % (app_label, model_name, self.prev, param)
				return '%s_%s_%s' % (app_label, model_name, param)

			@property
			def get_list_url_name(self):
				"""
				获取列表页面URL的name
				:return:
				"""
				return self.get_url_name('list')

			@property
			def get_add_url_name(self):
				"""
				获取添加页面URL的name
				:return:
				"""
				return self.get_url_name('add')

			@property
			def get_change_url_name(self):
				"""
				获取修改页面URL的name
				:return:
				"""
				return self.get_url_name('change')

			@property
			def get_delete_url_name(self):
				"""
				获取删除页面URL的name
				:return:
				"""
				return self.get_url_name('delete')

			def get_urls(self):
				patterns = [
					url(r'^list/$', self.changelist_view, name=self.get_list_url_name),
					url(r'^add/$', self.add_view, name=self.get_add_url_name),
					url(r'^change/$', self.change_view, name=self.get_change_url_name),
					url(r'^del/$', self.delete_view, name=self.get_delete_url_name),
				]
				patterns.extend(self.extra_urls())
				return patterns

	到这里，url的自动生成，以及别名就设置完毕





























