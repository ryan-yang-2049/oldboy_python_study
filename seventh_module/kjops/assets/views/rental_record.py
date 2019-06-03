# -*- coding: utf-8 -*-

# __title__ = 'rental_record.py'
# __author__ = 'Administrator'
# __mtime__ = '2019/5/31'

from django.conf.urls import url
from django.utils.safestring import mark_safe

from stark.service.v1 import  StarkHandler,get_choice_text,get_datetime_text
from assets.forms.rental_record_forms import RentalRecordModelForm
from assets import models
class RentalRecordHandler(StarkHandler):

	list_display = ['computer','user',get_choice_text('状态','rental_status'),get_datetime_text('借出/归还时间','rental_time'),'note']

	def display_edit_del(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return '操作'
		computer_id = kwargs.get('computer_id')
		tpl = '<a class="btn btn-sm btn-warning" href="%s">编辑</a>&nbsp;&nbsp;<a class="btn btn-sm btn-danger" href="%s">删除</a>' % (
			self.reverse_change_url(pk=obj.pk, computer_id=computer_id),
			self.reverse_delete_url(pk=obj.pk, computer_id=computer_id))
		return mark_safe(tpl)



	model_form_class = RentalRecordModelForm
	def get_urls(self):
		patterns = [
			url(r'^list/(?P<computer_id>\d+)/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
			url(r'^add/(?P<computer_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
			url(r'^change/(?P<computer_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.change_view), name=self.get_change_url_name),
			url(r'^delete/(?P<computer_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.delete_view), name=self.get_delete_url_name),
		]
		patterns.extend(self.extra_urls())
		return patterns

	def get_add_btn(self, request, *args, **kwargs):
		computer_id = kwargs.get('computer_id')
		computer_obj = models.Computer.objects.filter(id=computer_id).values('status')
		if computer_obj[0].get('status') == 3:
			return None
		if self.has_add_btn:
			# 根据别名反向生成URL

			return '<a class="btn btn-success" href="%s">添加</a>' % self.reverse_add_url(*args, **kwargs)
		return None

	def get_queryset(self, request, *args, **kwargs):
		computer_id = kwargs.get('computer_id')
		return self.model_class.objects.filter(computer_id=computer_id)


	def form_database_save(self, request, form, is_update, *args, **kwargs):

		computer_id = kwargs.get("computer_id")
		rental_status = request.POST.get("rental_status")
		print(rental_status,type(rental_status))
		if not is_update:
			form.instance.computer_id = computer_id
		form.save()
		computer_obj = models.Computer.objects.filter(id=computer_id)
		if int(rental_status) == 1:
			computer_obj.update(status=1)
		elif int(rental_status) == 2:
			computer_obj.update(status=2)



