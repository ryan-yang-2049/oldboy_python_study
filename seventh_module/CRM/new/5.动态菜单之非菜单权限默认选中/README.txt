点击非权限菜单 视频：16-17

a.数据库的设计（数据库表内关联）
		# 存权限和二级菜单
		class Permission(models.Model):
		   """
		   权限表
		   """
		   title = models.CharField(verbose_name='标题', max_length=32)
		   url = models.CharField(verbose_name='含正则的URL', max_length=128)
		   menu = models.ForeignKey(verbose_name='所属菜单',to='Menu',null=True,blank=True,help_text='null表示不是菜单;非Null表示二级菜单')
		   pid = models.ForeignKey(verbose_name='关联权限',to='Permission',null=True,blank=True,related_name='parents',help_text='对于非菜单权限需要选择一个可以成为菜单权的权限,用于做默认展开和选中菜单')
		   def __str__(self):
			  return self.title

b.思路
	-- 登录，做权限和菜单的初始化
		- 获取菜单信息
			#菜单信息字典格式
			{
				1:{
					title:'信息管理',
					icon : 'x1',
					children:[
						{'id':1,'title':'客户列表','url':'/customer/list/'}, #可以做菜单的权限ID
					]
				},
				2:{
					title:'用户管理',
					icon : 'x1',
					children:[
						{'id':2,'title':'账单列表','url':'/payment/list'},
					]
				},
			}

		- 获取权限信息
				# 权限信息应修改数据格式列表如下
				[
					{'id':1,'url':'/customer/list/','pid':'null'}	# 客户列表,可做菜单的权限
					{'id':2,'url':'/customer/add/','pid':'1'}		# 添加客户,不可做菜单，默认选中id等于1的菜单
					{'id':3,'url':'/customer/del/(?P<cid>\d+)/','pid':'1'}	# 删除客户,不可做菜单，默认选中id等于1的菜单
				]

	-- 用户再次访问URL
		- 中间件进行权限的校验（根据权限信息）
			获取ID或者PID（应该被选中的可以做菜单的权限ID）

	-- 模板中使用inclusion_tag 生成动态菜单(根据菜单信息动态生成)

