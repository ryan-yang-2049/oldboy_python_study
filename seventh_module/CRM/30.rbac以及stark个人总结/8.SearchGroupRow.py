class SearchGroupRow(object):
    def __init__(self,title,queryset_or_tuple,option,query_dict):
        """

        :param title: 组合搜索的列名称
        :param queryset_or_tuple: 组合搜索关联获取到的数据
        :param option: 调用此方法实例后自己的对象
        :param query_dict: request.GET 的值
        """
        self.queryset_or_tuple = queryset_or_tuple
        self.title = title
        self.option = option
        self.query_dict = query_dict

    def __iter__(self):
        yield '<div class="whole">%s</div>'%self.title
        yield '<div class="others">'

        total_query_dict = self.query_dict.copy()
        total_query_dict._mutable = True
        origin_value_list = self.query_dict.getlist(self.option.field) # reuqest.GET 的参数列表
        if not  origin_value_list:
            yield "<a class='active' href='?%s'>全部</a>"%total_query_dict.urlencode()
        else:
            total_query_dict.pop(self.option.field)
            yield "<a href='?%s'>全部</a>"%total_query_dict.urlencode()

        for item in self.queryset_or_tuple:
            text = self.option.get_text(item)   # 下面 Option类的 get_text方法
            # 获取组合搜索按钮文本背后的值
            value = str(self.option.get_value(item)) # 数据库里面获取的值 int类型。

            # 获取reuqest.GET ==> QueryDict对象={gender:['1',],depart:['2',]}
            query_dict = self.query_dict.copy() # 拷贝以后以后，修改自己的，不影响 reuqest.GET 原来的值
            query_dict._mutable = True  # reuqest.GET 默认不能修改，这样设置了才可以被修改

            # origin_value_list = query_dict.getlist(self.option.field)

            if not self.option.is_multi:
                query_dict[self.option.field] = value
                if value in origin_value_list:
                    query_dict.pop(self.option.field)
                    yield "<a class='active' href='?%s'>%s</a>" % (query_dict.urlencode(), text)
                else:
                    yield "<a href='?%s'>%s</a>"%(query_dict.urlencode(),text)
            else:
                # {}
                multi_value_list = query_dict.getlist(self.option.field)
                if value in multi_value_list:
                    multi_value_list.remove(value)
                    query_dict.setlist(self.option.field,multi_value_list)
                    yield "<a class='active' href='?%s'>%s</a>" % (query_dict.urlencode(), text)
                else:
                    multi_value_list.append(value)
                    query_dict.setlist(self.option.field, multi_value_list)
                    yield "<a href='?%s'>%s</a>" % (query_dict.urlencode(), text)
        yield '</div>'