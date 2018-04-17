#程序说明：
ATM程序说明：
    bin目录：
        入口文件：atm.py
        管理程序 manage.py
            实现功能有:
                1.对密码进行 hash_md5加密模块
                2.用户注册
                3.修改用户密码

    conf目录：
        所有ATM用户的信息文件

    core目录：
        file_operate.py:操作文件
            功能说明：
                1.读文件
                    方法：operate_user_info_file('ryan','read')
                2.写文件
                    方法：operate_user_info_file('ryan','write',data="yourdata")

        user_auth.py:用户登录的装饰器
            功能说明：实现了返回登录用户的用户名。


        main.py ：主要的逻辑处理
            功能说明：
                1.run函数：入口文件的调用函数。并对想要的功能实现逻辑处理
                2.view_account_info:查看用户信息
                3.with_draw：提现
                4.pay_back：还款（还未做）
                5.transfer：转账


        log_info.py:日志处理
            功能说明：
                可以使用不同level进行调用，待完善。

    logs目录：
        用于存放各种日志文件。



SHOPPING 说明：
    bin目录：
        购物车商城入口程序：shopping.py
        商品管理控制台程序： manage.py
            实现功能有：
                1.添加商品与对应价格
                2.删除商品

    conf 目录：
        所有用户对应的历史购买的商品信息  username.json
        购物用户临时购买信息：也就是，用户上一次在商城购买以后，只要本次不继续购买就可以对上次购买的
        商品进行退货的文件



    shop_core目录：
        商城主逻辑文件：main.py
            实现功能说明：
                1.删除上次或本次购买物品，并退款至ATM。附加说明：如果本次购买以后，上次购买的货物则不能在退货
                2.查看本次（上次）购买物品，查看历史购物物品
                3.购物
                4.run() 主逻辑入口。使用装饰器。

































