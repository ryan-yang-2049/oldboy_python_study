#/usr/bin/env python
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

Flag = False

while not Flag:
    for key in menu:
        print(key)
    choice = input("请输入城市名称，退出（q）1：").strip()
    if choice in menu:
        while not Flag:
            for zone in menu[choice]:
                print(zone)
            choice_zone = input("请输入区域名称，退出（q）,退回上级（exit）2：").strip()
            if choice_zone in menu[choice]:
                while not  Flag:
                    for street in menu[choice][choice_zone]:
                        print(street)
                    choice_street = input("请输入街道名称，退出（q）,退回上级（exit）3：").strip()
                    if choice_street in menu[choice][choice_zone]:
                        while not Flag:
                            for company in menu[choice][choice_zone][choice_street]:
                                print(company)
                            res = input("请输入您选择的公司，退出（q）,退回上级（exit）4：").strip()
                            if res in menu[choice][choice_zone][choice_street]:
                                print("您选择的公司名称是",res)
                            elif res == 'q':
                                Flag = True
                            elif res == 'exit':
                                break
                    elif choice_street == 'q':
                        Flag = True
                    elif choice_street == 'exit':
                        break
            elif choice_zone == 'q':
                Flag = True
            elif choice_zone == 'exit':
                break
    elif choice == 'q':
        Flag = True








































