from django.db import models
from accounts.models import Department

# Create your models here.
ASSET_STATUS = (
	(1, "使用中"),
	(2, "未使用"),
	(3, "故障"),
	(4, "其他")
)
ASSET_TYPE_CHOICE = (
		(1, "笔记本"),
		(2, "台式机"),
		(3, "显示器"),
	)
COMPANY_CHOICE = (
	(1, "客佳信息"),
	(2, "达欧百希特"),
	(3, "其他")
)
MEMORY_CHOICE = (
	(1, '2GB'),
	(2, '4GB'),
	(3, '8GB'),
	(4, '16GB'),
	(5, '32GB'),
)
class Computer(models.Model):
	asset_no = models.CharField(verbose_name='资产编号', max_length=50, unique=True)
	asset_type = models.IntegerField(verbose_name="设备类型", choices=ASSET_TYPE_CHOICE, default=1)
	company = models.IntegerField(verbose_name="所属公司", choices=COMPANY_CHOICE, default=1)
	status = models.IntegerField(verbose_name="设备状态", choices=ASSET_STATUS, default=1)
	vendor = models.CharField(verbose_name="设备厂商", max_length=50, null=True, blank=True)
	price = models.CharField(verbose_name="价格",max_length=32,null=True, blank=True)
	buy_time = models.CharField(verbose_name="购买时间",max_length=64,null=True, blank=True)
	memory = models.IntegerField(verbose_name="内存",choices=MEMORY_CHOICE,default=3)
	disk = models.CharField(verbose_name="磁盘", max_length=255, null=True, blank=True)
	sn = models.CharField(verbose_name="SN号码", max_length=128, null=True, blank=True)
	memo = models.TextField(verbose_name="备注信息", max_length=200, null=True, blank=True)

	def __str__(self):
		return self.asset_no


class RentalRecord(models.Model):
	"""
	租赁信息
	"""
	computer = models.ForeignKey(verbose_name="资产编号",to='Computer')
	user = models.CharField(verbose_name="租赁人",max_length=32)
	rental_choice =(
		(1,'借出'),
		(2,'归还'),
	)
	rental_status = models.IntegerField(verbose_name="状态",choices=rental_choice,default=1)
	rental_time = models.DateField(verbose_name="借出/归还时间",auto_now_add=True)
	note = models.TextField(verbose_name="备注",max_length=200,null=True, blank=True)

	def __str__(self):
		return self.computer


class FixPhone(models.Model):
	"""
	固定电话
	"""
	pass






