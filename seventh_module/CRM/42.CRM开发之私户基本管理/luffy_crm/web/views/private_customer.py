# -*- coding: utf-8 -*-
"""
__title__ = 'private_customer.py'
__author__ = 'yangyang'
__mtime__ = '2019-02-21'
"""

from stark.service.v1 import StarkHandler, StarkModelForm, get_m2m_text, get_choice_text

from web import models


class PrivateCustomerModelForm(StarkModelForm):
	class Meta:
		model = models.Customer
		exclude = ['consultant', ]


class PrivateCustomerHandler(StarkHandler):
	model_form_class = PrivateCustomerModelForm
	list_display = [StarkHandler.display_checkbox, 'name', 'qq', get_choice_text('性别', 'gender'),
	                get_m2m_text('咨询的课程', 'course'), get_choice_text('状态', 'status')]

	def get_queryset(self, request, *args, **kwargs):
		current_user_id = request.session['user_info']['id']
		print(current_user_id)
		# 拿到当前用户申请到的客户
		return self.model_class.objects.filter(consultant_id=current_user_id)

	def form_database_save(self, request, form, is_update, *args, **kwargs):
		if not is_update:
			current_user_id = request.session['user_info']['id']
			form.instance.consultant_id = current_user_id
		form.save()



	def action_multi_remove(self, request, *args, **kwargs):
		"""
		把私户批量移除到公户
		:param request:
		:return:
		"""
		current_user_id = request.session['user_info']['id']
		pk_list = request.POST.getlist('pk')

		self.model_class.objects.filter(id__in=pk_list,consultant_id=current_user_id).update(consultant_id=None)


	action_multi_remove.text = "批量移动到公户"

	action_list = [action_multi_remove,]




