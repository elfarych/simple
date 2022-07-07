from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

from profiles.models import Seller


class Shop(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, related_name='shops')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    logo = ThumbnailerImageField(upload_to='shop/logo/', resize_source={'size': (500, 500), 'crop': 'scale'}, null=True,
                                 blank=True, max_length=1000)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(null=True, blank=True)
    fcm_token = models.CharField(null=True, blank=True, max_length=255)
    whatsapp = models.CharField(null=True, blank=True, max_length=255)
    telegram = models.CharField(null=True, blank=True, max_length=255)
    vk = models.CharField(null=True, blank=True, max_length=255)
    instagram = models.CharField(null=True, blank=True, max_length=255)
    tiktok = models.CharField(null=True, blank=True, max_length=255)
    facebook = models.CharField(null=True, blank=True, max_length=255)
    twitter = models.CharField(null=True, blank=True, max_length=255)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)

    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.pk

    class Meta:
        ordering = ('-date',)


class ShopImage(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    name = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shop

    class Meta:
        ordering = ('-date',)


class MainCategory(models.Model):
    name = models.CharField(max_length=255)
    image = ThumbnailerImageField(upload_to='shop/categories/', resize_source={'size': (500, 500), 'crop': 'scale'},
                                  null=True, blank=True, max_length=1000)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date', 'order')


class Category(models.Model):
    main_category = models.ManyToManyField(MainCategory, blank=True, related_name='child')
    name = models.CharField(max_length=255)
    image = ThumbnailerImageField(upload_to='shop/categories/', resize_source={'size': (500, 500), 'crop': 'scale'},
                                  null=True, blank=True, max_length=1000)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date', 'order')


class CharacteristicType(models.Model):
    categories = models.ManyToManyField(Category, blank=True, related_name='characteristic_types')
    name = models.CharField(max_length=255)
    image = ThumbnailerImageField(upload_to='shop/characteristic_types/',
                                  resize_source={'size': (300, 300), 'crop': 'scale'},
                                  null=True, blank=True, max_length=1000)
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('-date', 'order')


class Characteristic(models.Model):
    type = models.ForeignKey(CharacteristicType, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='values')
    name = models.CharField(max_length=255)
    image = ThumbnailerImageField(upload_to='shop/characteristic_types/',
                                  resize_source={'size': (300, 300), 'crop': 'scale'},
                                  null=True, blank=True, max_length=1000)
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date', 'order')


class Product(models.Model):
    name = models.CharField(max_length=255)
    article = models.CharField(max_length=255)
    miniature = ThumbnailerImageField(upload_to='shop/product_miniatures/',
                                  resize_source={'size': (400, 400), 'crop': 'scale'}, null=True, blank=True,
                                  max_length=1000)
    rating = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    old_price = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True, default=0)
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    views_count = models.PositiveIntegerField(null=True, blank=True)
    sold_count = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(default=False)

    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, related_name='products')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='products')
    categories = models.ManyToManyField(Category, blank=True, related_name='products')
    main_categories = models.ManyToManyField(MainCategory, blank=True, related_name='products')
    characteristics = models.ManyToManyField(Characteristic, blank=True, related_name='products')
    related_products = models.ManyToManyField('self', blank=True, related_name='related_products')
    slug = models.SlugField(null=True, unique=True)

    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date', 'order')


class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_reviews')
    shop_rating = models.FloatField(null=True, blank=True)
    shop_review = models.TextField(null=True, blank=True)
    product_rating = models.FloatField(null=True, blank=True)
    product_review = models.TextField(null=True, blank=True)
    is_complaint = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    photo = ThumbnailerImageField(upload_to='shop/reviews/',
                                      resize_source={'size': (500, 500), 'crop': 'scale'}, null=True, blank=True,
                                      max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.shop or self.product or self.pk}'

    class Meta:
        ordering = ('-date',)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='images')
    image = ThumbnailerImageField(upload_to='shop/product/images/', resize_source={'size': (1500, 1500), 'crop': 'scale'}, null=True, blank=True, max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product or self.pk

    class Meta:
        ordering = ('-date',)


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='videos')
    file = models.FileField(upload_to='shop/product/videos/')
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product or self.pk

    class Meta:
        ordering = ('-date',)