#coding:utf-8

# import sys,os
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
#
#
# from core import withdraw
#
#
# withdraw.SayHi()

import logging
from logging import handlers
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = BASE_DIR+'/'+'logs'
info = 'luffy'

log_level = 40
logger = logging.getLogger("abc")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(log_level)

fh = handlers.TimedRotatingFileHandler("%s/%s.log" % (log_dir, info), when='S', interval=10, backupCount=3)
fh.setLevel(log_level)

logger.addHandler(fh)
logger.addHandler(ch)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(message)s')

fh.setFormatter(file_formatter)
ch.setFormatter(file_formatter)

logger.error("test")