from django.db import models


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色
    """
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)

    def __str__(self):
        return self.name

"""
current_user =models.UserInfo.objects.filter(name=user,password=pwd).first()
#获取当前用户所拥有的所有权限
permissions_list = current_user.roles.filter(permissions__isnull=False).values(permissions__id,permissions__url).distinct()

# 问题一：
	1.一个角色是否可以拥有多个角色？是
	2.一个角色是否可以拥有多个权限？是
# 问题二：
	


"""