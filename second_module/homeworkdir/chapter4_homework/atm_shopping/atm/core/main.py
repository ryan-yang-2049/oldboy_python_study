#coding:utf-8

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.user_auth import  login_auth
from core.file_operate import operate_user_info_file
from  core.log_info import log_output
#    '''查看账户信息'''
def view_account_info(username):
    single_info = operate_user_info_file(username,'read')
    for key,val in single_info.items():
        if key != 'password' and key != 'status':
            print(key,':',val)
    message = "Check account information"
    log_output(username, 'atm', "INFO", message=message)
    return True



def with_draw(username):
    single_user_info = operate_user_info_file(username,'read')
    while True:
        current_amount = single_user_info['balance']
        float_current_amount = float('%.1f' % current_amount)
        max_withdraw = '%.1f'%(current_amount - current_amount*0.05)
        print("您当前的金额为 %s,最大提现金额为 %s "%(float_current_amount,max_withdraw))
        withdraw_amount = input("您提现的金额为,返回(B)：").strip()
        if withdraw_amount == 'B':return True
        if not withdraw_amount.isdigit():
            print("提现金额必须是整数")
            continue
        withdraw_amount = int(withdraw_amount)
        settlement_amount = withdraw_amount + withdraw_amount*0.05
        float_settlement_amount = float('%.1f' % settlement_amount)
        if float_settlement_amount > float_current_amount:
            choice_input = input("您当前金额已不足，继续(Y),返回(B):").strip()
            if choice_input == 'B':
                return True
            else:
                continue
        else:
            float_current_amount -= float_settlement_amount
            single_user_info['balance'] = float_current_amount
            print("您提现的金额为：",withdraw_amount)
            print("您的余额为：",float_current_amount)
            operate_user_info_file(username,'write',data=single_user_info)
            message = "Your cash withdrawal amount is %s,The balance is %s;"%(withdraw_amount,float_current_amount)
            log_output(username,'atm',"INFO",message=message)

            choice = input("是否继续提现，继续(Y)，退出(B):").strip()
            if choice == 'Y':
                continue
            else:
                return True



def pay_back(username):
    '''还款'''
    flag = True
    while flag:
        single_user_info = operate_user_info_file(username, 'read')
        current_amount = single_user_info['balance']
        total_amount = single_user_info['quota']
        pay_bak_amount = total_amount - current_amount
        pay_bak_amount = float('%.1f'%pay_bak_amount)
        print("您应还金额为：",pay_bak_amount)
        while True:
            actual_pay_bak = input("您还款金额为,退出(B)：").strip()
            if actual_pay_bak == 'B':
                flag = False
                break
            if not actual_pay_bak.isdigit():continue
            if int(actual_pay_bak) > pay_bak_amount:
                print("实际还款金额应小于等于应还款金额")
                break
            current_amount = current_amount + int(actual_pay_bak)
            single_user_info['balance'] = current_amount
            operate_user_info_file(username,'write',data=single_user_info)
            print("余额：",current_amount)
            message = "Your repayment amount is %s,The balance is %s;"%(actual_pay_bak,current_amount)
            log_output(username,'atm',"INFO",message=message)
            choice = input("是否继续还款,继续(Y),返回(B):").strip()
            if choice == 'Y':
                break
            else:
                flag = False
                break

def transfer(username):
    '''转账'''
    flag = True
    while flag:
        single_user_info = operate_user_info_file(username, 'read')
        current_amount = single_user_info['balance']
        print("您最大转账金额为：",current_amount)
        while True:
            recv_username = input("请输入收款方用户名：").strip()
            judge_exist = operate_user_info_file(recv_username,'read')
            if judge_exist:
                actual_tran_amount = input("您转账金额为,退出(B)：").strip()
                if actual_tran_amount == 'B':
                    flag = False
                    break
                if not actual_tran_amount.isdigit():continue
                if int(actual_tran_amount) > current_amount:
                    print("转账金额过大")
                    break
                current_amount -= int(actual_tran_amount)
                single_user_info['balance'] = current_amount
                operate_user_info_file(username,'write',data=single_user_info)
                print("您的余额为",current_amount)

                recv_user_info = operate_user_info_file(recv_username,'read')
                recv_user_info['balance'] += int(actual_tran_amount)
                operate_user_info_file(recv_username,'write',data=recv_user_info)
                #转账方写日志
                message = "your transfer user is %s,the transfer amount is  %s,The balance is %s;" % (recv_username, actual_tran_amount,current_amount)
                log_output(username, 'atm', "INFO", message=message)
                #收账方写日志

                recv_message = "You received %s %s yuan，your banlance is %s" % (username,actual_tran_amount,recv_user_info['balance'])
                log_output(recv_username, 'atm', "INFO", message=recv_message)

                choice = input("是否继续转账，继续(Y),退出(Q):").strip()
                if choice == 'Y':
                    break
                else:
                    operate_user_info_file(username,'write',data=single_user_info)
                    flag = False
                    break

            else:
                choice = input("该用户在本系统不存在，是否继续，继续(Y),退出(Q):")
                if choice == 'Y':
                    break
                else:
                    flag = False
                    break





@login_auth
def run(login_name):
    operate_dict ={'1':['查看账户信息',view_account_info],
                   '2':['取现',with_draw],
                   '3':['还款',pay_back],
                   '4':['转账',transfer],
                   '5':['退出',sys.exit]

    }
    while True:
        print('-----welcome------')
        for key,val in operate_dict.items():
            print(key,val[0])

        choice = input("请输入序列号，进行选择：").strip()
        if choice in operate_dict:
            operate_dict[choice][1](login_name)



if __name__ == '__main__':
    run()













