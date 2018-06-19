# -*- coding: utf-8 -*-

# __title__ = 'views.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.06.19'
import pymysql
from urllib.parse import parse_qs

def login(environ):
	with open('templates/login.html','rb') as f:
		data = f.read()
	return data

def index(environ):
	with open('templates/index.html','rb') as f:
		data = f.read()
	return data

def fav(environ):
	with open('templates/favicon.ico','rb') as f:
		data = f.read()
	return data

def timer(environ):
	import datetime
	now = datetime.datetime.now().strftime("%y-%m-%d %X")
	return now.encode('utf8')

def auth(request):

	try:
		request_body_size = int(request.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0

	request_body = request['wsgi.input'].read(request_body_size)
	data = parse_qs(request_body)

	user = data.get(b"user")[0].decode("utf8")
	pwd = data.get(b"pwd")[0].decode("utf8")


	conn = pymysql.connect(host='101.132.161.180', port=3306, user='root', passwd='123456', db='new_web')  # db：库名
	# 创建游标
	cur = conn.cursor()
	SQL = "select * from userinfo WHERE NAME ='%s' AND PASSWORD ='%s'" % (user, pwd)
	cur.execute(SQL)

	if cur.fetchone():

		f = open("templates/index.html", "rb")
		data = f.read()
		data = data.decode("utf8")
		return data.encode("utf8")

	else:
		return b"user or pwd is wrong"

