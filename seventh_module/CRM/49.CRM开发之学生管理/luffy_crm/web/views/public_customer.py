# -*- coding: utf-8 -*-
"""
__title__ = 'public_customer.py'
__author__ = 'yangyang'
__mtime__ = '2019-02-21'
"""
from django.conf.urls import url
from django.utils.safestring import mark_safe
from django.shortcuts import HttpResponse, render
from django.db import transaction


from stark.service.v1 import StarkHandler, StarkModelForm, get_choice_text, get_m2m_text, Option
from web import models


class PublicCustomerModelForm(StarkModelForm):
	class Meta:
		model = models.Customer
		exclude = ['consultant', ]


class PublicCustomerHandler(StarkHandler):

	def display_record(self, obj=None, is_header=None,*args, **kwargs):
		if is_header:
			return '跟进记录'

		record_url = self.reverse_commons_url(self.get_url_name('record_view'), pk=obj.pk)
		return mark_safe('<a href="%s">查看跟进</a>' % record_url)

	list_display = [StarkHandler.display_checkbox, 'name', 'qq', get_choice_text('状态', 'status'),
	                get_choice_text('性别', 'gender'),
	                get_m2m_text('咨询的课程', 'course'), display_record]

	def get_queryset(self, request, *args, **kwargs):

		return self.model_class.objects.filter(consultant__isnull=True)

	model_form_class = PublicCustomerModelForm

	def extra_urls(self):
		patterns = [
			url(r'^record/(?P<pk>\d+)/$', self.wrapper(self.record_view),
			    name=self.get_url_name('record_view'))
		]

		return patterns

	def record_view(self, request, pk):
		"""
		查看跟进记录视图
		:param request:
		:param pk:
		:return:
		"""
		record_list = models.ConsultRecord.objects.filter(customer_id=pk)

		return render(request, 'record_view.html', {'record_list': record_list})

	def action_multi_apply(self, request, *args, **kwargs):
		"""
		批量申请到私户
		:param request:
		:return:
		"""
		"""
		# 基本实现--
		current_user_id = 6

		# 客户ID 列表
		pk_list = request.POST.getlist('pk')

		# 将选中的客户更新到我的私户(consultant=当前用户)
		models.Customer.objects.filter(id__in=pk_list,status=2,consultant__isnull=True).update(consultant_id=current_user_id)
		"""
		current_user_id = request.session['user_info']['id']
		pk_list = request.POST.getlist('pk')
		private_customer_count = models.Customer.objects.filter(consultant_id=current_user_id, status=2).count()
		# 私户个数的限制
		if private_customer_count + len(pk_list) > 150:
			return HttpResponse('做人不要太贪心，私户中已有%s个客户,最多只能申请 %s' % (private_customer_count, 150 - private_customer_count))

		# 数据库中加锁

		flag = False
		with transaction.atomic():  # 事务
			# 在数据库中加锁
			# 防止多个用户同时提交一个相同的客户到自己的私户
			origin_queryser = models.Customer.objects.filter(id__in=pk_list, status=2,
			                                                 consultant__isnull=True).select_for_update()
			if len(origin_queryser) == len(pk_list):
				models.Customer.objects.filter(id__in=pk_list, status=2, consultant__isnull=True).update(
					consultant_id=current_user_id)
				flag = True
		if not flag:
			return HttpResponse('手速太慢了，选中的客户已被其他人申请走')

	action_multi_apply.text = "申请到私户"

	action_list = [action_multi_apply, ]

	search_list = ['name__contains', 'status__contains', ]
	search_group = [
		Option('status'),
		Option('course')
	]
