from django import template


register = template.Library()

@register.simple_tag()
def category_title():
	pass
	
@register.inclusion_tag('sale/partial/subscribe.html')
def subscribe():
	pass

@register.inclusion_tag('sale/partial/advantages.html')
def advantages():
	pass

@register.inclusion_tag('sale/partial/statistics.html')
def statistics():
	pass
	
	
@register.inclusion_tag('sale/partial/happy_clients.html')
def happy_clients():
	pass
	
	
