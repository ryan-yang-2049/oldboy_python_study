# -*- coding: utf-8 -*-

# __title__ = 'my_tags.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.07.12'

from django import template

from blog import models
from django.db.models import Avg,Max,Min,Count

register = template.Library()

@register.inclusion_tag("classification.html")
def get_classification_style(username):
	user_obj = models.UserInfo.objects.filter(username=username).first()
	blog = user_obj.blog
	cate_list = models.Category.objects.filter(blog=blog).values('pk').annotate(
		c=Count("article__title")).values_list("title", "c")
	tag_list = models.Tag.objects.filter(blog=blog).values('pk').annotate(c=Count("article")).values_list("title","c")
	date_list = models.Article.objects.filter(user=user_obj).extra(select={"y_m_date": "date_format(create_time,'%%Y-%%m')"}).values("y_m_date").annotate(c=Count('nid')).values_list("y_m_date", "c")

	return {"blog":blog,"cate_list":cate_list,"tag_list":tag_list,"date_list":date_list}









