视频从 08---> 12


在web中实现用户的登陆逻辑代码和把权限（url）写入session中。然后在从rbac组件中去写中间件来实现对权限的控制。
常用的变量名，或者需要手动修改的变量配置，最好写在settings.py中，以便py文件去调用 （from django.conf import settings）