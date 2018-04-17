#!/usr/bin/env python
#coding:utf-8
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
#思路，把每一级的key，都作为一个元素存入一个临时列表。把新建的临时字典作为要显示的信息，在不断的循环这个临时列表，这样就避免用多个while循环去循环多层菜单。
temp_list = []
temp_menu = menu
while True:
    for key in temp_menu:
        print(key)
    choice = input("请输入信息，退出（q），返回（b）：").strip()
    if choice in temp_menu:
        temp_list.append(temp_menu)
        temp_menu = temp_menu[choice]
    elif choice == 'q':
        break
    elif choice == 'b':
        if temp_list:
            temp_menu = temp_list.pop()










