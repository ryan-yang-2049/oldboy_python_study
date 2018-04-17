# def shopping(username,salary):
#     shop_list = name_info[username]['buy_goods']
#     while True:
#         # salary = input("\033[31;1m请输入您预计消费的金额：\033[0m").strip()
#         print("\033[34;1m Welcome to the store \033[0m".center(40, '*'))
#         for index, val in enumerate(goods):
#             print(index, val['name'], val['price'])
#         choice_goods = input("\033[35;1m请根据编号购买商品，退出（q）：\033[0m")
#         if choice_goods.isdigit() and int(choice_goods) < len(goods):
#             choice_goods = int(choice_goods)
#             goods_name = goods[choice_goods]['name']
#             cost_salary = int(goods[choice_goods]['price'])
#             if cost_salary < salary:
#                 shop_list.append(goods_name)
#                 salary -= cost_salary
#                 print("your always buy \033[31;1m%s\033[0m and your cost  \033[31;1m%s\033[0m RMB.left %d RMB"%(goods_name,cost_salary,salary))
#             else:
#                 print("余额不足！")
#                 choice_keep = input("你想继续购买别的商品吗？（Y/N）").strip()
#                 if choice_keep == 'Y':
#                     continue
#                 elif choice_keep == 'N':
#                     return salary
#         elif choice_goods == 'q':
#             print("剩余金额为:%s" % salary)
#             print("购买的商品有:", shop_list)
#             return salary
#         else:
#             print("输入信息有误！")
#
# def judge_salary(username):
#     salary = name_info[username]['amount']