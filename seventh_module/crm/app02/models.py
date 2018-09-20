from django.db import models

# Create your models here.

class Role(models.Model):

	title = models.CharField(verbose_name="角色",max_length=32)


	def __str__(self):
		return  self.title