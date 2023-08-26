from django.contrib import admin
from .models import Goods, Category, Comments, User

class GoodsAdmin(admin.ModelAdmin):
	list_display = ['title', 'price', 'availability', 'rating', 'cat_to_str']
	list_editable = ['availability']
	list_filter = ['availability']
	search_fields = ['description', 'price', 'title', 'cat_to_str']
	prepopulated_fields = {'slug': ('title',)}
	
	def cat_to_str(self, obj):
		return ', '.join(cat.title for cat in obj.category.all())
	
	
admin.site.register(Goods, GoodsAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['position', 'title', 'status']
	list_editable = ['title', 'status']
	list_filter = ['status']
	search_field = ['title']
	prepopulated_fields = {'slug': ('title',)}
	
	
admin.site.register(Category, CategoryAdmin)


class CommentsAdmin(admin.ModelAdmin):
	list_display = ['user', 'good']
	list_editable = []
	list_filter = ['user', 'good']
	search_field = ['comment']
	prepopulated_fields = {}
	
	
admin.site.register(Comments, CommentsAdmin)


class UserAdmin(admin.ModelAdmin):
	list_display = ['name', 'last_name', 'user_name','email', 'country', 'date_of_birth', 'language']
	list_editable = ['user_name', 'country']
	list_filter = ['language', 'country']
	search_field = ['name','last_name', 'user_name','email']
	prepopulated_fields = {'slug': ('user_name',)}
	
	
admin.site.register(User, UserAdmin)