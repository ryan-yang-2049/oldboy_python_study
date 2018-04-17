
import os,sys,time


# for i in range(101):
#    #显示进度条百分比  #号从1开始 空格从99递减
#    hashes = '#' * int(i / 100.0 * 100)
#    spaces = ' ' * (100 - len(hashes))
#    sys.stdout.write("\r[%s] %s%%" % (hashes + spaces, i))
#    sys.stdout.flush()
#    time.sleep(0.5)



# #
# for i in range(total_size):
#    line = 100
#    recv_size += line
#    # print(i,'==>',recv_size/total_size)
#    hashes = '#' * int(recv_size/total_size)
#    spaces = ' ' * (total_size - len(hashes))
#    sys.stdout.write("\r[%s] %s%%" % (hashes + spaces, recv_size))
#    sys.stdout.flush()
#    time.sleep(0.5)
#
# total_size = 10212
# recv_size = 0
# while recv_size < total_size:
#    line = 1000
#    recv_size += line
#    hashes = '#' * int(1.0 * recv_size / total_size * 100)
#    spaces = ' ' * (100 - len(hashes))
#    # print(spaces)
#    sys.stdout.write("\r[%s] %s%%" % (hashes + spaces, 100))
#    sys.stdout.flush()
#    time.sleep(0.5)

# for i in range(101):
   # #显示进度条百分比  #号从1开始 空格从99递减
   # hashes = '#' * int(i / 100.0 * 100)
   # spaces = ' ' * (100 - len(hashes))
   # sys.stdout.write("\r[%s] %s%%" % (hashes + spaces, i))
   # sys.stdout.flush()
   # time.sleep(0.5)


import json, os


def list_dir(path, res):
	for i in os.listdir(path):
		res['files'].append(i)
		temp_dir = os.path.join(path, i)
		if os.path.isdir(temp_dir):
			temp = {"dirname": temp_dir, 'child_dirs': [], 'files': []}
			res['child_dirs'].append(list_dir(temp_dir, temp))


	return res


def get_config_dirs():
	res = {'dirname': '/user_home', 'child_dirs': [], 'files': []}
	return list_dir(r'/Users/ryan/python/oldboypython/oldboy_python_study/third_module/practice/ftp/server/user_home/ryan', res)





def recursive(dic,li,arg):
	for key in dic.keys():
		if type(dic[key]) == dict:
			for k,v in dic[key].items():
				if k == arg:
					li.append(key)
				else:
					recursive(dic[key],li,arg)

if __name__ == '__main__':
	res = get_config_dirs()
	file_list = []
	dir_list = []

	temp_list = []
	temp_menu = res
	while True:
		for key,val in temp_menu['files']:
			file_list.append(val)


		choice = input("请输入信息，退出（q），返回（b）：").strip()
		if choice in temp_menu:
			temp_list.append(temp_menu)
			temp_menu = temp_menu[choice]
		elif choice == 'q':
			break
		elif choice == 'b':
			if temp_list:
				temp_menu = temp_list.pop()