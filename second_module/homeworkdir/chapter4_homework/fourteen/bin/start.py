#coding:utf-8
import os
import io
import json

import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import withdraw

def operate_json_file(filename,mode,data=None):
    json_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + 'account'

    if mode == 'write':
        write_file = io.open("%s/%s.json"%(json_file_dir,filename),'w',encoding='utf-8')
        json.dump(data,write_file)
        write_file.close()
        return "写入成功"
    elif mode == 'read':
        read_file = io.open("%s/%s.json" % (json_file_dir, filename), 'r', encoding='utf-8')
        return_data = json.load(read_file)
        read_file.close()
        return return_data




# user_dict = {'name':'luffy','expire_date': '2021-01-01', 'id': 1234, 'status': 0,'accounts':1000000, 'pay_day': 22, 'password': '900150983cd24fb0d6963f7d28e17f72'}
# user02_dict = {'name':'tesla','expire_date': '2021-01-01', 'id': 1234, 'status': 0,'accounts':2000000, 'pay_day': 22, 'password': '900150983cd24fb0d6963f7d28e17f72'}
if __name__ == '__main__':
    name = input('name:')
    print('''
    ------- Luffy Bank ---------
    1.账户信息
    2.转账
    3.提现
    
    ''')

    json_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'+'account'

    user_info_dict = operate_json_file(json_file_dir,name,'read')

    choice = input("choice:").strip()
    if choice.isdigit() and int(choice) > 0 and int(choice) <4:
            if int(choice) == 1:

                print("余额：",user_info_dict['accounts'])
                print("信用额度:",user_info_dict['quota'])

            elif int(choice) == 2:
                while True:
                    recv_name = input("收款人：").strip()
                    transfer_amount = input("请输入转账金额：").strip()
                    last_amount = user_info_dict['accounts']
                    if int(transfer_amount) > int(last_amount):
                        print("余额不足！")
                    else:
                        last_amount = last_amount - int(transfer_amount) * 0.05 - int(transfer_amount)
                        print("余额为：",last_amount)
                        user_info_dict['accounts'] = last_amount
                        reduce_user_file = operate_json_file(json_file_dir,name,'write',data=user_info_dict)

                        increase_money_user_dict = operate_json_file(json_file_dir,recv_name,'read')
                        increase_money_user_dict['accounts'] += int(transfer_amount)
                        increase_money_user_file = operate_json_file(json_file_dir,recv_name,'write',increase_money_user_dict)
                        break
            elif int(choice) == 3:
                print("3")
                print(withdraw.withdraw(name))











