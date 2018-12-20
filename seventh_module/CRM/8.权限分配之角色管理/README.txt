视频 22-28

知识点
	1.namespace 用法： 
		用于在html中用 {% url "rbac:role_list"%}这样的用法去解析地址
		在views中 可以这样 return redirect(reverse('rbac:role_list')) 去返回页面
	
	2.django forms 组件
			forms 组件用法可以查看笔记
			forms 的class Meta 的用法，可以在笔记里面改进
			class meta 介绍可以看这里# https://blog.csdn.net/Leo062701/article/details/80963625
			class RoleModelForm(forms.ModelForm):
				class Meta:        
					model = models.Role
					fields = ['title',]

					widgets ={
						'title': forms.TextInput(attrs={'class':'form-control'})
					}		