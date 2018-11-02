from django.db import models

# Create your models here.

class UserInfo(models.Model):

	title = models.CharField(verbose_name="标题",max_length=32)

	def __str__(self):
		return self.title


class Depart(models.Model):
	name = models.CharField(verbose_name="部门",max_length=32)
	tel = models.CharField(verbose_name="联系电话",max_length=32)
	user = models.ForeignKey(verbose_name="负责人",to='UserInfo')

	def __str__(self):
		return self.name
