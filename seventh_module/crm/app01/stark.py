from django.utils.safestring import mark_safe
from django import forms
from stark.service.stark import site,StarkConfig
from app01 import models




class DepartModelForm(forms.ModelForm):
	class Meta:
		model = models.Depart
		fields = "__all__"

	def clean_name(self):

		return self.cleaned_data['name']


class DepartConfig(StarkConfig):
	list_display = [StarkConfig.display_checkbox,'id','name','tel','user',StarkConfig.display_edit_del]   # 表头，自定制
	model_form_class = DepartModelForm
	# def get_add_btn(self):
	# 	pass

class UserInfoConfig(StarkConfig):

	list_display = [StarkConfig.display_checkbox,'id','title',StarkConfig.display_edit]













site.register(models.UserInfo,UserInfoConfig)
site.register(models.Depart,DepartConfig)






