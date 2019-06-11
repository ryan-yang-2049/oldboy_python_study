# -*- coding: utf-8 -*-

from stark.service.v1 import site
from assets import models

from assets.views.computer import ComputerHandler
from assets.views.rental_record import RentalRecordHandler

from assets.views.fix_phone import FixPhoneHandler

# 电脑资产管理
site.registry(models.Computer,ComputerHandler)
# 电脑记录管理
site.registry(models.RentalRecord,RentalRecordHandler)

# 固定电话管理
site.registry(models.FixPhone,FixPhoneHandler)








