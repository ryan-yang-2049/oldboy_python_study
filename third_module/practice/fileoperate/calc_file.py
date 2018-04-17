'''
__title__ =  'calc_file.py'
__author__ = 'ryan'
__mtime__ = '2018/1/17'
'''
import os
import hashlib
def getfilemd5(filename):
	filemd5 = None
	if os.path.isfile(filename):
		f = open(filename,'rb')
		md5_obj = hashlib.md5()
		while True:
			data = f.read(102400)
			if not data:break
			md5_obj.update(data)
		hash_code = md5_obj.hexdigest()
		f.close()
		filemd5 = str(hash_code).lower()
	return filemd5


def file_info(filename):
	file_info_dict = {}
	if os.path.exists(filename) and os.path.isfile(filename):
		file_info_dict['file_md5'] = getfilemd5(filename)
		file_info_dict['file_size'] = os.path.getsize(filename)
		file_info_dict['file_name'] = filename
		return file_info_dict
	else:
		return False

# dirname = '/Users/ryan/python/oldboypython/oldboy_python_study/third_module/practice/fileoperate/'
# file = 'a.txt'
# filename = "%s%s"%(dirname,file)
# print(filename)
# res = file_info(filename)
# size = res['file_size']
# print(size)

print(os.path.abspath('.'))
