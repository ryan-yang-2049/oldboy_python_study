class StarkHandler(object):
    list_display = []  # 页面显示列
    per_page_num = 10  # 每页显示格式
    has_add_btn = True  # 是否具有添加按钮

    def __init__(self, site, model_class, prev):
        """

        :param site: 调用此函数的对象自己
        :param model_class: 类似于 models.UserInfo
        :param prev:    URL的前缀，也可以是后缀
        """
        self.site = site
        self.model_class = model_class  # 此时的model_class 是一个对象
        self.prev = prev  # 表示别名
        self.request = None  # 主要用于保存访问对象的request信息

    def action_multi_delete(self, request, *args, **kwargs):
        """
        批量删除(如果想要定制成功后的返回值，那么就为action函数设置返回值即可)
        例如：该函数后面加上   return rediret('https://www.baidu.com')
        :param request:
        :return:
        """
        pk_list = request.POST.getlist('pk')
        self.model_class.objects.filter(id__in=pk_list).delete()
    action_multi_delete.text = '批量删除'

    # 组合搜索
    search_group = []
    def get_search_group(self):
        return self.search_group

    def get_search_group_condition(self, request):
        """
        获取组合搜索的条件
        :param request:
        :return:
        """
        condition = {}
        # ?depart=1&gender=2&page=123&q=999
        for option in self.get_search_group():
            if option.is_multi: # 支持多选的时候
                values_list = request.GET.getlist(option.field)  # tags=[1,2]
                if not values_list:
                    continue
                condition['%s__in' % option.field] = values_list
            else:   # 不支持多选的时候
                value = request.GET.get(option.field)
                if not value:
                    continue
                condition[option.field] = value
        return condition


    def display_checkbox(self, obj=None, is_header=None):
        """
        自定义页面显示CheckBox
        :param obj:
        :param is_header:
        :return:
        """
        if is_header:
            return "选择"
        return mark_safe('<input type="checkbox" name="pk" value="%s"/>' % (obj.pk))

    # 编辑按钮
    def display_edit(self, obj=None, is_header=None):
        """
        自定义页面显示的列（表头和内容）
        :param obj:
        :param is_header:
        :return:
        """
        if is_header:
            return "编辑"
        parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_change_url_name,
                             pk=obj.pk)
        url = parse_url.memory_reverse_url()
        return mark_safe('<a href="%s">编辑</a>' % url)

    # 删除按钮
    def display_del(self, obj=None, is_header=None):
        if is_header:
            return "删除"
        parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_delete_url_name,
                             pk=obj.pk)
        url = parse_url.memory_reverse_url()
        return mark_safe('<a href="%s">删除</a>' % url)

    # 添加按钮的钩子函数
    def get_add_btn(self):
        if self.has_add_btn:
            # 根据别名反向生成URL
            parse_url = ParseUrl(self.request, self.site.namespace, self.get_add_url_name)
            url = parse_url.memory_reverse_url()
            return '<a class="btn btn-primary" href="%s">添加</a>' % (url)
        return None

    model_form_class = None
    def get_model_form_class(self):
        if self.model_form_class:
            return self.model_form_class
        else:
            class DynamicModelForm(StarkModelForm):
                class Meta:
                    model = self.model_class
                    fields = '__all__'

        return DynamicModelForm

    order_list = []
    def get_order_list(self):
        return self.order_list or ['id']  # -id 按照id降序

    search_list = []
    # 模糊搜索
    def get_search_list(self):
        return self.search_list

    action_list = []
    # 批量执行的下拉狂
    def get_action_list(self):
        return self.action_list


    def get_list_display(self):
        """
        获取页面上应该显示的列，预留的自定义扩展，例如：以后根据用户角色的不同展示不同的列
        :return:
        """
        value = []
        value.extend(self.list_display)

        return value

    def changelist_view(self, request, *args, **kwargs):
        """
        列表页面
        :param request:
        :return:
        """
        ################ 1.批量操作(处理Action 下拉框) #############
        action_list = self.get_action_list()
        action_dict = {func.__name__: func.text for func in action_list}  # {'multi_delete':'批量删除','multi_init':'批量初始化'}
        # 并且此时的multi_delete 是一个对象的名称

        if request.method == "POST":
            action_func_name = request.POST.get(
                "action")  # action_func_name,type(action_func_name),bool(action_func_name) = multi_init <class 'str'> True
            if action_func_name and action_func_name in action_dict:
                # <bound method UserInfoHandler.multi_delete of <app01.stark.UserInfoHandler object at ...>>
                action_response = getattr(self, action_func_name)(request, *args, **kwargs)
                if action_response: # 如果调用的批量处理函数有返回值，则执行返回值
                    return action_response
        ################ 2.模糊搜索 #############
        search_list = self.search_list
        """
        1.如果search_list 中没有之,则不显示搜索框
        2.获取用户提交的关键字
        3.构造条件
        """
        search_key_value = request.GET.get('q', None)
        from django.db.models import Q
        # Q　用于构造复杂的ORM查询条件
        conn = Q()
        conn.connector = 'OR'
        if search_key_value:
            for item in search_list:
                conn.children.append((item, search_key_value))

        ################ 3.排序处理 #############
        order_list = self.get_order_list()

        ################ 4.处理分页 #############
        # 数据库里面所有的数据
        # 获取组合搜索条件
        search_group_condition = self.get_search_group_condition(request)
        all_data = self.model_class.objects.filter(conn).filter(**search_group_condition).order_by(*order_list)
        query_params = request.GET.copy()  # copy方法是默认不能修改request.GET里面的参数的
        query_params._mutable = True  # 这样就可以修改request.GET 里面的参数值了

        pager = Pagination(
            current_page=request.GET.get('page'),  # 获取页面返回的获取的页码
            all_count=all_data.count(),  # 数据库里面所有数据的计算
            base_url=request.path_info,  # 访问的基础URL,例如 http://127.0.0.1/abc?name=ryan&age=18 里面的 http://127.0.0.1
            params=query_params,
            # 用户URL里面的参数,例如 http://127.0.0.1/abc?name=ryan&age=18里面的name=ryan&age=18,它是 QueryDict类型
            per_page_num=self.per_page_num  # 这个是每页显示的个数(扩展，可以在网页端输入，然后在传入服务器端)
        )

        # 列表展示页使用分页的设置 （切片的应用）
        data_list = all_data[pager.start:pager.end]

        ################ 5.处理表格 #############
        list_display = self.get_list_display()
        # 5.1 处理表头
        header_list = []
        if list_display:  # 如果有list_display(展示列) 就循环它
            for key_or_func in list_display:
                if isinstance(key_or_func, FunctionType):
                    verbose_name = key_or_func(self, obj=None, is_header=True)
                else:
                    verbose_name = self.model_class._meta.get_field(key_or_func).verbose_name
                header_list.append(verbose_name)
        else:  # 如果没有list_display(展示列)，那么表头就是它的表名
            header_list.append(self.model_class._meta.model_name)

        # 5.2 处理表的内容
        # queryset[对象1，对象2]
        body_list = []
        for row in data_list:
            tr_list = []
            if list_display:
                for key_or_func in list_display:
                    if isinstance(key_or_func, FunctionType):
                        tr_list.append(key_or_func(self, row, is_header=False))
                    else:
                        tr_list.append(getattr(row, key_or_func))
            else:
                tr_list.append(row)
            body_list.append(tr_list)

        ################ 6.添加按钮 #############
        add_btn = self.get_add_btn()

        ################ 7.组合搜索 #############
        search_group_row_list = []
        search_group = self.get_search_group()  # ['gender', 'depart']
        for option_object in search_group:
            row = option_object.get_queryset_or_tuple(self.model_class,request,*args,**kwargs)

            search_group_row_list.append(row)

        print("================",search_group_row_list)

        return render(request, 'stark/changelist.html', locals())

    def form_database_save(self, form, is_update=False):  # 视频中的save
        """
        在使用ModelForm保存数据之前，预留的钩子方法
        :param form:
        :param is_update:
        :return:
        """
        form.save()

    def add_view(self, request, *args, **kwargs):
        """
        添加页面
        :param request:
        :return:
        """
        model_form_class = self.get_model_form_class()
        if request.method == "GET":
            form = model_form_class()
            return render(request, 'stark/change.html', {"form": form})

        form = model_form_class(data=request.POST)
        if form.is_valid():
            self.form_database_save(form, is_update=False)
            # 在数据库中保存成功后,跳转回列表页面（携带原来的参数）
            parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_list_url_name)
            url = parse_url.memory_url()
            return redirect(url)
        return render(request, 'stark/change.html', {"form": form})

    def change_view(self, request, pk, *args, **kwargs):
        """
        编辑页面
        :param request:
        :return:
        """
        # 当前编辑对象
        current_change_object = self.model_class.objects.filter(pk=pk).first()
        if not current_change_object:
            return HttpResponse("需要修改的对象不存在，请重新选择")

        model_form_class = self.get_model_form_class()
        if request.method == "GET":
            form = model_form_class(instance=current_change_object)
            return render(request, 'stark/change.html', {"form": form})

        form = model_form_class(data=request.POST, instance=current_change_object)
        if form.is_valid():
            self.form_database_save(form, is_update=False)
            # 在数据库中保存成功后,跳转回列表页面（携带原来的参数）
            parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_list_url_name)
            url = parse_url.memory_url()
            return redirect(url)
        return render(request, 'stark/change.html', {"form": form})

    def delete_view(self, request, pk, *args, **kwargs):
        """
        删除页面
        :param request:
        :param pk:
        :return:
        """
        parse_url = ParseUrl(request=self.request, namespace=self.site.namespace, name=self.get_list_url_name)
        cancel = parse_url.memory_url()
        if request.method == "GET":
            return render(request, 'stark/delete.html', locals())
        current_delete_object = self.model_class.objects.filter(pk=pk).delete()
        return redirect(cancel)

    def get_url_name(self, param):
        app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name

        if self.prev:
            return '%s_%s_%s_%s' % (app_label, model_name, self.prev, param)
        return '%s_%s_%s' % (app_label, model_name, param)

    @property
    def get_list_url_name(self):
        """
        获取列表页面URL的name
        :return:
        """
        return self.get_url_name('list')

    @property
    def get_add_url_name(self):
        """
        获取添加页面URL的name
        :return:
        """
        return self.get_url_name('add')

    @property
    def get_change_url_name(self):
        """
        获取修改页面URL的name
        :return:
        """
        return self.get_url_name('change')

    @property
    def get_delete_url_name(self):
        """
        获取删除页面URL的name
        :return:
        """
        return self.get_url_name('delete')

    def wrapper(self, func):
        @functools.wraps(func)  # 保留原函数的源信息
        def inner(request, *args, **kwargs):
            self.request = request
            return func(request, *args, **kwargs)
        return inner

    def get_urls(self):
        patterns = [
            url(r'^list/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            url(r'^add/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            url(r'^change/(?P<pk>\d+)/$', self.wrapper(self.change_view), name=self.get_change_url_name),
            url(r'^del/(?P<pk>\d+)/$', self.wrapper(self.delete_view), name=self.get_delete_url_name),
        ]
        patterns.extend(self.extra_urls())
        return patterns

    def extra_urls(self):
        return []