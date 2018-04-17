#coding:UTF-8

import logging
from  logging import  handlers

#Filter过滤日志内容，可以有多个。
class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        #如果在message里面包含了 "db backup" 就不返回。
        return  "db backup" not in record.getMessage()

#1.生成logger对象
logger = logging.getLogger("web")
#1.1 设置日志级别，如果不设置，默认的级别是 >= warning
logger.setLevel(logging.DEBUG)
#l.1 把filter对象添加到logger中
logger.addFilter(IgnoreBackupLogFilter())

#2.生成handler对象
#输出到屏幕，并且设置日志级别
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

#输出到文件，并设置日志级别
# fh = logging.FileHandler('web.log')
# fh = handlers.RotatingFileHandler( "web.log",maxBytes=10,backupCount=3)
# fh.setLevel(logging.WARNING)
fh = handlers.TimedRotatingFileHandler( "web.log",when="S",interval=5,backupCount=3)

#2.1 把handler对象绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)


#3.生成formatter对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')

#3.1 把formatter对象绑定到handler对象
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)

#console : INFO
#global : DEBUG  ,global default level : warning
#file :Warning
#全局设置为DEBUG后， console handler 设置为INFO, 如果输出的日志级别是debug, 那就不会在屏幕上打印

#日志格式等级：数字越大，等级越高
'''
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
'''
#代码运行优先级，先查看global的日志等级，在查看局部的等级。


logger.warning("test log debug")
logger.info("test log info")
logger.error(" db backup test log info")



