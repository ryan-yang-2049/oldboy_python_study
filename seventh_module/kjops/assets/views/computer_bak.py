# -*- coding: utf-8 -*-
import csv,codecs
import datetime
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
from django.conf import settings

from stark.service.v1 import  StarkHandler,get_choice_text,Option
from assets.models import ASSET_STATUS, ASSET_TYPE_CHOICE, COMPANY_CHOICE, MEMORY_CHOICE

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
		# pk_list = request.POST.getlist('pk')
		# print(pk_list)
		# if not pk_list:
		# 	data = self.model_class.objects.all()
		# else:

		data = self.model_class.objects.all()
		response = HttpResponse(content_type='text/csv')
		response.write(codecs.BOM_UTF8)
		now = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')
		file_name = 'assets_computer_'+now+'.csv'
		response['Content-Disposition'] = "attachment; filename=" + file_name
		writer = csv.writer(response)
		writer.writerow([
			'资产编号',
			'设备类型',
			'所属公司',
			'设备状态',
			'设备厂商',
			'价格',
			'购买时间',
			'内存',
			'磁盘',
			'SN号码',
			'备注信息',
		])

		for item in data:
			if item.asset_type:
				asset_type_num = int(item.asset_type)
				asset_type_info = ASSET_TYPE_CHOICE[asset_type_num-1][1]
			else:
				asset_type_info = ""

			if item.company:
				company_num = int(item.company)
				company_info = COMPANY_CHOICE[company_num-1][1]
			else:
				company_info = ""

			if item.status:
				status_num = int(item.status)
				status_info = ASSET_STATUS[status_num-1][1]
			else:
				status_info = ""

			if item.memory:
				memory_num = int(item.memory)
				memory_info = MEMORY_CHOICE[memory_num-1][1]
			else:
				memory_info = ""

			writer.writerow([
				item.asset_no,
				asset_type_info,
				company_info,
				status_info,
				item.vendor,
				item.price,
				item.buy_time,
				memory_info,
				item.disk,
				item.sn,
				item.memo,
			])
		return response


	def import_excel_data(self,request,*args,**kwargs):
		if request.method == "POST":
			from assets import models
			asset_file = request.FILES.get("asset_import")
			filename = settings.UPLOAD_FILE_DIR + "asset.csv"
			with open(filename,'wb+') as f:
				for chunk in asset_file.chunks(chunk_size=1024):
					f.write(chunk)
			try:
				with open(filename,'r') as f:
					title = next(csv.reader(f))
					count = 0
					try:
						for data in csv.reader(f):
							computer = models.Computer.objects.filter(asset_no=data[0]).first()

							# 获取设备类型的对应的Choice的数字
							asset_type = data[1]
							for computer_type in ASSET_TYPE_CHOICE:
								if computer_type[1] == asset_type:
									asset_type = computer_type[0]

							company_info = data[2]
							for company in COMPANY_CHOICE:
								if company[1] == company_info:
									company_info = company[0]

							computer_status = data[3]
							for status in ASSET_STATUS:
								if status[1] == computer_status:
									computer_status = status[0]

							memory_num = data[7]
							for memory in MEMORY_CHOICE:
								if memory[1] == memory_num:
									memory_num = memory[0]
							if  computer:
								models.Computer.objects.filter(asset_no=data[0]).update(
									asset_type=asset_type,
									company=company_info,
									status=computer_status,
									vendor=data[4],
									price=data[5],
									buy_time=data[6],
									memory=memory_num,
									disk=data[8],
									sn=data[9],
									memo=data[10]
								)
							else:

								computer_obj = models.Computer(
									asset_no=data[0],
									asset_type=data[1],
									company=company_info,
									status=computer_status,
									vendor=data[4],
									price=data[5],
									buy_time=data[6],
									memory=memory_num,
									disk=data[8],
									sn=data[9],
									memo=data[10]
								)
								computer_obj.save()
					except Exception as msg:
						print(msg)




			except Exception as e:
				print(e)
				print("import asset csv file error!")
				status = 2

			status = 1
		return render(request,'assets/import.html')
