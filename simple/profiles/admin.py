from django.contrib import admin
from . import models


class SellerDocumentInline(admin.TabularInline):

    model = models.SellerDocument
    extra = 0


@admin.register(models.Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'active', 'is_verified', 'date')
    list_editable = ('active', 'is_verified')
    search_fields = ('email', 'phone_number', 'company_name')
    list_filter = ('active', 'is_verified', 'date', 'update')
    inlines = [SellerDocumentInline]


@admin.register(models.Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'active', 'date')
    list_editable = ('active',)
    search_fields = ('email', 'phone_number', 'name')
    list_filter = ('active', 'date', 'update')


