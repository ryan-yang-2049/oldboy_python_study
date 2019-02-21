# -*- coding: utf-8 -*-
"""
__title__ = 'public_customer.py'
__author__ = 'yangyang'
__mtime__ = '2019-02-21'
"""

from stark.service.v1 import StarkHandler,StarkModelForm,get_choice_text,get_m2m_text
from web import models
class PublicCustomerModelForm(StarkModelForm):
	class Meta:
		model =models.Customer
		exclude = ['consultant',]


class PublicCustomerHandler(StarkHandler):
	list_display = ['name','qq',get_choice_text('状态','status'),get_choice_text('性别','gender'),
	                get_m2m_text('咨询的课程','course')]

	def get_queryset(self, request, *args, **kwargs):

		return self.model_class.objects.filter(consultant__isnull=True)

	model_form_class = PublicCustomerModelForm







