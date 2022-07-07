from django_filters import rest_framework as filters
from . import models


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductImagesFilter(filters.FilterSet):
    product = CharFilterInFilter(field_name='product')

    class Meta:
        model = models.ProductImage
        fields = ['product']


class ProductVideosFilter(filters.FilterSet):
    product = CharFilterInFilter(field_name='product')

    class Meta:
        model = models.ProductVideo
        fields = ['product']


class ReviewsFilter(filters.FilterSet):
    product = CharFilterInFilter(field_name='product')
    shop = CharFilterInFilter(field_name='shop')

    class Meta:
        model = models.Review
        fields = ['product', 'shop']


class ProductsFilter(filters.FilterSet):
    categories = CharFilterInFilter(field_name='categories', lookup_expr='in')
    characteristics = CharFilterInFilter(field_name='characteristics', lookup_expr='in')
    shop = CharFilterInFilter(field_name='shop')
    price = filters.RangeFilter()

    class Meta:
        model = models.Product
        fields = ['categories', 'characteristics', 'shop', 'price']
