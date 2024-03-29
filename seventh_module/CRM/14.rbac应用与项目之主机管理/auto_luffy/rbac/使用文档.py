#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
RBAC组件的使用文档

1. 将rbac组件拷贝项目。


2. 将rbac/migrations目录中的数据库迁移记录删除


3. 业务系统中用户表结构的设计

    业务表结构中的用户表需要和rbac中的用户有继承关系，如：

    rbac/models.py
        class UserInfo(models.Model):
            # 用户表
            name = models.CharField(verbose_name='用户名', max_length=32)
            password = models.CharField(verbose_name='密码', max_length=64)
            email = models.CharField(verbose_name='邮箱', max_length=32)
            roles = models.ManyToManyField(verbose_name='拥有的所有角色', to=Role, blank=True) # 严重提醒 Role 不要加引号

            def __str__(self):
                return self.name

            class Meta:
                # django以后再做数据库迁移时，不再为UserInfo类创建相关的表以及表结构了。
                # 此类可以当做"父类"，被其他Model类继承。
                abstract = True

    业务/models.py
        class UserInfo(RbacUserInfo):
            phone = models.CharField(verbose_name='联系方式', max_length=32)
            level_choices = (
                (1, 'T1'),
                (2, 'T2'),
                (3, 'T3'),
            )
            level = models.IntegerField(verbose_name='级别', choices=level_choices)

            depart = models.ForeignKey(verbose_name='部门', to='Department')

4. 讲业务系统中的用户表的路径写到配置文件。

    # 业务中的用户表
    RBAC_USER_MODLE_CLASS = "app01.models.UserInfo"

    用于在rbac分配权限时，读取业务表中的用户信息。


5. 业务逻辑开发
    将所有的路由都设置一个name，如：
            url(r'^login/$', account.login, name='login'),
            url(r'^logout/$', account.logout, name='logout'),

            url(r'^index/$', account.index, name='index'),

            url(r'^user/list/$', user.user_list, name='user_list'),
            url(r'^user/add/$', user.user_add, name='user_add'),
            url(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),
            url(r'^user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),
            url(r'^user/reset/password/(?P<pk>\d+)/$', user.user_reset_pwd, name='user_reset_pwd'),

            url(r'^host/list/$', host.host_list, name='host_list'),
            url(r'^host/add/$', host.host_add, name='host_add'),
            url(r'^host/edit/(?P<pk>\d+)/$', host.host_edit, name='host_edit'),
            url(r'^host/del/(?P<pk>\d+)/$', host.host_del, name='host_del'),
    用于反向生成URL以及粒度控制到按钮级别的权限控制。

6. 权限信息录入
    - 在url中添加rbac的路由分发,注意：必须设置namespace
        urlpatterns = [
            ...
            url(r'^rbac/', include('rbac.urls', namespace='rbac')),

        ]

    - rbac提供的地址进行操作
        - http://127.0.0.1:8000/rbac/menu/list/
        - http://127.0.0.1:8000/rbac/role/list/
        - http://127.0.0.1:8000/rbac/distribute/permissions/

    相关配置：自动发现URL时，排除的URL：

        # 自动化发现路由中URL时，排除的URL
        AUTO_DISCOVER_EXCLUDE = [
            '/admin/.*',
            '/login/',
            '/logout/',
            '/index/',
        ]


7. 编写用户登录的逻辑【进行权限初始化】

    from django.shortcuts import render, redirect
    from app01 import models
    from rbac.service.init_permission import init_permission


    def login(request):
        if request.method == 'GET':
            return render(request, 'login.html')

        user = request.POST.get('username')
        pwd = request.POST.get('password')

        user_object = models.UserInfo.objects.filter(name=user, password=pwd).first()
        if not user_object:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

        # 用户权限信息的初始化
        init_permission(user_object, request)

        return redirect('/index/')


    相关配置: 权限和菜单的session key：

        setting.py
            PERMISSION_SESSION_KEY = "luffy_permission_url_list_key"
            MENU_SESSION_KEY = "luffy_permission_menu_key"

8. 编写一个首页的逻辑

    def index(request):
        return render(request, 'index.html')


    相关配置：需要登录但无需权限的URL

        # 需要登录但无需权限的URL
        NO_PERMISSION_LIST = [
            '/index/',
            '/logout/',
        ]

9. 通过中间件进行权限校验

    # 权限校验
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'rbac.middlewares.rbac.RbacMiddleware',
    ]

    # 白名单，无需登录就可以访问
    VALID_URL_LIST = [
        '/login/',
        '/admin/.*'
    ]


