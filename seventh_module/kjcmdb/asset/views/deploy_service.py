# -*- coding: utf-8 -*-

# __title__ = 'deploy_service.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.03.01'

from stark.service.v1 import StarkHandler,get_choice_text,Option,get_m2m_text

class DeployServiceHandler(StarkHandler):
	list_display = ['name',get_m2m_text('部署地址','deployip'),'deployport',get_choice_text('环境','env')]


	search_list = ['name',]
	search_group = [
		Option(field='env'),
	]






