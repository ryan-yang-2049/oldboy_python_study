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
current_user = models.UserInfo.objects.filter(name=user,password=pwd).first()

#获取当前用户所拥有的所有角色
role_list = current_user.roles.all()

#获取当前用户所拥有的所有权限
permissions_list = current_user.roles.filter(permissions__isnull=False).all().values(permissions__url,permissions__url).distinct()

# 问题一：
	1.一个用户是否可以拥有多个角色？是
	2.一个角色是否可以拥有多个权限？是
	所以,获取所有权限的时候要去重(distinct()),否则查询出来的权限就会有重复。
	
# 问题二：
	例如：当wupeiqi用户拥有总监、销售、金牌讲师的角色,且金牌讲师的角色没有任何权限的时候，所获取的权限就会有一个 "金牌讲师"：null 的情况。
	

"""






















