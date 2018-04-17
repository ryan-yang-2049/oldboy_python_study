
li = ['手机','电脑','鼠标垫','游艇']
choice_li = []
while True:
    for k,v in enumerate(li):
        print(k,v)
    choice = input("请选择商品编号,退出 q：").strip()
    if choice.isdigit():
        choice_li.append(li[int(choice)])
        print(choice_li)
    elif choice == 'q':
        print("退出购物！")
        break
    else:
        print("请选择商品编号")
        continue
print(choice_li)



