视频 40-46
	知识点：
		1.formset
			- 什么是formset
				答：django 的 form组件或ModelForm组件用于做一个表单验证。
				formset用于做多个表单验证的组件。
			- 应用场景？
				批量操作
			
			- 如何使用formset？
				查看:django 代码  luffy_formset 
		
		2.自动发现项目中的URL
			- 问题：给你一个项目，请帮我获取当前项目中都有哪些URL以及name   rbac:permission_list
			- 实现思路：
				具体实现查看：rbac.services.routes 下面的代码
				
		
		3.权限的批量操作
			1.获取项目中所有权限(用集合的方式：set1)
			2.去数据库中获取已经录入的所有权限(用集合的方式：set2)
			
			情况1：自动发现的权限 "大于" 数据库中的权限  --> 实现批量添加    ps: 通过name进行对比
					set1 - set2 == 添加的权限
					基于 formset
			情况2：数据库中的权限 "大于"  自动发现的权限  --> 批量删除
					set2 - set1 == "删除的权限"
					
			情况3：自动发现的权限 和数据库中的权限 个数一直，值有不一致的
					取交集  set3 = set1 & set2  --> 更新权限
					基于 formset
		
		
		
		
		