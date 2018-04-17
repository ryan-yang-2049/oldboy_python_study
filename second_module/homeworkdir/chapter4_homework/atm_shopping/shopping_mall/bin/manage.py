#coding:utf-8

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from atm.core.file_operate import operate_user_info_file

'''
商城产品：
    1.添加商品
    2.删除商品
    commodity_dict = {
       '商品名称':'价格'
    }

'''
if os.name == 'posix':
    conf_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'+'conf'
elif os.name == 'nt':
    conf_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\'+'conf'

def add_commodity():
    commodity_info = operate_user_info_file('commodity_info','read',dirname=conf_dir)
    while True:
        print("商品名称".center(12, '*'), "商品价格".center(8, '*'))
        for key, val in commodity_info.items():
            print(key.center(14), ':', str(val).center(8))
        add_info = input("请输入添加的商品名称，退出(Q)：").strip()
        if len(add_info) == 0:continue
        if add_info == 'Q':break
        if add_info in commodity_info:
            print("商品已存在")
            continue
        info_price = input("请输入商品价格:").strip()
        if not info_price.isdigit():continue
        commodity_info[add_info] = int(info_price)
        operate_user_info_file('commodity_info','write',dirname=conf_dir,data=commodity_info)

def del_commodify():
    commodity_info = operate_user_info_file('commodity_info','read',dirname=conf_dir)
    while True:
        print("商品名称".center(12, '*'), "商品价格".center(8, '*'))
        for key, val in commodity_info.items():
            print(key.center(14), ':', str(val).center(8))
        del_info = input("请输入删除的商品名称，退出(Q)：").strip()

        if len(del_info) == 0:continue
        if del_info == 'Q':break
        if del_info not in commodity_info:
            print("商品不存在")
            continue
        del_info_price = commodity_info[del_info]
        commodity_info.pop(del_info)
        operate_user_info_file('commodity_info', 'write', dirname=conf_dir, data=commodity_info)
        print("删除的商品为：%s，价格为：%s"%(del_info,del_info_price))



if __name__ == '__main__':
    modify_info = {'1':["添加商品",add_commodity],
                   '2':["删除商品",del_commodify],
                   '3':["退出",sys.exit]}
    while True:
        for key,val in modify_info.items():
            print(key+':'+val[0])
        choice = input("请选择序号进行修改：").strip()
        if choice in modify_info:
            modify_info[choice][1]()







