from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'football'
urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    re_path(r'^news_detail/(?P<slug>[-\w]+)/$', views.news_details, name='news_details'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post', views.post, name='post'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
