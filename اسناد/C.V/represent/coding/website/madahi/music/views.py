from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import album, song

class Hajmahmood98View(generic.ListView):
	context_object_name = 'all_album'
	template_name="music/haj Mahmood 98.html"
	queryset=album.objects.all()
	
	def get_context_data(self, **kwargs):
		context=super(Hajmahmood98View, self).get_context_data(**kwargs)
		context['all_album'] = album.objects.all()
		context['all_song'] = song.objects.all()
		return context
	
class SongCreate(CreateView):
	model = song
	fields=['album', 'song_title', 'logo', 'genre', 'path', 'des', 'fave', ]
	seccess_url=reverse_lazy('music:haj mahmood 98')
		

	#def get_queryset(self):
	#	return album.objects.all()