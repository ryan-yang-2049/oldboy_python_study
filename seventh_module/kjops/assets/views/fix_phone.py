# -*- coding: utf-8 -*-

# __title__ = 'fix_phone.py'
# __author__ = 'Administrator'
# __mtime__ = '2019/6/4'
import xlwt
from django.shortcuts import HttpResponse,render,redirect

from stark.service.v1 import  StarkHandler,get_choice_text,Option
from assets import models
class FixPhoneHandler(StarkHandler):

	list_display = ['phone_num','depart','user']

	order_list = ['phone_num']

	search_list = ['user__contains',]

	search_group = [
		Option('depart'),
	]

	def action_export(self, request, *args, **kwargs):
		"""
		导出电话号码
		:param request:
		:param args:
		:param kwargs:
		:return:
		"""

		# 设置HTTPResponse 的类型
		response = HttpResponse(content_type='application/vnd.ms-excel')
		response['Content-Disposition'] = 'attachment;filename=phone_tpl.xls'
		# 创建一个文件对象
		wb = xlwt.Workbook(encoding='utf-8')
		# 创建一个sheet对象
		sheet = wb.add_sheet('phone-sheet')

		# 设置文件头的样式,这个不是必须的可以根据自己的需求进行更改
		style_heading = xlwt.easyxf("""
			            font:
			                name Arial,
			                colour_index white,
			                bold on,
			                height 0xA0;
			            align:
			                wrap off,
			                vert center,
			                horiz center;
			            pattern:
			                pattern solid,
			                fore-colour 0x19;
			            borders:
			                left THIN,
			                right THIN,
			                top THIN,
			                bottom THIN;
			 """)
		style_green = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x11;")
		style_red = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x0A;")
		style_body = xlwt.easyxf("""
			    font:
			        name Arial,
			        bold off,
			        height 0XA0;
			    align:
			        wrap on,
			        vert center,
			        horiz left;
			    borders:
			        left THIN,
			        right THIN,
			        top THIN,
			        bottom THIN;
			    """)

		sheet.write(0, 0, '电话号码', style_heading)
		sheet.write(0, 1, '使用者部门', style_heading)
		sheet.write(0, 2, '使用者', style_heading)
		sheet.write(0, 3, '备注', style_heading)

		# 写入数据
		data_row = 1
		from io import BytesIO

		for data in models.FixPhone.objects.all():

			sheet.write(data_row, 0, data.phone_num, style_body)
			sheet.write(data_row, 1, data.depart.title, style_body)
			sheet.write(data_row, 2, data.user, style_body)
			sheet.write(data_row, 3, data.note, style_body)

			data_row += 1
		output = BytesIO()
		wb.save(output)
		output.seek(0)
		response.write(output.getvalue())
		return response

	action_export.text = "批量导出电话号码"
	action_list = [action_export,]




