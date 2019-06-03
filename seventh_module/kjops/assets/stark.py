# -*- coding: utf-8 -*-

from stark.service.v1 import site
from assets import models

from assets.views.computer import ComputerHandler
from assets.views.rental_record import RentalRecordHandler


site.registry(models.Computer,ComputerHandler)

site.registry(models.RentalRecord,RentalRecordHandler)








