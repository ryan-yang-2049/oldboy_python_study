"""mysites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include,register_converter

from app01 import views
from app01.url_convert import MonConvert


# 注册自定义的url转换器
register_converter(MonConvert,"MC")



urlpatterns = [
    path('admin/', admin.site.urls),

	# path('articles/<int:year>/',views.path_year), # year 是 int 类型
	path('articles/<str:year>/',views.path_year),   # year 是 str类型

		# Django默认支持以下5个转化器：
		# str,匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
		# int,匹配正整数，包含0。
		# slug,匹配字母、数字以及横杠、下划线组成的字符串。
		# uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00。
		# path,匹配任何非空字符串，包含了路径分隔符

	# path指定的转换器
	path('articles/<int:year>/<MC:month>',views.path_year_month)


]
