import os,sys
import shelve

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import file_manage

class School(object):

    def __init__(self,school_name,school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.course_name = {}
        self.class_name = {}
        self.teacher_name = {}





