# -*- coding: utf-8 -*-

# __title__ = 'fix_phone.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.03.01'

import mimetypes
import xlrd
import os
from django.conf.urls import url
from django.shortcuts import HttpResponse, render
from django.utils.safestring import mark_safe
from django.http import FileResponse


from django.conf import settings
from stark.service.v1 import StarkHandler, Option
from asset import models

class FixPhoneHandler(StarkHandler):
	# has_imoort_excel_btn = True

	list_display = ['user', 'depart', 'extension', 'straight_line']



	def extra_urls(self):
		patterns = [
			url(r'^import/$', self.wrapper(self.batch_import), name=self.get_url_name('batch_import')),
			url(r'^import/tpl/$', self.wrapper(self.import_url), name=self.get_url_name('import_url')),
		]
		return patterns

	def get_import_excel_btn(self, request, *args, **kwargs):

		import_url = self.reverse_commons_url(self.get_url_name('batch_import'))
		return '<a href="%s" class="btn btn-warning" >批量导入</a>' % import_url

	def batch_import(self, request, *args, **kwargs):

		if request.method == "GET":
			import_url = self.reverse_commons_url(self.get_url_name('import_url'))

			return render(request, 'batch_import.html',{'import_url':import_url})

		content = {'status': True, 'msg': '导入成功'}
		try:
			batch_import_excel = request.FILES.get('batch_import_excel')
			print(batch_import_excel)
			workbook = xlrd.open_workbook(file_contents=batch_import_excel.file.read())

			sheet = workbook.sheet_by_index(0)
			row_map = {
				0: {'text': '使用者', 'name': 'user'},
				1: {'text': '所属部门', 'name': 'depart'},
				2: {'text': '分机号', 'name': 'extension'},
				3: {'text': '直线号码', 'name': 'straight_line'},
			}
			object_list = []
			for now_num in range(1,sheet.nrows):
				row = sheet.row(now_num)
				row_dict = {}
				for col_num,name_text in row_map.items():
					row_dict[name_text['name']] = row[col_num].value
				print("====",row_dict)
				object_list.append(models.FixPhone(**row_dict))
			models.FixPhone.objects.bulk_create(object_list,batch_size=20)
		except Exception as e:
			print("---->",e)
			content['status'] = False
			content['msg'] = '导入失败'
		return render(request, 'batch_import.html', content)

	def import_url(self,request,*args,**kwargs):

		tpl_path = os.path.join(settings.BASE_DIR,'asset','files','批量导入固定电话模板.xlsx')
		content_type = mimetypes.guess_type(tpl_path)[0]
		print("content_type===>",content_type)
		response = FileResponse(open(tpl_path,mode='rb'),content_type=content_type)
		response['Content-Disposition'] = "attachment;filename=%s" % 'fixphone_excel_tpl.xlsx'
		return response

	search_list = ['user', 'depart']
	per_page_num = 20
	order_list = ['extension',]