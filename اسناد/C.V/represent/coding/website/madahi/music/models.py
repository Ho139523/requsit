from django.db import models
from django.urls import reverse

class album(models.Model):
	artist=models.CharField(max_length=500)
	title=models.CharField(max_length=500)
	logo=models.CharField(max_length=5000)
	fav=models.BooleanField(default=False)
	def __str__(self):
		return self.artist + '-' + self.title
	
class song(models.Model):
	album=models.ForeignKey(album, on_delete=models.CASCADE)
	song_title=models.CharField(max_length=500)
	logo=models.CharField(max_length=500)
	genre=models.CharField(default='null', max_length=500)
	path=models.CharField(default='null', max_length=500)
	des=models.CharField(max_length=500)
	fave=models.BooleanField(default=False)
	def __str__(self):
		return self.album + '-' + self.song_title
		
	def get_absolute_url(self):
		reverse('music:haj mahmood 98')