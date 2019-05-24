# -*- coding: utf-8 -*-

# __title__ = 'classs_list.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.02.21'


from stark.service.v1 import StarkHandler, get_datetime_text, get_m2m_text


class ClassListHandler(StarkHandler):

	def display_course(self, obj=None, is_header=None):
		if is_header:
			return '班级'
		return "%s  %s期" % (obj.course.name, obj.semester)

	list_display = [
		'school',
		display_course,
		'price',
		get_datetime_text('开班日期', 'start_date'),
		'class_teacher',
		get_m2m_text('任课老师', 'tech_teachers')
	]
