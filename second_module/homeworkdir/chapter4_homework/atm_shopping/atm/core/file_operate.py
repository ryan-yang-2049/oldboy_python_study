#coding:utf-8

import os
import io
import json
import sys

'''
该脚本用于操作文件，由于很多实现过程都需要使用到文件操作，因此，特别写一个文件操作方法来实现。
该模块使用方法：
operate_user_info_file(filename,mode,dirname=default_path,data=None)
filename:文件名（可以用用户的名称作为文件名）
mode：参数用：read 或者  write
dirname：默认是写到conf目录下，但是，也可以自己自己路径。
data： 是用于写方法时，写入文件的数据。
正确调用方法：
1.读：operate_user_info_file('ryan','read') 或者，自己自己目录读取 operate_user_info_file(filename,mode,dirname=yourdir)
2.写：operate_user_info_file('ryan','write',data="yourdata"),如果要指定路径写，也是和读一样自己指定路径。
'''

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if os.name == 'posix':
    default_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'+'conf'
elif os.name == 'nt':
    default_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\'+'conf'

# print(default_path)

def operate_user_info_file(filename,mode,dirname=default_path,data=None):
    if mode == 'write':
        write_file = io.open("%s/%s.json"%(dirname,filename),'w',encoding='utf-8')
        json.dump(data,write_file)
        write_file.close()
        return True,"写入成功"
    elif mode == 'read':
        filename = "%s/%s.json" % (dirname, filename)
        # print(filename)
        if os.path.isfile(filename) and os.path.exists(filename):
            read_file = io.open(filename, 'r', encoding='utf-8')
            return_data = json.load(read_file)
            read_file.close()
            return return_data
        else:
            return False



if __name__ == '__main__':

    res = operate_user_info_file("ryan2",'read',data='test')
    if res:
        print("文件存在")
    else:
        print("not exists")