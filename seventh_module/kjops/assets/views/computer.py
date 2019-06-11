# -*- coding: utf-8 -*-
import csv,codecs
import datetime
import xlrd,xlwt
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
from django.conf import settings

from stark.service.v1 import  StarkHandler,get_choice_text,Option
from assets.models import ASSET_STATUS, ASSET_TYPE_CHOICE, COMPANY_CHOICE, MEMORY_CHOICE
from assets import models
class ComputerHandler(StarkHandler):

	change_list_template = 'assets/computer_list.html'
	def display_rental_record(self, obj=None, is_header=None, *args, **kwargs):
		if is_header:
			return "租赁详情"
		rental_record_url = reverse('stark:assets_rentalrecord_list',kwargs={'computer_id':obj.pk})
		return mark_safe('<a class="btn btn-small btn-info"  target="_blank" href="%s">租赁详情</a>'%rental_record_url )

	list_display = [
		StarkHandler.display_checkbox,
		'asset_no',
		get_choice_text('设备类型','asset_type'),
		get_choice_text('所属公司','company'),
		get_choice_text('设备状态','status'),
		get_choice_text('内存','memory'),
		'sn',
		display_rental_record
	]

	def extra_urls(self):
		patterns =[
			url(r'^export_excel/$',self.wrapper(self.export_excel_data),name=self.get_url_name('export_excel')),
			url(r'^import_excel/$',self.wrapper(self.import_excel_data),name=self.get_url_name('import_excel')),
		]
		return patterns


	search_list = ['memory__contains','asset_no__contains']
	search_group = [
		Option('company'),
		Option('status'),
		Option('asset_type'),
		Option('memory',),
	]
	def export_excel_data(self,request,*args,**kwargs):
		"""
		导出数据
		:param request:
		:param args:
		:param kwargs:
		:return:
		"""
		# 设置HTTPResponse 的类型
		response = HttpResponse(content_type='application/vnd.ms-excel')
		response['Content-Disposition'] = 'attachment;filename=asset_tpl.xls'
		# 创建一个文件对象
		wb = xlwt.Workbook(encoding='utf-8')
		# 创建一个sheet对象
		sheet = wb.add_sheet('computer-sheet')

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
		# fmts = [
		# 	'M/D/YY',
		# 	'D-MMM-YY',
		# 	'D-MMM',
		# 	'MMM-YY',
		# 	'h:mm AM/PM',
		# 	'h:mm:ss AM/PM',
		# 	'h:mm',
		# 	'h:mm:ss',
		# 	'M/D/YY h:mm',
		# 	'mm:ss',
		# 	'[h]:mm:ss',
		# 	'mm:ss.0',
		# ]
		# style_body.num_format_str = fmts[0]
		# 写入文件标题
		sheet.write(0,0,'资产编号',style_heading)
		sheet.write(0,1,'设备类型',style_heading)
		sheet.write(0,2,'所属公司',style_heading)
		sheet.write(0,3,'设备状态',style_heading)
		sheet.write(0,4,'设备厂商',style_heading)
		sheet.write(0,5,'价格',style_heading)
		sheet.write(0,6,'购买时间',style_heading)
		sheet.write(0,7,'内存',style_heading)
		sheet.write(0,8,'磁盘',style_heading)
		sheet.write(0,9,'SN号码',style_heading)
		sheet.write(0,10,'备注信息',style_heading)

		# 写入数据
		data_row = 1
		from io import BytesIO

		for data in  models.Computer.objects.all():
			# buy_time = i.buy_time.strftime('%Y-%m-%d')

			if data.asset_type:
				asset_type_num = int(data.asset_type)
				asset_type_info = ASSET_TYPE_CHOICE[asset_type_num - 1][1]
			else:
				asset_type_info = ""

			if data.company:
				company_num = int(data.company)
				company_info = COMPANY_CHOICE[company_num - 1][1]
			else:
				company_info = ""

			if data.status:
				status_num = int(data.status)
				status_info = ASSET_STATUS[status_num - 1][1]
			else:
				status_info = ""

			if data.memory:
				memory_num = int(data.memory)
				memory_info = MEMORY_CHOICE[memory_num - 1][1]
			else:
				memory_info = ""

			sheet.write(data_row,0,data.asset_no,style_body)
			sheet.write(data_row,1,asset_type_info,style_body)
			sheet.write(data_row,2,company_info,style_body)
			sheet.write(data_row,3,status_info,style_body)
			sheet.write(data_row,4,data.vendor,style_body)
			sheet.write(data_row,5,data.price,style_body)
			sheet.write(data_row,6,data.buy_time,style_body)
			sheet.write(data_row,7,memory_info,style_body)
			sheet.write(data_row,8,data.disk,style_body)
			sheet.write(data_row,9,data.sn,style_body)
			sheet.write(data_row,10,data.memo,style_body)
			data_row += 1
		output = BytesIO()
		wb.save(output)
		output.seek(0)
		response.write(output.getvalue())
		return response

	def import_excel_data(self,request,*args,**kwargs):
		if request.method == "GET":
			return render(request,'assets/import.html')

		context = {'status':True,'msg':'导入成功','exist_computer':[]}
		try:
			computer_excel = request.FILES.get('asset_import')
			workbook = xlrd.open_workbook(file_contents=computer_excel.file.read())
			sheet = workbook.sheet_by_index(0)
			row_map = {
				0:{'text':'资产编号','name':'asset_no'},
				1:{'text':'设备类型','name':'asset_type'},
				2:{'text':'所属公司','name':'company'},
				3:{'text':'设备状态','name':'status'},
				4:{'text':'设备厂商','name':'vendor'},
				5:{'text':'价格','name':'price'},
				6:{'text':'购买时间','name':'buy_time'},
				7:{'text':'内存','name':'memory'},
				8:{'text':'磁盘','name':'disk'},
				9:{'text':'SN号码','name':'sn'},
				10:{'text':'备注信息','name':'memo'},
			}

			object_list = []

			for row_num in range(1,sheet.nrows):
				row = sheet.row(row_num)
				row_dict = {}

				for col_num,name_text in row_map.items():
					if name_text['name'] == 'asset_no':
						asset_no = row[col_num].value
						computer_exist = models.Computer.objects.filter(asset_no=asset_no).exists
						if computer_exist:
							context['exist_computer'].append(asset_no)
					if name_text['name'] == 'asset_type':
						asset_type = row[col_num].value
						for item in ASSET_TYPE_CHOICE:
							if item[1] == asset_type:
								asset_type_value = item[0]
								row_dict['asset_type'] = int(asset_type_value)
					elif name_text['name'] == 'company':
						company = row[col_num].value
						for item in COMPANY_CHOICE:
							if item[1] == company:
								company_value = item[0]
								row_dict['company'] = int(company_value)
					elif name_text['name'] ==  'status':
						status = row[col_num].value
						for item in ASSET_STATUS:
							if item[1] == status:
								status_value = item[0]
								row_dict['status'] = int(status_value)
					elif name_text['name'] == 'memory':
						memory = row[col_num].value
						for item in MEMORY_CHOICE:
							if item[1] == memory:
								memory_value = item[0]
								row_dict['memory'] = int(memory_value)
					else:
						row_dict[name_text['name']] = row[col_num].value
				object_list.append(models.Computer(**row_dict))
			models.Computer.objects.bulk_create(object_list,batch_size=20)

		except Exception as  e:
			print(e)
			context['status'] = False
			context['msg'] = '导入失败'


		return render(request, 'assets/import.html', context)