from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sale'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('product/<slug:slug>/', views.product, name='product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)