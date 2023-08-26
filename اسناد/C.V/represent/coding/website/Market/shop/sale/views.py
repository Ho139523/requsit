from django.shortcuts import render, get_object_or_404
from .models import Goods, Category, Comments, User
from django.core.paginator import Paginator


def home(request):
	pag4 = [1, 2, 3, 4]
	pag3 = [1, 2, 3]
	goods_list = Goods.objects.available()
	paginator = Paginator(goods_list, 3)
	page = request.GET.get('page')
	goods = paginator.get_page(page)
	context = {'goods': goods, 'pag4': pag4, 'pag3': pag3}
	return render(request, 'sale/index.html', context)


def about(request):
	context = {'users': User.objects.all()}
	return render(request, 'sale/about.html', context)
	
	
def contact(request):
	context = {}
	return render(request, 'sale/contact.html', context)
	
	
def category(request, slug):
	context = {'cats': get_object_or_404(Category, slug=slug, status=True)}
	return render(request, 'sale/category.html', context)
	
	
def product(request, slug):
	context = {'good': get_object_or_404(Goods, slug=slug, availability=True)}
	return render(request, 'sale/product.html', context)
	
	
def services(request):
	context = {}
	return render(request, 'sale/services.html', context)
	