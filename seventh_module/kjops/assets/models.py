from django.db import models
from accounts.models import Department

# Create your models here.
ASSET_STATUS = (
	(1, u"使用中"),
	(2, u"未使用"),
	(3, u"故障"),
	(4, u"其他")
)



class Computer(models.Model):
	asset_no = models.CharField(verbose_name='资产编号',max_length=50,unique=True)
	asset_type_choice = (
		(1, "笔记本"),
		(2, "台式机"),
		(3, "显示器"),
	)
	asset_type = models.IntegerField(verbose_name="设备类型",choices=asset_type_choice,default=1)
	company_choice = (
		(1,"客佳信息"),
		(2,"达欧百希特"),
		(3,"其他")
	)
	company = models.IntegerField(verbose_name="所属公司",choices=company_choice,default=1)
	status = models.IntegerField(verbose_name="设备状态", choices=ASSET_STATUS,default=1)
	vendor = models.CharField(verbose_name="设备厂商", max_length=50,null=True,  blank=True)
	price = models.IntegerField(verbose_name="价格", blank=True)
	buy_time = models.DateField(verbose_name="购买时间", max_length=50, blank=True)

	memory = models.CharField(verbose_name="内存", max_length=30,null=True,  blank=True)
	disk = models.CharField(verbose_name="磁盘", max_length=255,null=True,  blank=True)
	sn = models.CharField(verbose_name="SN号码", max_length=60,null=True,  blank=True)
	memo = models.TextField(verbose_name="备注信息", max_length=200,null=True, blank=True)
	def __str__(self):
		return self.asset_no











