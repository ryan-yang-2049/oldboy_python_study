

from django import template

# register 不能改变
register = template.Library()

@register.filter
def mutli_fliter(x,y):



	return x*y


@register.simple_tag
def mutli_tag(x,y):


	return x*y




