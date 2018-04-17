# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2017.12.25'
"""
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from atm.core.file_operate import operate_user_info_file
from atm.core.user_auth import login_auth
from atm.core.log_info import log_output



if os.name == 'posix':
    conf_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'+'conf'
    user_config_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+ '/'+'atm' + '/'+'conf'
    logs_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'+'logs'
    atm_logs_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'+'atm' + '/'+'logs'

elif os.name == 'nt':
    conf_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\'+'conf'
    log_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\'+'logs'
    user_config_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+ '\\'+'atm' + '\\'+'conf'
    atm_log_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+ '\\'+'atm' + '\\'+'logs'



def delete_commodify(username):
    while True:
        use_temp_shop = operate_user_info_file(username + '_temp_shop', 'read', dirname=conf_dir)
        if len(use_temp_shop) == 0:
            print("最近您没有进行购物,或者您已清空购物车！")
            break

        total_shop = operate_user_info_file(username, 'read', dirname=conf_dir)

        user_atm_info_dict = operate_user_info_file(username, 'read', dirname=user_config_dir)
        total_user_atm_amount = user_atm_info_dict['balance']    ######
        print("商品名称".center(12, '*'), "商品价格".center(8, '*'), "商品个数".center(8, '*'))
        for key, val in use_temp_shop.items():
            print(key.center(14), ':', str(val[0]).center(8), str(val[1]).center(8))

        delete_single = input("请输入您想删除的商品,退出（Q）").strip()
        if delete_single == 'Q':break
        if delete_single not in use_temp_shop:
            print("请输入正确的商品名称")
        total_temp_number = use_temp_shop[delete_single][1]
        delete_number = input("您一共购买的数量为：%s,请输入您要删除的数量:"%total_temp_number).strip()

        if int(delete_number) > total_temp_number:
            print("您输入的数量大于购买的数量，请重新选择需要删除的商品！")
            continue
        else:
            #atm amount
            total_delte_shop_amount = use_temp_shop[delete_single][0] * int(delete_number)
            user_atm_info_dict['balance'] += total_delte_shop_amount
            operate_user_info_file(username, 'write', dirname=user_config_dir,data=user_atm_info_dict)
            print("退货成功，已退还款项 %s"%total_delte_shop_amount)
            #temp number
            total_temp_number -= int(delete_number)
            if total_temp_number == 0 and len(use_temp_shop) == 1:
                use_temp_shop.clear()
                operate_user_info_file(username + '_temp_shop', 'write', dirname=conf_dir,data=use_temp_shop)
            else:
                use_temp_shop[delete_single][1] = total_temp_number
                operate_user_info_file(username + '_temp_shop', 'write', dirname=conf_dir, data=use_temp_shop)

            #total number
            total_shop_num = total_shop[delete_single][1]
            total_shop_num -= int(delete_number)

            if total_shop_num == 0 and len(total_shop) == 1:
                total_shop.clear()
                operate_user_info_file(username, 'write', dirname=conf_dir, data=total_shop)
            else:
                total_shop[delete_single][1] = total_shop_num
                operate_user_info_file(username, 'write', dirname=conf_dir, data=total_shop)
            #shopping logs
            message = "delete commodify:%s,numbers: %s"%(delete_single,delete_number)
            log_output(username, 'shopping', "INFO", message=message)
            #atm logs
            atm_log_message = "delete commodify:%s,balance increase: %s"%(delete_single,total_delte_shop_amount)
            log_output(username, 'atm', "INFO", message=atm_log_message)

def check_temp_shop(username):
    while True:

        print('''
1.查看本次或上一次购买记录
2.查看历史购买记录
3.退出''')
        choice = input("请选择:").strip()
        if choice == '1':
            use_temp_shop = operate_user_info_file(username+'_temp_shop', 'read', dirname=conf_dir)
            print("商品名称".center(12, '*'), "商品价格".center(8, '*'),"商品个数".center(8, '*'))
            for key, val in use_temp_shop.items():
                print(key.center(14), ':', str(val[0]).center(8),str(val[1]).center(8))
        elif choice=='2':
            use_temp_shop = operate_user_info_file(username, 'read', dirname=conf_dir)
            print("商品名称".center(12, '*'), "商品价格".center(8, '*'), "商品个数".center(8, '*'))
            for key, val in use_temp_shop.items():
                print(key.center(14), ':', str(val[0]).center(8), str(val[1]).center(8))
        elif choice == '3':
            break
        else:
            print("请输入正确的选择")




def shopping(username):
    user_shop_dict = {}
    old_user_commodity_dict = operate_user_info_file(username, 'read', dirname=conf_dir)
    if not old_user_commodity_dict:
        old_user_commodity_dict = {}
    print(old_user_commodity_dict)
    commodity_info = operate_user_info_file('commodity_info', 'read', dirname=conf_dir)
    user_atm_info_dict = operate_user_info_file(username, 'read', dirname=user_config_dir)
    balance = user_atm_info_dict['balance']
    while True:
        print("商品名称".center(12, '*'), "商品价格".center(8, '*'))
        for key, val in commodity_info.items():
            print(key.center(14), ':', str(val).center(8))
        choice = input("您购买的商品是,退出（Q）：").strip()
        if choice == 'Q':break
        if choice not in commodity_info:
            print("请填写正确的商品信息：")
            continue
        commodity_price = commodity_info[choice]
        if commodity_price > balance:
            print("您当前余额为 %s,不能购买 %s ;"%(balance,choice))
            continue
        balance -= commodity_price
        if choice not in user_shop_dict:
            user_shop_dict[choice] = [commodity_price,1]
        else:
            user_shop_dict[choice][1] += 1

        if choice not in old_user_commodity_dict:
            old_user_commodity_dict[choice] = [commodity_price,1]
        else:
            old_user_commodity_dict[choice][1] += 1
        user_atm_info_dict['balance'] = balance
        operate_user_info_file(username,'write',dirname=user_config_dir,data=user_atm_info_dict)
        operate_user_info_file(username,'write',dirname=conf_dir,data=old_user_commodity_dict)
        operate_user_info_file(username+'_temp_shop', 'write', dirname=conf_dir, data=user_shop_dict)

        # shopping logs
        message = "buy commodify:%s,cost: %s" % (choice, commodity_price)
        log_output(username, 'shopping', "INFO", message=message)
        # atm logs
        atm_log_message = "buy commodify:%s,cost: %s,balance:%s" % (choice, commodity_price,balance)
        log_output(username, 'atm', "INFO", message=atm_log_message)




@login_auth
def run(username):
    while True:
        shop_operate_dict = {
            '1':['购物',shopping],
            '2':['查看购物车',check_temp_shop],
            '3':['取消购买某商品',delete_commodify],
            '4':['退出',sys.exit]
        }
        print("序号".center(12, '*'), "名称".center(8, '*'))
        for key, val in shop_operate_dict.items():
            print(key.center(12), ':', str(val[0]).center(8))
        choice = input("请选择序号进行操作：").strip()
        if choice in shop_operate_dict:
            shop_operate_dict[choice][1](username)


run()












