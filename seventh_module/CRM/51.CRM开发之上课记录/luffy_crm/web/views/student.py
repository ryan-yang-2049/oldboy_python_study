# -*- coding: utf-8 -*-

# __title__ = 'student.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.27'

from django.conf.urls import url
from django.utils.safestring import mark_safe
from stark.service.v1 import StarkHandler, get_choice_text, StarkModelForm, get_m2m_text, Option
from django.urls import reverse
from web import models


class StudentModelForm(StarkModelForm):
	class Meta:
		model = models.Student
		fields = ['qq', 'mobile', 'emergency_contract', 'memo']


class StudentHandler(StarkHandler):
	model_form_class = StudentModelForm
	'web_scorerecord_list'

	def display_score(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return '积分管理'
		record_url = reverse('stark:web_scorerecord_list', kwargs={'student_id': obj.pk})
		return mark_safe('<a target="_blank" href="%s">%s</a>'%(record_url,obj.score))


	list_display = ['customer', 'qq', 'mobile', 'emergency_contract', get_m2m_text('已报班级', 'class_list'),display_score,
	                get_choice_text('状态', 'student_status')]

	has_add_btn = False

	def get_list_display(self):
		"""
		获取页面上应该显示的列，预留的自定义扩展，例如：以后根据用户角色的不同展示不同的列
		:return:
		"""
		value = []
		if self.list_display:
			value.extend(self.list_display)
			value.append(type(self).display_edit)

		return value

	def get_urls(self):
		patterns = [
			url(r'^list/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
			# url(r'^add/$', self.wrapper(self.add_view), name=self.get_add_url_name),
			url(r'^change/(?P<pk>\d+)/$', self.wrapper(self.change_view), name=self.get_change_url_name),
			# url(r'^delete/(?P<pk>\d+)/$', self.wrapper(self.delete_view), name=self.get_delete_url_name),
		]
		patterns.extend(self.extra_urls())
		return patterns

	search_list = ['customer__name', 'qq', 'mobile']

	search_group = [
		Option('class_list', text_func=lambda x: '%s-%s' % (x.school.title, str(x))),
		Option('student_status')
	]
