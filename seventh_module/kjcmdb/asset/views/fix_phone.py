# -*- coding: utf-8 -*-

# __title__ = 'fix_phone.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.03.01'


from stark.service.v1 import StarkHandler,Option

class FixPhoneHandler(StarkHandler):
	list_display = ['user','depart','extension','straight_line']

	search_list = ['user','depart']

	search_group = [
		Option(field='depart'),
	]






