from django.db import models
from django.utils import timezone

class GoodsManager(models.Manager):
	def available(self):
		return self.filter(availability=True)
		
		
class CategoryManager(models.Manager):
	def active(self):
		return self.filter(status=True)
		
		
class Category(models.Model):
	title = models.CharField(max_length=250, verbose_name='عنوان دسته بندی')
	status = models.BooleanField(default=True, null=False,verbose_name='آیا نشان داده شود؟')
	slug = models.SlugField(unique=True, max_length=250, null=False, verbose_name='آدرسدسته بندیا')
	position = models.IntegerField(verbose_name='موقعیت')
	
	
	class Meta():
		verbose_name = 'دسته بندی'
		verbose_name_plural = 'دسته بندی‌ها'
		ordering = ['position']
		
	def __str__(self):
		return self.title
		
	objects = CategoryManager()


class Goods(models.Model):
	title = models.CharField(max_length=250, verbose_name='عنوان کالا')
	category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='Goods')
	availability = models.BooleanField(default=True, null=False,verbose_name='موجود در انبار')
	description = models.TextField(max_length=10000, verbose_name='جزییات کالا')
	price = models.DecimalField(decimal_places=2, max_digits=10000000, verbose_name='قیمت کالا')
	rating = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='درصد رضایت از کالا')
	slug = models.SlugField(unique=True, max_length=250, null=False, verbose_name='آدرس کالا')
	image = models.ImageField(upload_to='media', verbose_name='تصویر کالا')
	
	class Meta():
		verbose_name = 'کالا'
		verbose_name_plural = 'کالاها'
		ordering = ['title']
		
	def __str__(self):
		return self.title
		
	objects = GoodsManager()
	
	
class User(models.Model):
    lang = (('E', 'English'), ('P', 'Persian'))
    name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    user_name = models.CharField(max_length=20, verbose_name='نام کاربری')
    password = models.IntegerField(verbose_name='رمز عبور')
    image = models.ImageField(upload_to='media/users', verbose_name='تصویر کاربر')
    slug = models.SlugField(unique=True, verbose_name='آدرس', null=True)
    email = models.EmailField(max_length=254, verbose_name='ایمیل')
    country = models.CharField(max_length=50, verbose_name='کشور')
    date_of_birth = models.DateTimeField(timezone.now(), auto_now_add=True)
    language = models.CharField(max_length=3, choices=lang, default='E', verbose_name='زبان')

    def __str__(self):
        return self.name + ' ' + self.last_name

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Comments(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='کالای مربوطه')
    comment = models.TextField(verbose_name='نظر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر مربوطه')

    def __str__(self):
        return self.user.name + ' - ' + self.good.title

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class ads(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='کالا')
    text = models.TextField(max_length=5000, verbose_name='متن تبلیغات')
    off_bool = models.BooleanField(unique=True, blank=True, null=False, editable=True,help_text='آیا تخفیف خورده است؟', verbose_name='داشتن تخفیف')
    off = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='درصد تخفیف', null=True, blank=True, default=10)
    image = models.ImageField(upload_to='media', verbose_name='تصویر کالا')

    def __str__(self):
        return self.good + ' -- ' + self.off

    class Meta:
        verbose_name = 'تخفیف'
        verbose_name_plural = 'تخفیفات'
	
	