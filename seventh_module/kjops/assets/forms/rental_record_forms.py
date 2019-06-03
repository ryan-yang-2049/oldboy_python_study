# -*- coding: utf-8 -*-

# __title__ = 'rental_record_forms.py'
# __author__ = 'Administrator'
# __mtime__ = '2019/5/31'

from django import forms
from assets import models
from stark.forms.base import StarkForm,StarkModelForm

class RentalRecordModelForm(StarkModelForm):

	class Meta:
		model = models.RentalRecord
		fields = ['user','rental_status','note']







