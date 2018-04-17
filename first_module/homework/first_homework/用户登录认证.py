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
