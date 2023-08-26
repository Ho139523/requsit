# Generated by Django 3.1 on 2021-05-01 08:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان دسته بندی')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نشان داده شود؟')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='آدرسدسته بندیا')),
                ('position', models.IntegerField(verbose_name='موقعیت')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی\u200cها',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('user_name', models.CharField(max_length=20, verbose_name='نام کاربری')),
                ('password', models.IntegerField(verbose_name='رمز عبور')),
                ('image', models.ImageField(upload_to='media/users', verbose_name='تصویر کاربر')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='آدرس')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('country', models.CharField(max_length=50, verbose_name='کشور')),
                ('date_of_birth', models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 5, 1, 8, 58, 51, 754938, tzinfo=utc))),
                ('language', models.CharField(choices=[('E', 'English'), ('P', 'Persian')], default='E', max_length=3, verbose_name='زبان')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان کالا')),
                ('availability', models.BooleanField(default=True, verbose_name='موجود در انبار')),
                ('description', models.CharField(max_length=10000, verbose_name='جزییات کالا')),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000000, verbose_name='قیمت کالا')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='درصد رضایت از کالا')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='آدرس کالا')),
                ('image', models.ImageField(upload_to='media', verbose_name='تصویر کالا')),
                ('category', models.ManyToManyField(null=True, related_name='Goods', to='sale.Category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'کالا',
                'verbose_name_plural': 'کالاها',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='نظر')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.goods', verbose_name='کالای مربوطه')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.user', verbose_name='کاربر مربوطه')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='متن تبلیغات')),
                ('off_bool', models.BooleanField(blank=True, help_text='آیا تخفیف خورده است؟', unique=True, verbose_name='داشتن تخفیف')),
                ('off', models.DecimalField(blank=True, decimal_places=2, default=10, max_digits=4, null=True, verbose_name='درصد تخفیف')),
                ('image', models.ImageField(upload_to='media', verbose_name='تصویر کالا')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.goods', verbose_name='کالا')),
            ],
            options={
                'verbose_name': 'تخفیف',
                'verbose_name_plural': 'تخفیفات',
            },
        ),
    ]
