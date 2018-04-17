#!/usr/bin/env python
#coding:utf-8
'''
功能要求：
基础要求：
1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
扩展需求：
1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
2、允许查询之前的消费记录

json 文件类型：
{"alex": {"passwd": "1234", "amount": 0, "buy_goods": []}, "ryan": {"passwd": "1345", "amount": 0, "buy_goods": []}, "jams": {"passwd": "1345", "amount":0, "buy_goods": []}, "cherry": {"passwd": "2345", "amount": 0, "buy_goods": []}}

代码优化：可以添加新用户注册，清空历史购物车，注销账户，
'''
import json
goods = [
{"name": "电脑", "price": 9999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]
def shop(username):
    now_shop_list = []
    shop_list = user_info_dict[username]["buy_goods"]
    salary = user_info_dict[username]['amount']
    while True:
        print(" \033[35;1mWelcome to the store \033[0m".center(40, '*'))
        for ind,val in enumerate(goods):
            print("\033[35;1m%s %s %s\033[0m"%(ind,val['name'],val['price']))
        choice_goods = input("请根据编号购买商品，退出商品购买（q）：").strip()
        if choice_goods.isdigit() and 0 <=int(choice_goods)< len(goods):
            choice_goods = int(choice_goods)
            goods_name = goods[choice_goods]['name']
            cost_salary = goods[choice_goods]['price']
            if cost_salary < salary:
                shop_list.append(goods_name)
                now_shop_list.append(goods_name)
                salary -= cost_salary
                print("your always buy %s and your cost %d RMB.left %d RMB" % (goods_name, cost_salary, salary))
            else:
                print("余额不足，剩余金额为:%s RMB" % salary)
                choice_keep = input("你想继续购买别的商品吗？（Y/N）").strip()
                if choice_keep == 'Y':
                    continue
                elif choice_keep == 'N':
                    user_info_dict[username]["buy_goods"] = shop_list
                    user_info_dict[username]['amount'] = salary
                    return now_shop_list
        elif choice_goods == 'q':
            user_info_dict[username]["buy_goods"] = shop_list
            user_info_dict[username]['amount'] = salary
            return now_shop_list
        else:
            print("输入信息有误")
if __name__ == '__main__':
    with open("user_info_shop.txt",'r') as read_info:
        user_info_dict = json.loads(read_info.read())
    Flag = True
    while True:
        if Flag:
            username = input("login：").strip()
            password = input("passwd:").strip()
            if username in user_info_dict and password == user_info_dict[username]['passwd']:
                while True:
                    choice = input("\033[34;1m1.购买商品，2.查看消费记录，3.查看余额，4.充值，5.退出:\033[0m")#abc
                    if choice == '1':
                        now_shop = shop(username)
                        if len(now_shop) > 0:
                            print("\033[31;1m本次购买了： %s\033[0m"%now_shop)
                    elif choice == '2':
                        print("\033[31;1m消费记录： %s\033[0m"%user_info_dict[username]["buy_goods"])
                    elif choice == '3':
                        print("\033[31;1m余额为：%d RMB\033[0m"%(user_info_dict[username]['amount']))
                    elif choice == '4':
                        while True:
                            recharge = input("\033[31;1m充值金额为：\033[0m").strip()
                            if recharge.isdigit() and int(recharge) > 0:
                                get_money = user_info_dict[username]['amount']
                                get_money += int(recharge)
                                user_info_dict[username]['amount'] = get_money
                                print("\033[33;1m充值完成，本次充值 %s RMB，余额 %s RMB！\033[0m"%(recharge,get_money))
                                break
                            else:
                                go_on = input("充值不合法，是否继续充值（Y/N）:")
                                if go_on == 'Y':
                                    continue
                                elif go_on == 'N':
                                    break
                    elif choice == '5':
                        Flag =  False
                        break
            else:
                print("info is wrong")
        else:
            print("\033[31;1mbyebye\033[0m")
            break
    with open("user_info_shop.txt",'w') as write_info:
        data = json.dumps(user_info_dict)
        write_info.write(data)
