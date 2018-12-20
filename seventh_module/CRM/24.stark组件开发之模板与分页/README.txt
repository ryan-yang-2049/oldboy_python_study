视频 75-76  应用模板和 分页

1.应用样式
	设置模板  layout.html
https://www.cnblogs.com/smallmars/p/8657094.html
2.分页组件（在任何地方都可以使用，有时间可以仔细理解下）

class Pagination(object):

	def __init__(self, current_page, all_count, base_url, params, per_page_num=2, pager_count=11):
		"""
		封装分页相关数据
		:param current_page: 当前页
		:param all_count:    数据库中的数据总条数
		:param per_page_num: 每页显示的数据条数
		:param base_url: 分页中显示的URL前缀
		:param pager_count:  最多显示的页码个数
		"""

		try:
			current_page = int(current_page)
		except Exception as e:
			current_page = 1

		if current_page < 1:
			current_page = 1

		self.current_page = current_page

		self.all_count = all_count
		self.per_page_num = per_page_num
		self.base_url = base_url
		import copy
		params = copy.deepcopy(params)
		params._mutable = True
		self.params = params

		# 总页码
		all_pager, tmp = divmod(all_count, per_page_num)
		if tmp:
			all_pager += 1
		self.all_pager = all_pager
		self.pager_count = pager_count
		self.pager_count_half = int((pager_count - 1) / 2)

	@property
	def start(self):
		return (self.current_page - 1) * self.per_page_num

	@property
	def end(self):
		return self.current_page * self.per_page_num

	def page_html(self):
		# 如果总页码 < 11个：
		if self.all_pager <= self.pager_count:
			pager_start = 1
			pager_end = self.all_pager + 1
		# 总页码  > 11
		else:
			# 当前页如果<=页面上最多显示11/2个页码
			if self.current_page <= self.pager_count_half:
				pager_start = 1
				pager_end = self.pager_count + 1

			# 当前页大于5
			else:
				# 页码翻到最后
				if (self.current_page + self.pager_count_half) > self.all_pager:
					pager_end = self.all_pager + 1
					pager_start = self.all_pager - self.pager_count + 1
				else:
					pager_start = self.current_page - self.pager_count_half
					pager_end = self.current_page + self.pager_count_half + 1

		page_html_list = []
		self.params["page"] = 1
		first_page = '<li><a href="%s?%s">首页</a></li>' % (self.base_url, self.params.urlencode(),)
		page_html_list.append(first_page)

		if self.current_page <= 1:
			prev_page = '<li class="disabled"><a href="#">上一页</a></li>'
		else:
			self.params["page"] = self.current_page - 1
			prev_page = '<li><a href="%s?%s">上一页</a></li>' % (self.base_url, self.params.urlencode(),)

		page_html_list.append(prev_page)

		for i in range(pager_start, pager_end):
			self.params["page"] = i
			if i == self.current_page:
				temp = '<li class="active"><a href="%s?%s">%s</a></li>' % (self.base_url, self.params.urlencode(), i,)
			else:
				temp = '<li><a href="%s?%s">%s</a></li>' % (self.base_url, self.params.urlencode(), i,)
			page_html_list.append(temp)

		if self.current_page >= self.all_pager:
			next_page = '<li class="disabled"><a href="#">下一页</a></li>'
		else:
			self.params["page"] = self.current_page + 1
			next_page = '<li><a href="%s?%s">下一页</a></li>' % (self.base_url, self.params.urlencode(),)
		page_html_list.append(next_page)
		self.params["page"] = self.all_pager
		last_page = '<li><a href="%s?%s">尾页</a></li>' % (self.base_url, self.params.urlencode(),)
		page_html_list.append(last_page)

		return ''.join(page_html_list)

3.分页使用方法：
	all_data = self.model_class.objects.all()	# 数据库里面所有的数据
	query_params = request.GET.copy()   # copy方法是默认不能修改request.GET里面的参数的
	query_params._mutable = True    # 这样就可以修改request.GET 里面的参数值了

	pager = Pagination(
		current_page=request.GET.get('page'),	# 获取页面返回的获取的页码
		all_count = all_data.count(),			# 数据库里面所有数据的计算
		base_url = request.path_info,			# 访问的基础URL
		params = query_params,					# 用户URL里面的参数，例如 127.0.0.1/abc?name=ryan&age=18 里面的 name=ryan&age=18 ，它是 QueryDict类型
		per_page_num= self.per_page_num			# 这个是每页显示的个数(扩展，可以在网页端输入，然后在传入服务器端)
	)
	# 列表展示页使用分页的设置 （切片的应用）
	data_list = all_data[pager.start:pager.end]













