#!/usr/bin/env python
#coding:utf-8
'''
2017-10-18 15:56:26,613 - access - ERROR - account [1234] too many login attempts

'''

import logging
from logging import handlers
logger = logging.getLogger("access")

ch = logging.StreamHandler()
fh = logging.FileHandler('access.log')

logger.addHandler(ch)
logger.addHandler(fh)

log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(log_format)
fh.setFormatter(log_format)

logger.error("account [1234] too many login attempts")

















