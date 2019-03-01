# -*- coding: utf-8 -*-

# __title__ = 'local_machine_management.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.03.01'


from stark.service.v1 import StarkHandler,get_choice_text,Option

class MachineHandler(StarkHandler):
	list_display = ['host','intranet','external','specification','system',get_choice_text('状态','status'),'principal',get_choice_text('供应商','supplier'),'remark']


	search_list = ['intranet','supplier']

	search_group = [
		Option(field='status'),
		Option(field='supplier'),
	]



