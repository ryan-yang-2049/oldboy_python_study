# -*- coding: utf-8 -*-

# __title__ = 'payment_record.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.26'
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.utils.safestring import mark_safe
from stark.service.v1 import StarkHandler, StarkModelForm, get_m2m_text, get_choice_text
from django.urls import reverse

from web import models

class PaymentRecordModelForm(StarkModelForm):
	class Meta:
		model = models.PaymentRecord
		fields = ['pay_type','paid_fee','class_list','note']


class PaymentRecordHandler(StarkHandler):
	list_display = [get_choice_text('缴费类型','pay_type'),'paid_fee','class_list','consultant',get_choice_text('状态','confirm_status')]

	model_form_class = PaymentRecordModelForm
	def get_list_display(self):
		"""
		不展示操作(编辑，删除列)
		:return:
		"""
		value = []
		if self.list_display:
			value.extend(self.list_display)
		return value

	def get_urls(self):
		patterns = [
			url(r'^list/(?P<customer_id>\d+)/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
			url(r'^add/(?P<customer_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
		]
		patterns.extend(self.extra_urls())
		return patterns

	def get_queryset(self, request, *args, **kwargs):
		customer_id = kwargs.get('customer_id')
		current_user_id = request.session['user_info']['id']
		print("customer_id====>",customer_id)
		print("current_user_id====>",current_user_id)
		return self.model_class.objects.filter(customer_id=customer_id,customer__consultant_id=current_user_id)




	def form_database_save(self, request, form, is_update, *args, **kwargs):
		customer_id = kwargs.get('customer_id')
		current_user_id = request.session['user_info']['id']

		object_exists = models.Customer.objects.filter(id=customer_id,consultant_id=current_user_id).exists()
		if not object_exists:
			return HttpResponse('非法操作')

		form.instance.customer_id = customer_id
		form.instance.consultant_id = current_user_id
		form.save()
