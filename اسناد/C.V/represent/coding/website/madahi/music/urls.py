from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.Hajmahmood98View.as_view(),name='haj mahmood 98'),
    path("song/add", views.SongCreate.as_view(), name='song-add')
]