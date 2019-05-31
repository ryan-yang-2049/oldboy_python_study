# -*- coding: utf-8 -*-

from stark.service.v1 import site

from assets.views.computer import ComputerHandler
from assets import models

site.registry(models.Computer,ComputerHandler)








