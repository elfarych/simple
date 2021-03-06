# Generated by Django 4.0.5 on 2022-06-02 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, max_length=1000, null=True, upload_to='shop/categories/')),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-date', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, max_length=1000, null=True, upload_to='shop/characteristic_types/')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-date', 'order'),
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, max_length=1000, null=True, upload_to='shop/categories/')),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-date', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('article', models.CharField(max_length=255)),
                ('miniature', easy_thumbnails.fields.ThumbnailerImageField(blank=True, max_length=1000, null=True, upload_to='shop/product_miniatures/')),
                ('rating', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('old_price', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('views_count', models.PositiveIntegerField(blank=True, null=True)),
                ('sold_count', models.PositiveIntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='products', to='shop.category')),
                ('characteristics', models.ManyToManyField(blank=True, related_name='products', to='shop.characteristic')),
                ('main_categories', models.ManyToManyField(blank=True, related_name='products', to='shop.maincategory')),
                ('related_products', models.ManyToManyField(blank=True, related_name='related_products', to='shop.product')),
            ],
            options={
                'ordering': ('-date', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', easy_thumbnails.fields.ThumbnailerImageField(blank=True, max_length=1000, null=True, upload_to='shop/logo/')),
                ('address', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('fcm_token', models.CharField(blank=True, max_length=255, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True)),
                ('telegram', models.CharField(blank=True, max_length=255, null=True)),
                ('vk', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField()),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shops', to='profiles.seller')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='shop.shop')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_rating', models.FloatField(blank=True, null=True)),
                ('shop_review', models.TextField(blank=True, null=True)),
                ('product_rating', models.FloatField(blank=True, null=True)),
                ('product_review', models.TextField(blank=True, null=True)),
                ('is_complaint', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(blank=True, max_length=1000, null=True, upload_to='shop/reviews/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_reviews', to='shop.shop')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='shop.shop')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='ProductVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='shop/product/videos/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='shop.product')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, max_length=1000, null=True, upload_to='shop/product/images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='shop.product')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.shop'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CharacteristicType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, max_length=1000, null=True, upload_to='shop/characteristic_types/')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='characteristic_types', to='shop.category')),
            ],
            options={
                'ordering': ('-date', 'order'),
            },
        ),
        migrations.AddField(
            model_name='characteristic',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='characteristics', to='shop.characteristictype'),
        ),
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.ManyToManyField(blank=True, related_name='child', to='shop.maincategory'),
        ),
    ]
