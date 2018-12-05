from django.db import models

# Create your models here.


class Menu(models.Model):
	title = models.CharField(verbose_name='菜单名称', max_length=32)
	icon = models.CharField(verbose_name='图标',max_length=32)
	# icon = models.CharField(verbose_name='图标',max_length=32,null=True,blank=True)
	# null = True 表示数据库可以为空，blank=True：表示django admin里面对它操作可以为空

	def __str__(self):
		return self.title


# 存权限和二级菜单
class Permission(models.Model):
	"""
	权限表
	"""
	title = models.CharField(verbose_name='标题', max_length=32)
	url = models.CharField(verbose_name='含正则的URL', max_length=128)
	name = models.CharField(verbose_name='URL别名',max_length=32,unique=True)
	menu = models.ForeignKey(verbose_name='所属菜单',to='Menu',null=True,blank=True,help_text='null表示不是菜单;非Null表示二级菜单')
	pid = models.ForeignKey(verbose_name='关联权限',to='Permission',null=True,blank=True,related_name='parents',help_text='对于非菜单权限需要选择一个可以成为菜单权的权限,用于做默认展开和选中菜单')
	def __str__(self):
		return self.title



