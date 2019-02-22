# -*- coding: utf-8 -*-

# __title__ = 'consult_record.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.22'

from django.conf.urls import url



from stark.service.v1 import StarkHandler

class ConsultRecordHandler(StarkHandler):
	list_display = ['date','consultant','note']

	def get_urls(self):
		patterns = [
			url(r'^list/(?P<customer_id>\d+)$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
			url(r'^add/$', self.wrapper(self.add_view), name=self.get_add_url_name),
			url(r'^change/(?P<pk>\d+)/$', self.wrapper(self.change_view), name=self.get_change_url_name),
			url(r'^del/(?P<pk>\d+)/$', self.wrapper(self.delete_view), name=self.get_delete_url_name),
		]
		patterns.extend(self.extra_urls())
		return patterns

	def get_queryset(self, request, *args, **kwargs):
		current_user_id = request.session['user_info']['id']
		customer_id = kwargs.get('customer_id')
		return self.model_class.objects.filter(customer_id=customer_id,customer__consultant_id=current_user_id)

