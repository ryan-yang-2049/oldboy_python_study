# -*- coding: utf-8 -*-
"""
__title__ = 'widgets.py'
__author__ = 'yangyang'
__mtime__ = '2019-02-21'
"""

from django import forms

class DateTimePickerInput(forms.TextInput):
	template_name = 'stark/forms/widgets/datetime_picker.html'








