from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from . import models
from . import serializers
from . import service


class MyShopView(generics.ListAPIView):
    # Магазины пользователя, который инициировал запрос
    serializer_class = serializers.ShopSerializer

    def get_queryset(self):
        queryset = models.Shop.objects.filter(user=self.request.user.id)
        return queryset


class ShopListView(generics.ListAPIView):
    # Все магазины
    serializer_class = serializers.ShopListSerializer

    def get_queryset(self):
        queryset = models.Shop.objects.filter(active=True)
        return queryset


class ShopDetailView(generics.RetrieveAPIView):
    # Детальная информация о магазине
    serializer_class = serializers.ShopSerializer
    queryset = models.Shop.objects.filter(active=True)


class ShopUpdateView(generics.UpdateAPIView):
    # Обновление данных о магазине
    serializer_class = serializers.ShopSerializer

    def get_queryset(self):
        queryset = models.Shop.objects.filter(user=self.request.user.id)
        return queryset


class ShopCreateView(generics.CreateAPIView):
    # Создание магазина
    serializer_class = serializers.ShopSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user or None)


class ShopDeleteView(generics.DestroyAPIView):
    # Удаление магазина
    serializer_class = serializers.ShopSerializer

    def get_queryset(self):
        queryset = models.Shop.objects.filter(user=self.request.user.id)
        return queryset


class ShopImageCreateView(generics.CreateAPIView):
    # Создание фото магазина
    serializer_class = serializers.ShopImageSerializer
    queryset = models.ShopImage.objects.all()


class ShopImageDeleteView(generics.DestroyAPIView):
    # Удаление фото магазина
    serializer_class = serializers.ShopImageSerializer
    queryset = models.ShopImage.objects.all()


class MainCategoryListView(generics.ListAPIView):
    # Главные категории
    queryset = models.MainCategory.objects.all()
    serializer_class = serializers.MainCategorySerializer


class MainCategoryDetailView(generics.RetrieveAPIView):
    # Главная категория по id
    queryset = models.MainCategory.objects.all()
    serializer_class = serializers.MainCategorySerializer


class CategoryListView(generics.ListAPIView):
    # Категории
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    # Категория по id
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryDetailSerializer


class ProductListView(generics.ListAPIView):
    # Все товары
    queryset = models.Product.objects.filter(active=True)
    serializer_class = serializers.ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = service.ProductsFilter


class ProductDetailView(generics.RetrieveAPIView):
    # Детализация товара
    queryset = models.Product.objects.filter(active=True)
    serializer_class = serializers.ProductDetailSerializer


class ProductCreateView(generics.CreateAPIView):
    # Создание товара
    queryset = models.Product.objects.filter(active=True)
    serializer_class = serializers.ProductCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user or None)


class ProductUpdateView(generics.UpdateAPIView):
    # Обновление товара
    serializer_class = serializers.ProductDetailSerializer

    def get_queryset(self):
        queryset = models.Shop.objects.filter(user=self.request.user.id)
        return queryset


class ProductDeleteView(generics.DestroyAPIView):
    # Удаление товара
    serializer_class = serializers.ProductDetailSerializer

    def get_queryset(self):
        queryset = models.Shop.objects.filter(user=self.request.user.id)
        return queryset


class ProductImagesListView(generics.ListAPIView):
    # Фото товара
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = service.ProductImagesFilter


class ProductImageCreateView(generics.CreateAPIView):
    # Создание фото товара
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer


class ProductImageDeleteView(generics.DestroyAPIView):
    # Удаление фото товара
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer


class ProductVideosListView(generics.ListAPIView):
    # Видео товара
    queryset = models.ProductVideo.objects.all()
    serializer_class = serializers.ProductVideoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = service.ProductVideosFilter


class ProductVideoCreateView(generics.CreateAPIView):
    # Создание видео товара
    queryset = models.ProductVideo.objects.all()
    serializer_class = serializers.ProductVideoSerializer


class ProductVideoDeleteView(generics.DestroyAPIView):
    # Удаление видео товара
    queryset = models.ProductVideo.objects.all()
    serializer_class = serializers.ProductVideoSerializer


class ReviewListView(generics.ListAPIView):
    # Список отзывов
    queryset = models.Review.objects.filter(active=True)
    serializer_class = serializers.ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = service.ReviewsFilter


class ReviewCreateView(generics.CreateAPIView):
    # Создание отзывов
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class ReviewUpdateView(generics.UpdateAPIView):
    # Обновление отзывов
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class ReviewDeleteView(generics.DestroyAPIView):
    # Удаление отзывов
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

