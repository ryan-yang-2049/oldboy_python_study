#coding:utf-8

import logging
from logging import handlers
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = BASE_DIR+'/'+'logs'
'''
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10

'''
# log_level_dict = {"DEBUG":logging.DEBUG,
#                   "INFO":logging.INFO,
#                   "WARN":logging.WARN,
#                   "ERROR":logging.ERROR,
#                   "CRITICAL":logging.CRITICAL,
#                   }
log_level_dict = {"DEBUG":10,
                  "INFO":20,
                  "WARN":30,
                  "ERROR":40,
                  "CRITICAL":50,
                  }

def log_output(name,operate,log_level,message="hehe"):
    log_level = log_level_dict[log_level]
    info = name+'-'+operate
    logger = logging.getLogger(info)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    fh = handlers.TimedRotatingFileHandler("%s/%s.log"%(log_dir,info),when='D',interval=1,backupCount=3)
    fh.setLevel(log_level)

    logger.addHandler(fh)
    logger.addHandler(ch)


    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(message)s')

    fh.setFormatter(file_formatter)
    ch.setFormatter(file_formatter)

    if log_level == 10:
        logger.debug(message)
    elif log_level == 20:
        logger.info(message)
    elif log_level == 30:
        logger.warning(message)
    elif log_level == 40:
        logger.error(message)
    elif log_level == 50:
        logger.critical(message)



if __name__ == '__main__':
    log_output('yang','shopping','INFO',message="hehe02")














