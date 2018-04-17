#!/usr/bin/env python
#coding:utf-8
menus = [
    {
        'text': '北京',
        'children': [
            {'text': '朝阳', 'children': []},
            {'text': '昌平', 'children': [
                {'text': '沙河', 'children': []},
                {'text': '回龙观', 'children': []},
            ]},
        ]
    },
    {
        'text': '上海',
        'children': [
            {'text': '宝山', 'children': []},
            {'text': '金山', 'children': []},
        ]
    }
]
#深度查询
#1. 打印所有的节点
#2. 输入一个节点名字，沙河， 你要遍历找，找到了，就打印它，并返回true,

# def info(address):
#     global menus
#     for key in menus:
#         if len(key) < 0:
#             break
#         elif key['text'] != address:
#             print("text:",key['text'],"children:",key['children'])
#             menus = key['children']
#             info(address)
#         elif key['text'] == address:
#
#             return 'aa'



def info(menus,address):
    for key in menus:
        if key['text'] == address:
            return True
        else:
            menus = key['children']
            info(menus,address)
            return menus


res = info(menus,'guizhou')
# print(res)
if res:
    print('找到了')
else:
    print("没找到")



















