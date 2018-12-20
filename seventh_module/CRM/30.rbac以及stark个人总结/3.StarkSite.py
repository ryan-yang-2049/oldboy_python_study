
class StarkSite(object):
    def __init__(self):
        self._registry = []
        self.app_name = 'stark'
        self.namespace = 'stark'

    def registry(self, model_class, handler_calss=None, prev=None):
        """
        用于构建数据结构等
        :param model_class: 是调用此方法的app中的 models中相关的类  例如：models.UserInfo
        :param handler_calss: 处理请求的视图函数所在的类
        :param prev: 生成 url 的前缀
        :return:
        """
        if not handler_calss:
            handler_calss = StarkHandler  # StarkHandler 就是上面创建的类

        self._registry.append(
            {'model_class': model_class, 'handler': handler_calss(self, model_class, prev), 'prev': prev})

    def get_urls(self):
        patterns = []
        for item in self._registry:
            model_class = item['model_class']
            handler = item['handler']  # 此时的handler 其实是一个对象；例如：StarkHandler(models.UserInfo) 对象
            prev = item['prev']
            app_label, model_name = model_class._meta.app_label, model_class._meta.model_name
            # app_label 表示项目下某个应用的名称  ：app01
            # model_name 表示应用的表名称(小写) ：depart
            if prev:  # url中带前缀的
                patterns.append(url(r'%s/%s/%s/' % (app_label, model_name, prev),
                                    (handler.get_urls(), None, None)))  # 第一个None 是namespace,第二个是name
            else:  # url中不带前缀的
                patterns.append(url(r'%s/%s/' % (app_label, model_name), (handler.get_urls(), None, None)))

        return patterns

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.namespace

site = StarkSite()

代码解释：
    1.StarkSite 实现了单例模式。
        if not handler_calss:
            handler_calss = StarkHandler 
        如果表没有写自己的Handler ，那么默认使用StarkHandler
    2._registry 注册构造的数据：
        """
        site._registry = [
            {'prev':None,'model_class': <class 'app01.models.Depart'>, 'handler': DepartHandler(self,models.Depart,prev)对象中有一个model_class=models.Depart},
            {'prev':private,'model_class': <class 'app01.models.UserInfo'>, 'handler': StarkHandler(self,models.UserInfo,prev)对象中有一个model_class=models.UserInfo},    
            {'prev':None,'model_class': <class 'app02.models.Host'>, 'handler': StarkHandler(self,models.Host,prev)对象中有一个model_class=models.Host}
            ]
        """ 
    3.调用此类的方法：
        app01/stark.py
            site.registry(models.UserInfo, UserInfoHandler)
            
    4.get_urls方法的理解：
        1.每一个item 就是 models.UserInfo 的对象
        2.每一个对象都封装在了 _registry 里面 （_registry 表示一个私有的变量，不应再在外部被调用）
        3._registry解释,重点解释，这个是贯穿全部项目的关键
            {'model_class': model_class, 'handler': handler_calss(self, model_class, prev), 'prev': prev})
            model_class ：models.UserInfo 
            handler : 如果对象创建了自己的handler(UserInfoHandler) 就用自己，没有就使用 StarkHandler
            prev ： URL的前缀/后缀，可以根据调用者对象进行代码的改造，也可以不写。

    5.获取表所在的项目名称以及表自己的名称
        项目名称：app_label = model_class._meta.app_label    例如：app01
        表名小写：model_name = model_class._meta.model_name  例如：userinfo

    6.handler.get_urls() 
        这个是 StarkHandler 里面的方法，
        其中：url(r'%s/%s/' % (app_label, model_name), (handler.get_urls(), None, None)) 就是urls分发的本质

    7.@property
        property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
        property 可以封装方法，然后通过 “对象.属性” 访问。












