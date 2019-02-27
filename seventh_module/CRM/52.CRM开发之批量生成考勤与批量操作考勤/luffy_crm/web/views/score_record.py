# -*- coding: utf-8 -*-

# __title__ = 'score_record.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.27'

from django.conf.urls import url
from stark.service.v1 import StarkHandler,StarkModelForm
from web import models


class ScoreRecordModelForm(StarkModelForm):
	class Meta:
		model = models.ScoreRecord
		fields = ['content','score']



class ScoreRecordHandler(StarkHandler):
	list_display = ['student','content','score','user']
	model_form_class = ScoreRecordModelForm
	def get_urls(self):
		patterns = [
			url(r'^list/(?P<student_id>\d+)/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
			url(r'^add/(?P<student_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
		]
		patterns.extend(self.extra_urls())
		return patterns

	def get_queryset(self, request, *args, **kwargs):
		student_id = kwargs.get('student_id')
		return self.model_class.objects.filter(student_id=student_id)

	def get_list_display(self):
		"""
		获取页面上应该显示的列，预留的自定义扩展，例如：以后根据用户角色的不同展示不同的列
		:return:
		"""
		value = []
		if self.list_display:
			value.extend(self.list_display)
		return value


	def form_database_save(self, request, form, is_update, *args, **kwargs):
		student_id = kwargs.get('student_id')
		user_id = request.session['user_info']['id']
		form.instance.student_id = student_id
		form.instance.user_id = user_id
		form.save()

		# 原来的积分

		score = form.instance.score
		if score > 0:
			form.instance.student.score += abs(score)
		else:
			form.instance.student.score -= abs(score)
		form.instance.student.save()
