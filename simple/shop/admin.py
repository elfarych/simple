from django.contrib import admin
from . import models


class ShopImagesInline(admin.TabularInline):
    model = models.ShopImage
    extra = 0


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'phone_number', 'email', 'active',  'date')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('active', )
    search_fields = ('name', 'email', 'phone_number', 'description', 'seller__company_name')
    list_filter = ('active', 'date', 'update')
    inlines = [ShopImagesInline]


@admin.register(models.MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'date')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('order',)
    list_filter = ('date', 'update')
    search_fields = ('name',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'date')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('order',)
    list_filter = ('date', 'update')
    search_fields = ('name',)


class CharacteristicsInline(admin.TabularInline):
    model = models.Characteristic
    extra = 0


@admin.register(models.CharacteristicType)
class CharacteristicTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'date')
    list_editable = ('order',)
    list_filter = ('date', 'update')
    search_fields = ('name',)
    inlines = [CharacteristicsInline]


@admin.register(models.Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'date')
    list_editable = ('order',)
    list_filter = ('date', 'update')
    search_fields = ('name',)


class ProductImagesInline(admin.TabularInline):
    model = models.ProductImage
    extra = 0


class ProductVideosInline(admin.TabularInline):
    model = models.ProductVideo
    extra = 0


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'shop', 'active', 'price', 'likes', 'views_count', 'sold_count', 'date')
    list_editable = ('active',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'shop__name')
    list_filter = ('active', 'date', 'update')
    inlines = [ProductImagesInline, ProductVideosInline]


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('shop', 'product', 'shop_rating', 'product_rating', 'is_complaint', 'active', 'date')
    list_editable = ('active',)
    search_fields = ('shop__name', 'product__name', 'shop_review', 'product_review')
    list_filter = ('active', 'is_complaint', 'shop_rating', 'product_rating')








