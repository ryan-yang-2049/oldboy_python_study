#主要看多参数的用法。
#!/usr/bin/env python3
#coding:utf-8
def auth(func):
    def user_auth(*arg,**kwargs):
        print('--before--')
        func(*arg,**kwargs)
        print('--after--')
    return user_auth

@auth
def test(*args,**kwargs):
    print('hello--',args,kwargs)


L1 = [1,2,3,4]

info ={
    "name":'root',
    "pwd":'1234'
}


if __name__ == '__main__':

    print('-----List----------')
    test(*L1)
    print('-----Dict----------')
    test(**info)
    print('-----double----------')
    test(*L1,**info)
'''
[root@js-93 wrap]# python3 exam04.py
-----List----------
--before--
hello-- (1, 2, 3, 4) {}
--after--
-----Dict----------
--before--
hello-- () {'name': 'root', 'pwd': '1234'}
--after--
-----double----------
--before--
hello-- (1, 2, 3, 4) {'name': 'root', 'pwd': '1234'}
--after--
'''