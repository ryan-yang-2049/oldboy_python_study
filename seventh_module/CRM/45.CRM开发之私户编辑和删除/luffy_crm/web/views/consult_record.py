# -*- coding: utf-8 -*-

# __title__ = 'consult_record.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.22'

from django.conf.urls import url
from django.utils.safestring import mark_safe


from stark.service.v1 import StarkHandler,StarkModelForm
from web import models

class ConsultRecordModelForm(StarkModelForm):
	class Meta:
		model = models.ConsultRecord
		fields = ['note']

class ConsultRecordHandler(StarkHandler):

	# change_list_template = 'consult_record.html'

	def display_edit_del(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return '操作'
		customer_id = kwargs.get('customer_id')
		tpl = '<a href="%s">编辑</a> <a href="%s">删除</a>' % (
			self.reverse_change_url(pk=obj.pk, customer_id=customer_id),
			self.reverse_delete_url(pk=obj.pk, customer_id=customer_id))
		return mark_safe(tpl)


	list_display = ['note','consultant','date']
	model_form_class = ConsultRecordModelForm
	def get_urls(self):
		patterns = [
			url(r'^list/(?P<customer_id>\d+)/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
			url(r'^add/(?P<customer_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
			url(r'^change/(?P<customer_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.change_view), name=self.get_change_url_name),
			url(r'^del/(?P<customer_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.delete_view), name=self.get_delete_url_name),
		]
		patterns.extend(self.extra_urls())
		return patterns

	def get_queryset(self, request, *args, **kwargs):
		current_user_id = request.session['user_info']['id']
		customer_id = kwargs.get('customer_id')
		return self.model_class.objects.filter(customer_id=customer_id,customer__consultant_id=current_user_id)


	def form_database_save(self, request, form, is_update, *args, **kwargs):
		if not is_update:
			current_user_id = request.session['user_info']['id']
			customer_id = kwargs.get('customer_id')
			form.instance.customer_id = customer_id
			form.instance.consultant_id = current_user_id
		form.save()




