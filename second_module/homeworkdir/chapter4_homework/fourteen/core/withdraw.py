#coding:utf-8

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from bin import start


def withdraw(name):
    json_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + 'account'
    user_info_dict = start.operate_json_file(json_file_dir,name,'read')
    while True:
        withdraw_amount = input("您提现的金额为:").strip()
        if not withdraw_amount.isdigit():continue
        withdraw_amount = int(withdraw_amount)
        last_accounts = user_info_dict['accounts']
        if withdraw_amount > last_accounts:
            print("您提现的金额超过了您的额度！")
        else:
            last_accounts -= withdraw_amount
            user_info_dict['accounts'] = last_accounts
            print("您提现的金额为：",withdraw_amount)
            break
    start.operate_json_file(json_file_dir,name,'write',user_info_dict)
    return  user_info_dict