10. 粒度到按钮级别的控制

        {% extends 'layout.html' %}
        {% load rbac %}

        {% block content %}
            <div class="luffy-container">
                <div class="btn-group" style="margin: 5px 0">

                    {% if request|has_permission:'host_add' %}
                        <a class="btn btn-default" href="{% memory_url request 'host_add' %}">
                            <i class="fa fa-plus-square" aria-hidden="true"></i> 添加主机
                        </a>
                    {% endif %}

                </div>
                <table class="table table-bordered table-hover">
                    <thead>
                    <tr>
                        <th>主机名</th>
                        <th>IP</th>
                        <th>部门</th>
                        {% if request|has_permission:'host_edit' or request|has_permission:'host_del' %}
                            <th>操作</th>
                        {% endif %}

                    </tr>
                    </thead>
                    <tbody>
                    {% for row in host_queryset %}
                        <tr>
                            <td>{{ row.hostname }}</td>
                            <td>{{ row.ip }}</td>
                            <td>{{ row.depart.title }}</td>
                            {% if request|has_permission:'host_edit' or request|has_permission:'host_del' %}
                                <td>
                                    {% if request|has_permission:'host_edit' %}
                                        <a style="color: #333333;" href="{% memory_url request 'host_edit' pk=row.id %}">
                                            <i class="fa fa-edit" aria-hidden="true"></i></a>
                                    {% endif %}
                                    {% if request|has_permission:'host_del' %}
                                        <a style="color: #d9534f;" href="{% memory_url request 'host_del' pk=row.id %}"><i
                                                class="fa fa-trash-o"></i></a>
                                    {% endif %}
                                </td>
                            {% endif %}
                        </tr>
                    {% endfor %}
                    </tbody>
                </table>
            </div>

        {% endblock %}




总结，目的是希望在任意系统中应用权限系统。
    - 用户登录 + 用户首页 + 用户注销 业务逻辑
    - 项目业务逻辑开发
        注意：开发时候灵活的去设置layout.html中的两个inclusion_tag
            <div class="pg-body">
                <div class="left-menu">
                    <div class="menu-body">
                        {% multi_menu request %}  # 开发时，去掉；上线时，取回。
                    </div>
                </div>
                <div class="right-body">
                    <div>
                        {% breadcrumb request %} # 开发时，去掉；上线时，取回。
                    </div>
                    {% block content %} {% endblock %}
                </div>
            </div>
    - 权限信息的录入
    - 配置文件
        # 注册APP
        INSTALLED_APPS = [
            ...
            'rbac.apps.RbacConfig'
        ]
        # 应用中间件
        MIDDLEWARE = [
            ...
            'rbac.middlewares.rbac.RbacMiddleware',
        ]

        # 业务中的用户表
        RBAC_USER_MODLE_CLASS = "app01.models.UserInfo"
        # 权限在Session中存储的key
        PERMISSION_SESSION_KEY = "luffy_permission_url_list_key"
        # 菜单在Session中存储的key
        MENU_SESSION_KEY = "luffy_permission_menu_key"

        # 白名单
        VALID_URL_LIST = [
            '/login/',
            '/admin/.*'
        ]

        # 需要登录但无需权限的URL
        NO_PERMISSION_LIST = [
            '/index/',
            '/logout/',
        ]

        # 自动化发现路由中URL时，排除的URL
        AUTO_DISCOVER_EXCLUDE = [
            '/admin/.*',
            '/login/',
            '/logout/',
            '/index/',
        ]

    - 粒度到按钮级别的控制






"""
