from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

from profiles.models import Seller


class Shop(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, related_name='shops')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(null=True, blank=True, max_length=255)
    logo = ThumbnailerImageField(upload_to='shop/logo/', resize_source={'size': (500, 500), 'crop': 'scale'}, null=True, blank=True, max_length=1000)
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
    slug = models.SlugField()

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
    name = models.CharField(null=True, blank=True, max_length=255)
    image = ThumbnailerImageField(upload_to='shop/logo/', resize_source={'size': (500, 500), 'crop': 'scale'}, null=True, blank=True, max_length=1000)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

