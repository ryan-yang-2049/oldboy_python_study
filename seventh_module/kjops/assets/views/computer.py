# -*- coding: utf-8 -*-
from django.utils.safestring import mark_safe

from stark.service.v1 import  StarkHandler,get_choice_text,get_datetime_text


class ComputerHandler(StarkHandler):

	# list_display = [
	# 	'asset_no',
	# 	get_choice_text('设备类型','asset_type'),
	# 	get_choice_text('所属公司','company'),
	# 	get_choice_text('设备状态','status'),
	# 	'vendor','price',
	# 	get_datetime_text('购买时间','buy_time'),
	# 	'cpu_model','cpu_num','memory','disk','sn','memo'
	# ]
	def display_rental_record(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return "租赁详情"
		return mark_safe('<a class="btn btn-small btn-info" href="%s">租赁详情</a>' )

	list_display = [
		'asset_no',
		get_choice_text('设备类型','asset_type'),
		get_choice_text('所属公司','company'),
		get_choice_text('设备状态','status'),
		'memory',
		display_rental_record
	]






