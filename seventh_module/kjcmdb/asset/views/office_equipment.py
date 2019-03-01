# -*- coding: utf-8 -*-

# __title__ = 'office_equipment.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.03.01'


from stark.service.v1 import StarkHandler,get_choice_text,Option

class OfficeEquipmentHandler(StarkHandler):
	list_display = [
		'asset_code',
		get_choice_text('状态','status'),
		get_choice_text('设备类型','types'),
		'department',
		'sn',
		'buydate',
		'warrantydate',
		'user',
		'cpu',
		'mem',
		'system',
		'remark'
	]

	search_list = ['types','department','user','system']
	search_group = [
		Option(field='status'),
		Option(field='types'),
		Option(field='department'),
	]







