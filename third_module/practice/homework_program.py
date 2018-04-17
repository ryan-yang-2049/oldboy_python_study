#coding:utf-8

# '''
# 1. 模拟CS游戏，并定义两个类(人物角色)分为警察和匪徒
#    所有的警察的角色都是police
#    每个警察都有自己独有名字，生命值，武器，性别
#    每个都可以开枪攻击敌人，且攻击目标不能是police
#    所有的匪徒角色都是terrorist
#    每个匪徒都有自己独有名字，生命值，武器，性别
#    每个都可以开枪攻击敌人，切攻击目标不能是terrorist
#    a. 实例化一个警察，一个匪徒，警察攻击匪徒，匪徒掉血
#    b. 为警察和匪徒提供一个属性，来获取他们各自的攻击日志(提示：文本存储；property)
# '''
#
# log = {'police': 'attack terrorist', 'terrorist': 'attack police'}
#
# # attact_log ={}
#
# class People(object):
# 	attack_value = 50
#
# 	def __init__(self,name,sex,life_value,weapon):
# 		self.name = name
# 		self.sex = sex
# 		self.life_value = life_value
#
#
# 	def attack(self,enemy):
# 		if enemy.camp == self.camp:
# 			print("don't attack")
# 		else:
# 			enemy.life_value  -= self.attack_value
# 			log[self.name] = 'attack %s '%enemy.name
#
#
#
#
# 	@property
# 	def attack_log(self):
# 		print(log[self.name])
#
#
# class Police(People):
# 	camp = 'police'
#
#
#
#
# class Terrorist(People):
# 	camp = 'terrorist'
#
#
#
#
# terrorist01 = Terrorist('terr01','male',100,'gun')
# terrorist02 = Terrorist('terr01','male',100,'gun')
# police01 = Police('police01','male',200,'gun')
# police02 = Police('police01','male',100,'gun')
#
# # police01.attack(police02)
# police01.attack(terrorist01)
# police01.attack_log
#
# # print(terrorist01.life_value)
# # # print(police02.life_value)
# #
# terrorist01.attack(police01)
# terrorist01.attack_log
# # print(police02.camp)

'''
2.写一个支持多用户客户端调用服务端的系统命令的程序
'''

import os,socket,subprocess,struct,json

ip_port = ('127.0.0.1',8080)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(ip_port)
server.listen(5)

while True:
	conn,client_addr = server.accept()
	while True:
		cmd = conn.recv(1024)

		if not cmd:continue

		res = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

		stdout = res.stdout.read()
		stderr = res.stderr.read()

		res_dict = {'total_size':len(stdout)+len(stderr)}

		res_json = json.dumps(res_dict)

		res_bytes = res_json.encode('utf-8')

		conn.send(struct.pack('i',len(res_bytes)))

		conn.send(res_bytes)

		conn.send(stdout)
		conn.send(stderr)
	conn.close()
server.close()










