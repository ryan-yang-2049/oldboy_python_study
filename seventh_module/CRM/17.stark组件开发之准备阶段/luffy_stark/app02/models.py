from django.db import models

# Create your models here.

class Host(models.Model):
	"""
	主机表
	"""
	host = models.CharField(verbose_name='主机名',max_length=32)
	ip = models.GenericIPAddressField(verbose_name='IP',protocol='both')    # protocol='both' 表示既支持IPV4 也支持IPV6

