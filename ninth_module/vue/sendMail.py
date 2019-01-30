#coding:utf-8

import sys,os,datetime
import logging
import smtplib
from email.mime.text import MIMEText

class SendEmail(object):

	password="Kj@12345"
	email_host="smtp.exmail.qq.com"
	send_user="yunwei@kjdow.com"
	sendstatus = True
	senderr = None
	def send_mail(self,user_list,sub,content):

		message = MIMEText(content,_subtype='plain',_charset='utf-8')
		message['Subject'] = sub
		message['From'] = self.send_user
		message['To'] = ";".join(user_list)
		try:

			server = smtplib.SMTP_SSL(self.email_host,465)
			# server.connect(self.email_host,465)
			server.login(self.send_user,self.password)
			server.sendmail(self.send_user,user_list,message.as_string())
			server.close()
		except Exception as e:
			self.senderr = str(e)
			self.sendstatus = False

	def logwrite(self,mail_to,content):
		# logpath='/var/log/zabbix/alert'
		logpath='./alert'

		if not self.sendstatus:
			content = self.senderr

		if not os.path.isdir(logpath):
			os.makedirs(logpath)

		t = datetime.datetime.now()
		daytime = t.strftime('%Y-%m-%d')
		daylogfile = logpath+'/'+str(daytime)+'.log'
		logging.basicConfig(filename=daylogfile, level=logging.DEBUG)
		os.system('chown zabbix.zabbix {0}'.format(daylogfile))
		logging.info('*' * 130)
		logging.debug(str(t) + ' mail send to {0},content is :\n {1}'.format(mail_to, content))


if __name__ == '__main__':
	send = SendEmail()
	user_list = ['yangyang@kjdow.com',]
	sub = "测试邮件zabbix"
	message = "zabbix test"
	# user_list = [sys.argv[1],]
	# sub = sys.argv[2]
	# message = sys.argv[3]
	send.send_mail(user_list,sub,message)
	send.logwrite(user_list,message)
