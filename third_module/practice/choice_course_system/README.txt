选课系统用例开发：

角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程 
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校， 
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
6.3 管理视图，创建讲师， 创建班级，创建课程
7. 上面的操作产生的数据都通过pickle序列化保存到文件里



从现实的角度去看：
1.选课系统提供的使用人群分为三类：管理员，教师，学生
2.根据现实的角度去看学校
	2.1 学校的地址（BJ,SH）
	2.2 学校的组成：老师，学生，班级，课程信息
	2.3 从老师的角度去看：课程名称，学生，班级
	2.4 从学生的角度去看：上课的的班级，上课周期，上课课程, 课程的价格，
	2.5 从课程的角度去看：上该门课程的老师，学生，价格，以及班级名称


从程序的框架结构去做程序的逻辑顺序:

1.三个视图
	学员视图，讲师视图，管理视图；三个视图就是三个接口
	这三个视图其实都是用户信息类，因此，可以根据这个去创建用户的role，不同的role 登陆到不同的接口下面去
	学员(student)--> 选择课程，查看课程
	讲师(teacher)--> 查看班级学员列表 
	管理(admin)  --> 创建讲师， 创建班级，创建课程
	

具体实现去看：
	整体的逻辑还是比较混乱。
	那直接理清楚数据类型，也就是，设计出整个程序的数据结构。根据数据结构去建立程序的逻辑关系，自我感觉上实现过程较快。


school_dict = {
    'BJ':{'school_name':'oldboy_bj',
          'course_info':{'python':{'course_price':5000,'course_period':4},'Linux':{'course_price':3000,'course_period':2}},
          'class_info':{'B1':'python','B2':'linux','B3':'python'},
          'teacher_info':{'alex':{'course_name':'python','salary':10000,'class_name':'B1'}},
          'student_info':{'ryan':{'B1':'python'}}
          },


    'SH': {'school_name': 'oldboy_sh',
           'course_info': {'go': {'course_price': 6000, 'course_period': 5}},
           'class_info': {'S1': 'go', 'S2': 'go',},
           'teacher_info': {'egon': {'course_name': 'go', 'salary': 10000, 'class_name':'S1'}},
           'student_info': {'cherry': {'S1':'go'}}
           },

}

user_dict = {
    'admin':{'admin':{'role':'admin','passwd':'1234','login_statsu':0}},
    'teacher':{'alex':{'role':'teacher','passwd':'1234','login_status':0},'egon':{'role':'teacher','passwd':'1234','login_status':0}},
    'student':{'ryan':{'role':'student','passwd':'1234','login_status':0},'cherry':{'role':'student','passwd':'1234','login_status':0}},
}














