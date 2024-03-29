# -*- coding: utf-8 -*-

# __title__ = 'course_record.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.27'
from django.shortcuts import HttpResponse,render
from django.conf.urls import url
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.forms.models import modelformset_factory


from stark.service.v1 import StarkHandler, StarkModelForm, get_datetime_text
from web import models


class CourseRecordModelForm(StarkModelForm):
	class Meta:
		model = models.CourseRecord
		fields = ['day_num', 'teacher']

class StudyRecordModelForm(StarkModelForm):
	class Meta:
		model = models.StudyRecord
		fields = ['record',]



class CourseRecordHandler(StarkHandler):
	def display_attendance(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return '考勤'
		# 获取别名
		name = "%s:%s" % (self.site.namespace, self.get_url_name('attendance'))
		attendance_url = reverse(name, kwargs={'course_record_id': obj.pk})
		tpl = '<a target="_blank" href="%s">考勤</a>' % (attendance_url)
		return mark_safe(tpl)

	list_display = [StarkHandler.display_checkbox, 'class_object', 'day_num', 'teacher',
	                get_datetime_text('日期', 'date'), display_attendance]
	model_form_class = CourseRecordModelForm

	def display_edit_del(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return '操作'
		class_id = kwargs.get('class_id')
		tpl = '<a href="%s">编辑</a> <a href="%s">删除</a>' % (
			self.reverse_change_url(pk=obj.pk, class_id=class_id),
			self.reverse_delete_url(pk=obj.pk, class_id=class_id))
		return mark_safe(tpl)

	def get_urls(self):
		patterns = [
			url(r'^list/(?P<class_id>\d+)/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
			url(r'^add/(?P<class_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
			url(r'^change/(?P<class_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.change_view),
			    name=self.get_change_url_name),
			url(r'^delete/(?P<class_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.delete_view),
			    name=self.get_delete_url_name),
			url(r'^attendance/(?P<course_record_id>\d+)/$', self.wrapper(self.attendance_view),
			    name=self.get_url_name('attendance')),
		]
		patterns.extend(self.extra_urls())
		return patterns

	def get_queryset(self, request, *args, **kwargs):

		class_id = kwargs.get("class_id")
		return self.model_class.objects.filter(class_object_id=class_id)

	def form_database_save(self, request, form, is_update, *args, **kwargs):
		if not is_update:
			class_id = kwargs.get('class_id')
			form.instance.class_object_id = class_id
		form.save()

	def action_multi_init(self, request, *args, **kwargs):
		# 拿到上课记录的id
		course_record_id_list = request.POST.getlist('pk')
		# 拿到班级ID
		class_id = kwargs.get('class_id')

		class_object = models.ClassList.objects.filter(id=class_id).first()
		if not class_object:
			return HttpResponse('班级不存在')

		# 班级反向关联学生
		student_object_list = class_object.student_set.all()

		for course_record_id in course_record_id_list:
			# 判断上课记录是否合法(是否存在数据库)
			course_record_object = models.CourseRecord.objects.filter(id=course_record_id,
			                                                          class_object_id=class_id).first()
			if not course_record_object:
				continue

			# 判断此上课记录的考勤记录是否已经存在
			study_record_object = models.StudyRecord.objects.filter(course_record=course_record_object).exists()
			if study_record_object:
				continue
			# 为每个学生在该天创建考勤记录
			study_record_object_list = [models.StudyRecord(student_id=stu.id, course_record_id=course_record_id) for stu
			                            in student_object_list]
			models.StudyRecord.objects.bulk_create(study_record_object_list, batch_size=50)

	action_multi_init.text = '批量初始化考勤'

	action_list = [action_multi_init, ]

	def attendance_view(self, request, course_record_id, *args, **kwargs):
		'''
		考勤记录的批量操作
		:param request:
		:param course_record_id:
		:param args:
		:param kwargs:
		:return:
		'''
		study_record_object_list = models.StudyRecord.objects.filter(course_record_id=course_record_id)
		study_model_formset = modelformset_factory(models.StudyRecord,form=StudyRecordModelForm,extra=0 )


		if request.method == 'POST':
			formset = study_model_formset(queryset=study_record_object_list, data=request.POST)
			if formset.is_valid():
				formset.save()
			return render(request, 'attendance.html', {'formset': formset})

		formset = study_model_formset(queryset=study_record_object_list)

		return render(request,'attendance.html',{'formset':formset})
