from django.db import models
from django.utils import timezone


class Category(models.Model):
	title = models.CharField(max_length=2000, default='No Category')
	slug = models.SlugField(max_length=100, unique=True)
	display = models.BooleanField(default=True, verbose_name='should be diplayed?')
	position=models.IntegerField(verbose_name='position')
	
	
	class Meta:
		verbose_name = 'Categorie'
		ordering = ['position']
		
	def __str__(self):
		return self.title


class News(models.Model):
    STATUS_CHOICES = (
        ('b', 'breaking'), ('f', 'first hand')
    )
    title = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, verbose_name='Category')
    image = models.ImageField(upload_to='images')
    published = models.DateTimeField(default=timezone.now)
    happened = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'new'
        ordering = ['-published',]

    def __str__(self):
        return self.title