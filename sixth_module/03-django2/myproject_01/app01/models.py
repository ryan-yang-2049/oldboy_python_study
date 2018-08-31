from django.db import models

# Create your models here.

class Classes(models.Model):
	"""
	班级表
	"""
	name = models.CharField(max_length=32)
	m = models.ManyToManyField("Teachers")


class Teachers(models.Model):
	"""
	老师表
	"""
	name = models.CharField(max_length=32)



class Student(models.Model):
	username = models.CharField(max_length=32)
	age = models.IntegerField()
	gender = models.BooleanField()
	cs = models.ForeignKey("Classes")













