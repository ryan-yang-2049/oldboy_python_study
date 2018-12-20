视频 47--
	
	1.权限分配
		- 展示用户,角色，权限信息




		- 选择用户，角色，页面上的默认选项




		- 角色和权限分配【保存】
		
		
		
all_menu_dict = {
	1: {
		'id': 1,
		'title': '客户管理',
		'children': [
					{
						'id': 1,
						'title': '客户列表',
						'menu_id': 1,
						'children': [
								{
									'id': 2,
									'title': '添加客户',
									'pid_id': 1
								}, 
								{
									'id': 3,
									'title': '删除客户',
									'pid_id': 1
								}, 
								{
									'id': 4,
									'title': '修改客户',
									'pid_id': 1
								}, 
								{
									'id': 5,
									'title': '批量导入客户',
									'pid_id': 1
								}, 
								{
									'id': 6,
									'title': '客户批量导入模板下载',
									'pid_id': 1
								}]
					}]
	},
	2: {
		'id': 2,
		'title': '账单管理',
		'children': [{
			'id': 7,
			'title': '账单列表',
			'menu_id': 2,
			'children': [{
				'id': 8,
				'title': '添加账单',
				'pid_id': 7
			}, {
				'id': 9,
				'title': '删除账单',
				'pid_id': 7
			}, {
				'id': 10,
				'title': '修改订单',
				'pid_id': 7
			}, {
				'id': 16,
				'title': 'oo__xx',
				'pid_id': 7
			}]
		}]
	},
	9: {
		'id': 9,
		'title': '权限管理',
		'children': [{
			'id': 18,
			'title': 'rbac角色列表',
			'menu_id': 9,
			'children': [{
				'id': 19,
				'title': 'rbac添加角色',
				'pid_id': 18
			}, {
				'id': 20,
				'title': 'rbac编辑角色',
				'pid_id': 18
			}, {
				'id': 21,
				'title': 'rbac删除角色',
				'pid_id': 18
			}]
		}, {
			'id': 22,
			'title': 'rbac用户列表',
			'menu_id': 9,
			'children': [{
				'id': 23,
				'title': 'rbac增加用户',
				'pid_id': 22
			}, {
				'id': 24,
				'title': 'rbac编辑用户',
				'pid_id': 22
			}, {
				'id': 25,
				'title': 'rbac删除用户',
				'pid_id': 22
			}, {
				'id': 26,
				'title': 'rbac重置密码',
				'pid_id': 22
			}]
		}, {
			'id': 27,
			'title': 'rbac菜单列表',
			'menu_id': 9,
			'children': [{
				'id': 28,
				'title': 'rbac添加菜单',
				'pid_id': 27
			}, {
				'id': 29,
				'title': 'rbac编辑菜单',
				'pid_id': 27
			}, {
				'id': 30,
				'title': 'rbac删除菜单',
				'pid_id': 27
			}, {
				'id': 31,
				'title': 'rbac增加二级菜单',
				'pid_id': 27
			}, {
				'id': 32,
				'title': 'rbac编辑二级菜单',
				'pid_id': 27
			}, {
				'id': 33,
				'title': 'rbac删除二级菜单',
				'pid_id': 27
			}, {
				'id': 34,
				'title': 'rbac增加权限',
				'pid_id': 27
			}, {
				'id': 35,
				'title': 'rbac编辑权限',
				'pid_id': 27
			}, {
				'id': 36,
				'title': 'rbac删除权限',
				'pid_id': 27
			}, {
				'id': 37,
				'title': 'rbac批量权限操作',
				'pid_id': 27
			}, {
				'id': 38,
				'title': 'rbac删除权限',
				'pid_id': 27
			}]
		}]
	}
}
	




