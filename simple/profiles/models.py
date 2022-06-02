from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    company_name = models.CharField(null=True, blank=True, max_length=255)
    requisites = models.TextField(null=True, blank=True, max_length=2000)
    phone_number = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(null=True, blank=True)
    fcm_token = models.CharField(null=True, blank=True, max_length=255)
    photo = ThumbnailerImageField(upload_to='sellers/', resize_source={'size': (500, 500), 'crop': 'scale'}, null=True, blank=True, max_length=1000)
    active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name or self.pk

    class Meta:
        ordering = ('-date',)


class SellerDocument(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, related_name='documents')
    image = ThumbnailerImageField(upload_to='sellers/', resize_source={'size': (1000, 1000), 'crop': 'scale'}, null=True, blank=True, max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.seller.company_name or self.pk

    class Meta:
        ordering = ('-date',)


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=255)
    address = models.TextField(null=True, blank=True, max_length=255)
    phone_number = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(null=True, blank=True)
    fcm_token = models.CharField(null=True, blank=True, max_length=255)
    photo = ThumbnailerImageField(upload_to='sellers/', resize_source={'size': (500, 500), 'crop': 'scale'}, null=True, blank=True, max_length=1000)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.pk

    class Meta:
        ordering = ('-date',)
