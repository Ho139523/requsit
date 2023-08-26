from django.contrib import admin
from .models import News, Category


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('position', 'title', 'slug', 'display')
	list_filter = (['slug'])
	list_editable = (['display'])
	search_fields = ('title', 'slug')
	prepopulated_fields = {'slug':('title',)}
	
	
admin.site.register(Category, CategoryAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'cat_to_list', 'status')
    list_editable = ('status',)
    list_filter = ('published', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-published']
    
    
    def cat_to_list(category, obj):
    	return ", ".join([category.title for category in obj.category.all()])
    cat_to_list.short_description = 'categories'
    

admin.site.register(News, NewsAdmin)
