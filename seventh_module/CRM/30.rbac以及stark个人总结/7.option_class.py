class Option(object):
    def __init__(self,field,is_multi=False,db_condition=None,text_func=None,value_func=None):
        """

        :param field: 组合搜索的字段
        :param is_multi: 是否支持多选
        :param db_condition: 数据库关联查询时的条件
        :param text_func: 此函数用于显示组合搜索按钮页面文本
        :param value_func: 此函数用于显示组合搜索按钮值
        """
        self.field = field
        self.is_multi = is_multi
        if not db_condition:
            db_condition = {}
        self.db_condition = db_condition
        self.text_func = text_func
        self.is_choice = False
        self.value_func = value_func


    def get_db_condition(self,request,*args,**kwargs):
        return self.db_condition

    def get_queryset_or_tuple(self,model_class,request,*args,**kwargs):
        """
        根据字段去获取数据库关联的数据
        :return:
        """
        # 根据gender或depart字符串，去自己对应的Model类中找到字段对象，
        field_object = model_class._meta.get_field(self.field)
        verbose_name = field_object.verbose_name

        # 根据对象获取关联数据
        if isinstance(field_object, ForeignKey) or isinstance(field_object, ManyToManyField):
            # FK和M2M，应该获取其关联表中的数据
            # 根据表字段获取其关联表的所有数据 field_object.rel.model.objects.all()
            db_condition = self.get_db_condition(request,*args,**kwargs)

            return  SearchGroupRow(verbose_name,field_object.rel.model.objects.filter(**db_condition),self,request.GET)   # 返回的queryset类型,self 是自身的Option对象

        else:
            # 获取Choice中的数据
            self.is_choice = True
            return SearchGroupRow(verbose_name,field_object.choices,self,request.GET) #返回的元组类型,self 是自身的Option对象

    def get_text(self,field_object):
        if self.text_func:  # 此为扩展此函数的条件，只要为此类实例化时，可以传递一个自定义的text_func 的函数对象
            return self.text_func(field_object)
        if self.is_choice:
            return field_object[1]
        return str(field_object)

    def get_value(self,field_object):
        if self.value_func:  # 此为扩展此函数的条件，只要为此类实例化时，可以传递一个自定义的text_func 的函数对象
            return self.value_func(field_object)
        if self.is_choice:
            return field_object[0]
        return field_object.pk