from django.shortcuts import render, get_object_or_404
from football.models import News, Category


def news(request):
    context = {'news': News.objects.all(), 'category': Category.objects.filter(display=True)}
    return render(request, 'football/news.html', context)


def news_details(request, slug):
    context = {'news': get_object_or_404(News, slug=slug), 'category': Category.objects.filter(display=True)}
    return render(request, 'football/news_details.html', context)


def home(request):
    return render(request, 'football/home.html')


def about(request):
    return render(request, 'football/about.html')


def contact(request):
    return render(request, 'football/contact.html')


def post(request):
    return render(request, 'football/post.html')
