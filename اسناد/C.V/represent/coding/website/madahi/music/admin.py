from django.contrib import admin

from .models import song, album

admin.site.register(song)
admin.site.register(album)
