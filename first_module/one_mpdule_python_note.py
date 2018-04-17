
Python 解释器
	Cpython ：官方版本解释器（C语言开发的）
	Ipython ：和Cpython 差不多
	Jpython : Java平台上的解释器
	PyPy    ：Python 写的解释器（采用JIT技术）
	IronPython


Python 安装
   安装python3

   wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
	yum install readline-devel openssl-devel openssl  -y   #防止交互界面的上下左右不可用
	tar xf Python-3.6.3.tgz
	./configure --prefix=/usr/local/python36/
	make && make install
	添加环境变量：
	[root@web-rs01 scripts]# tail -n 1 /etc/profile
	export PATH="/usr/local/python36/bin/:$PATH"
	source /etc/profile
	ln -s /usr/local/python36/bin/python3 /usr/bin/python3
	ln -s /usr/local/python36/bin/pip3 /usr/bin/pip3

	linux 下面tab使用4空格：
		vi /etc/vimrc
		新增一行：set ts=4  


查看帮助
	python -c "help('modules')"

变量
	变量定义规则：
		变量名只能是 字母、数字或下划线的任意组合
		变量名的第一个字符不能是数字
		关键字不能声明为变量
			>>> import keyword
			>>> keyword.kwlist
			['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

 		>>> a,b = (1,2)
		>>> a
		1
		>>> b
		2

	命令习惯
		变量命令：驼峰型，下划线型
		函数命令：全小写，或小写+下划线型
		类命名： 驼峰式，驼峰型+下划线型
		（变量名不易过长，变量名表达明确）

	常量
		常量命令：全部大写（不是必须的）

数据类型
	基本数据类型
		数 字（integer） ：整数（int）、长整型（long）<python3 没有long类型>、浮点型（float）
		字符串（string）： 文本（str）、字节（bytes）
		布 尔（bool）    ： True/False

	数据集
		列表（list）
		元组（tuple）
		字典（dict）：有序字典、无序字典
		集合（set）：有序集合、无序集合



字符串（string）
	字符串格式化： 字符串 %s  整数 %d  浮点 %f  原样打印 %r
	input 默认输出的都是字符串
		#!/usr/bin/env python
		#coding:utf-8
		'''字符串格式化：%s 代表字符串，%d 代表 数字，%f 表示浮点数'''

		name = input("name:")
		age = int(input("age:"))
		job = input("job:")
		hometown = input("hometown:")

		info = """
		-------info of %s -----------
		Name:       %s              
		Age :       %d              
		Job :       %s              
		Hometown:   %s              
		--------end------------------
		""" % (name,name,age,job,hometown)
		print(info)

	基于字典的字符串格式化
	   params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
	   print("%(pwd)s" % params)                                         # 'secret'
	   print("%(pwd)s is not a good password for %(uid)s" % params)      # 'secret is not a good password for sa'
	   print("%(database)s of mind, %(database)s of body" % params)      # 'master of mind, master of body'


运算符
	算数运算符：+ - * / // **
	比较运算符： == !=  > < >= <=    #python3  里面已经取消   <>
	赋值运算符： = += -= *=  /= %= //=
	逻辑运算符：and  not or


流程控制
	if 语句
	    # 布尔值操作符 and or not 实现多重判断
	    a = input(">>:")
	    b = input(">>:")
	    if a == b:
	        print('==')
	    elif a < b:
	        print(b)
	    else:
	        print(a)

	while 语句
	  	例1：
	        while True:
	            if a == b:
	                print("==")
	                break
	            print("!=")
	        else:
	            print('over')

		例2：
			count = 0
			while count <= 10:
			    if count == 5:
			        pass
			    elif 6 <= count <= 8:
			        print(count**2)
			    else:
			        print(count)
			    count += 1

		例3：
			while True:
				print("永远执行")

			while 1:
				print("永远执行")

	break and continue 说明：
		break:用于完全结束一个循环，跳出循环体执行循环后面的语句
		continue：终止本次循环，接着执行后面的循环，break 则完全终止循环



例子：
	#coding:utf-8

	age = 24
	num = 0
	while num < 3:
	    guess_age_number = int(input("please guess age:"))
	    num += 1
	    if num < 3:
	        if guess_age_number != age:
	            print("guess wrong！")
	            continue
	        else:
	            print("guess right")
	            break
	    else:
	        str = input("是否继续玩（Y/y）?：").strip()
	        if str == 'y' or str == 'Y':
	            num = 0
	        else:
	            print("退出程序！")



	else:
	    print("拜拜！")


练习题：
1.简述编译型与解释型语言的区别，且分别列出你知道的那些语言属于编译型，那些属于解释型。
	编译型语言在程序执行之前，有一个单独的编译过程，将程序翻译成机器语言，以后执行这个程序的时候，就不用再进行翻译了。编译可以达到最大的优化；
	解释型语言，是在运行的时候将程序翻译成机器语言，所以运行速度相对于编译型语言要慢。解释可以达到最大的灵活。

	编译型语言： C/C++
	解释型语言：java C# python 

2. 执行python脚本的两种方式是什么？
	环境：linux
	1、 python example.py
	2、 chmod +x example.py && ./example.py

3.python 单行注释和多行注释分别用什么。
	单行注释： #
	多行注释： '''注释'''  

4.布尔值分别有什么
	True / False

5.声明变量注意事项有哪些？
	变量只能是字母、数字、下划线的组合
	变量开头不能用数字
	变量不要使用关键字
	变量命名尽量易识别

6.如何查看变量在内存中的地址？
	a = 1
	id(a)


7.写代码
	(1)实现用户输入用户名和密码，当用户名为 seven 且密码为123 时，显示登录成功，否则登录失败！
		#coding:utf-8
		username = "seven"
		password = "123"
		login_user = input("login:")
		login_passwd = input("password:")
		if login_user == username and password == login_passwd:
		    print("登录成功")
		else:
		    print("登录失败")

	(2)实现用户输入用户名和密码，当用户名为 seven 且密码为123 时，显示登录成功，否则登录失败，失败时允许用户重复输入三次
		#coding:utf-8
		username = "seven"
		password = "123"
		num = 0
		while num < 3:
		    login_user = input("login:")
		    login_passwd = input("password:")
		    num += 1
		    if login_user == username and password == login_passwd:
		        print("登录成功")
		    else:
		        print("登录失败")
	(3)实现用户输入用户名和密码，当用户名为 seven 或 alex 且密码为123 时，显示登录成功，否则登录失败，失败时允许用户重复输入三次
		#coding:utf-8
		username01 = "seven"
		username02 = "alex"
		password = "123"
		num = 0
		while num < 3:
		    login_user = input("login:").strip()
		    login_passwd = input("password:")
		    num += 1
		    if login_user == username01 or login_user == username02:
		        if password == login_passwd:
		            print("登录成功")
		            break
		        else:
		            print("密码错误")
		    else:
		        print("用户名错误、登录失败")

8.写代码
	(a)使用while循环实现输出 2-3+4-5+6.....+100 的和
		#coding:utf-8
		sum = 0
		n = 1
		while n < 100:
		    n += 1
		    mode = n%2
		    if mode == 0:
		        sum += n
		    else:
		        sum -= n
		else:
		    print("sum:",sum)
	(b)使用while循环实现输出 1,2,3,4,5,67,8,9,11,12
		#coding:utf-8
		n = 0
		while n < 12:
		    n += 1
		    if n == 10:
		        continue
		    else:
		        print(n)

	（d）使用while循环实现输出 1-100内的所有奇数
		#coding:utf-8
		n = 0
		while n < 100:
		    n += 1
		    mode = n%2
		    if mode == 1:
		        print(n)
	
	(e) 使用while循环实现输出1-100内的所有偶数		        
		#coding:utf-8
		n = 0
		while n < 100:
		    n += 1
		    mode = n%2
		    if mode == 0:
		        print(n)

9.现有如下两个变量，请简述 n1 和 n2 是什么关系？
n1 = 123456
n2 = n1

解:
n1,n2 它们都是变量，n1 首先被赋值了一个整数，此刻n1的值在内存中存在了一个内存地址"id(n1)"可以得到n1的值在内存中的地址。当 n2 = n1 时，是n2 的内存指针指向了n1 的值内存地址，因此，此时 n2 = 123456，当n1被重新赋值以后，n1 的内存指针指向了另外的内存地址，但是n2的内存指针在n1被重新赋值时，已经指向了值“123456”，因此，就算n1 的值改变了，n2的内存指针指向的内存地址不变，n2的值也就不变。



作业：
	编写登录接口
	(1)基础需求：
		1.让用户输入用户名和密码
		2.认证成功后显示欢迎信息
		3.输错三次后退出程序

	(2)升级需求：
		1.可以支持多个用户登录（提示，通过列表存多个账户信息）
		2.用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示：需要把用户锁定的状态存到文件里）


	解1：
		#coding:utf-8
		username = 'ryan'
		password = '1234'
		count = 0
		while count < 3:
		    login_name = input("login:").strip()
		    login_passwd = input("passwd:").strip()
		    count += 1
		    if login_name == username and login_passwd == password:
		        print("welcome to python")
		        break
		    else:
		        print("login faild!")

	解2：
		'''
		1.可以支持多个用户登录（提示，通过列表存多个账户信息）
		2.用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示：需要把用户锁定的状态存到文件里）

		待完善内容：
		该程序还可以继续升级优化的，比如，只要登录的用户，然后在文件里面填写登录次数，
		登录失败一次，就在后面数值+1,登录成功则清除后面的数字，如果同一用户三次都未登录
		成功，则lock用户。鉴于时间和课程时间问题，待后续解决该bug，也可以在后面学习了字典以后
		用字典解决该bug更容易。
		'''
		import  os
		def check_user_info(username):
		    temp_user_list = []
		    temp_times_list = []
		    with open('userinfo.json','r') as read_user_info:
		        for line in read_user_info.readlines():
		            if line.startswith(username):      # 也可以用 if len(line.strip()):
		                user = line.split(":")[0]
		                login_times = int(line.split(":")[1])
		                temp_user_list.append(user)
		                temp_times_list.append(login_times)
		    if username in temp_user_list:
		        id_num = temp_user_list.index(username)
		        login_times_total = temp_times_list[id_num]
		        return  login_times_total
		# def modify_user_info(username):
		#     temp_line_list = []
		#     with open('temp_userinfo.json','w') as write_info,open('userinfo.json','r') as read_info:
		#         for line in read_info.readlines():
		#             if line.startswith(username):
		#                 line_content = line.strip()
		#                 line_list = line_content.split(':')
		#                 line_list[1] = str(int(line_list[1]) + 1)
		#                 line_value = ':'.join(line_list)
		#                 temp_line_list.append(line_value)
		#             else:
		#                 temp_line_list.append(line)
		#         values = ''.join(temp_line_list)
		#         write_info.write(values+'\n')
		#     # os.rename('userinfo01.json','userinfo01.json')
		#     os.remove('userinfo.json')
		#     os.rename('temp_userinfo.json','userinfo.json')
		user_list = ['alex','ryan','jams','cherry','curry','b']
		password = '1234'
		count = 0
		Flag = True
		while count < 3:
		    login_user = input("login:").strip()
		    login_passwd = input("password:").strip()
		    count += 1
		    if login_user in user_list and login_passwd == password:
		        res = check_user_info(login_user)
		        if res:
		            if res > 3:
		                print("your user being lock")
		                break
		        else:
		            print("welcome python")
		            break
		    # elif login_user in user_list:
		    #     modify_user_info(login_user)
		    #     print("请输入正确的密码")
		    #     continue
		    else:
		        print("info is wrong!")
		        if count == 3:
		            with open("userinfo.json",'a') as write_info:
		                write_info.write(login_user + ':' + '4'+'\n')
		                break


进制转换
	十进制转二进制
		>>> bin(342)
		'0b101010110'    #不看0b
	10进制转16进制: hex(16)


	8bit = 1bytes = 1B
	1kB = 1024B
	1BB = 1024YB = 1024**2 ZB = 1024**3 EB = 1024**4 PB = 1024**5 TB = 1024**6 TB = 1024**7 GB = 1024**8 MB = 1024**9 KB = 1024**10 B 



列表（list）
	列表是一个数据的集合，集合内可以放任何数据类型，可对集合进行方便的增删改查操作
	列表的功能：
		创建  li = [] or li = list()
		查询	 li.index(value)
		切片  li[0:3],li[-5,-1],li[0:6:2]
		增加  li.append(value),li.insert(index,obj)
		修改  li[2] = 3
		删除  li.pop() ,li.remove(value), del li[3] ,del li[2:5]
		循环	  for 
		排序   li.sort() ,li.reverse()

	列表类型内建函数
	   list.clear()						# 清楚列表
	   list.copy()						# 复制列表   l1 = [1,2] l2=l1.copy()
	  *list.append(obj)                 # 向列表中添加一个对象obj
	  *list.count(obj)                  # 返回一个对象obj在列表中出现的次数
	   list.extend(seq)                 # 把序列seq的内容添加到列表中
	  *list.index(obj,i=0,j=len(list))  # 返回list[k] == obj 的k值,并且k的范围在i<=k<j;否则异常
	  *list.insert(index.obj)           # 在索引量为index的位置插入对象obj
	  *list.pop(index=-1)               # 删除并返回指定位置的对象,默认是最后一个对象
	   list.remove(obj)                 # 从列表中删除对象obj
	   list.reverse()                   # 原地翻转列表
	   list.sort(func=None,key=None,reverse=False)  # 以指定的方式排序列表中成员,如果func和key参数指定,则按照指定的方式比较各个元素,如果reverse标志被置为True,则列表以反序排列




深浅copy
	import copy
	x = copy.copy(y)        # make a shallow copy of y    #浅拷贝：只拷贝顶级的对象，或者说：父级对象
	x = copy.deepcopy(y)    # make a deep copy of y       #深拷贝：拷贝所有对象，顶级对象及其嵌套对象。或者说：父级对象及其子对象



	1.深浅拷贝都是对源对象的复制，占用不同的内存空间
	2.如果源对象只有一级目录，那么源对象做任何改动，都不影响深浅拷贝对象
	3.如果源对象不止一级目录，那么源对象做任何改动，都要影响浅拷贝，但不影响深拷贝。
	4.序列对象的切片是浅拷贝，即只拷贝顶级的对象。




字符串
	特性
		有序
		不可变
	
    字符串类型内建方法
    	string = 'abc'
    	string.capitalize()						      # 字符串首字母大写
    	string.center(width,[fillchar])				  # 字符串居中显示（两边用空格填充）,fillchar 可以用字符填充
    	string.encode(encoding='utf-8')
    	string.casefold()							  # 字符串全小写
        string.expandtabs(tabsize=8)                  # tab符号转为空格 #默认8个空格
        string.format()								  # 字符串格式化 等同于 '%' 
       *string.endswith(obj,beg=0,end=len(staring))   # 检测字符串是否已obj结束,如果是返回True #如果beg或end指定检测范围是否已obj结束
       *string.count(str,beg=0,end=len(string))       # 检测str在string里出现次数  f.count('\n',0,len(f)) 判断文件行数
       *string.find(str,beg=0,end=len(string))        # 检测str是否包含在string中,返回索引
       *string.index(str,beg=0,end=len(string))       # 检测str不在string中,会报异常
        string.isalnum()                              # 如果string至少有一个字符并且所有字符都是字母或数字则返回True
        string.isalpha()                              # 如果string至少有一个字符并且所有字符都是字母则返回True
        string.isnumeric()                            # 如果string只包含数字字符,则返回True
        string.isspace()                              # 如果string包含空格则返回True
        string.isupper()                              # 字符串都是大写返回True
        string.islower()                              # 字符串都是小写返回True
        string.lower()                                # 转换字符串中所有大写为小写
        string.upper()                                # 转换字符串中所有小写为大写
        string.lstrip()                               # 去掉string左边的空格
        string.rstrip()                               # 去掉string字符末尾的空格
       *string.replace(str1,str2,num=string.count(str1))  # 把string中的str1替换成str2,如果num指定,则替换不超过num次
       *string.startswith(obj,beg=0,end=len(string))  # 检测字符串是否以obj开头
        string.zfill(width)                           # 返回字符长度为width的字符,原字符串右对齐,前面填充0
       *string.isdigit()                              # 只包含数字返回True
       *string.split("分隔符")                        # 把string切片成一个列表
       *":".join(string.split())                      # 以:作为分隔符,将所有元素合并为一个新的字符串


元组（tuple）
	特性
		不可变
		元组本身不可变


字典（dict）
	字典是一种key-value 的数据类型
	特性
		key-value 结构
		key必须可 hash、且必须为不可变数据类型、必须唯一
		可存放任意多个值、可修改可以不唯一
		无序
		查找速度快

	字典内建方法
        dict.clear()                            # 删除字典中所有元素
       *dict copy()                             # 返回字典(浅复制)的一个副本
       *dict.fromkeys(seq,val=None)             # 创建并返回一个新字典,以seq中的元素做该字典的键,val做该字典中所有键对的初始值
       *dict.get(key,default=None)              # 对字典dict中的键key,返回它对应的值value,如果字典中不存在此键,则返回default值
       *dict.items()                            # 返回一个包含字典中键、值对元组的列表
       *dict.keys()                             # 返回一个包含字典中键的列表
        dict.pop(key[,default])                 # 和方法get()相似.如果字典中key键存在,删除并返回dict[key]
        dict.setdefault(key,default=None)       # 和set()相似,但如果字典中不存在key键,由dict[key]=default为它赋值
       *dict.update(dict2)                      # 将字典dict2的键值对添加到字典dict
       *dict.values()                           # 返回一个包含字典中所有值得列表
        dict([container])     					# 创建字典的工厂函数。提供容器类(container),就用其中的条目填充字典
        len(mapping)          					# 返回映射的长度(键-值对的个数)
        hash(obj)             					# 返回obj哈希值,判断某个对象是否可做一个字典的键值



前两章总结：从整体结构知识点往下延伸
深浅copy-->变量-->数据类型-->各个数据类型的方法使用
数据类型-->{数字，字符串，列表，元组，字典，集合}-->各自的方法使用
数字，字符串，元组（不可变类型）--> 赋值,比较运算符(<">","<","=","!=",is,not,or,and,+=,-=,==,>）
列表，字典（可变类型）--> 增删改查，
编码-->encode('utf-8'),decode('utf-8')

路飞学城面试题（第一模块）
一. 口述题
  开始前请自我介绍（包括为什么来路飞学习Python，和学习后的目标）
  1. 分别解释"=","==","+="的含义
  2. 解释'and','or','not'
  3. "is"和"=="的区别
  4. 数据类型的可变与不可变分别有哪些？

二. 编程题
  1. 求100以内不能被3整除的所有数，并把这些数字放在列表sum=[]里，并求出这些数字的总和和平均数。





























