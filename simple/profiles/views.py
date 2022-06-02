from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers


class SellerMeView(generics.ListAPIView):
    # Получение продавца в зависимости от юзера, который иницировал запрос
    serializer_class = serializers.SellerSerializer

    def get_queryset(self):
        queryset = models.Seller.objects.filter(user=self.request.user.id or None)
        return queryset


class CreateSellerView(generics.CreateAPIView):
    # Создание нового продавца. user = user, который иницирует запрос
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateSellerView(generics.UpdateAPIView):
    # Обновление продавца
    serializer_class = serializers.SellerSerializer

    def get_queryset(self):
        queryset = models.Seller.objects.filter(user=self.request.user.id or None)
        return queryset


class CreateSellerDocumentView(generics.CreateAPIView):
    # Создание документа продавца.
    queryset = models.SellerDocument.objects.all()
    serializer_class = serializers.DocumentsSerializer
    permission_classes = [IsAuthenticated]


class DeleteSellerDocumentView(generics.UpdateAPIView):
    # Обновление документа продавца
    serializer_class = serializers.DocumentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = models.SellerDocument.objects.all()
        return queryset


class BuyerMeView(generics.ListAPIView):
    # Получение покупателя в зависимости от юзера, который иницировал запрос
    serializer_class = serializers.BuyerSerializer

    def get_queryset(self):
        queryset = models.Buyer.objects.filter(user=self.request.user or None)
        return queryset


class CreateBuyerView(generics.CreateAPIView):
    # Создание нового покупателя. user = user, который иницирует запрос
    queryset = models.Buyer.objects.all()
    serializer_class = serializers.BuyerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user or None)


class UpdateBuyerView(generics.UpdateAPIView):
    # Обновление покупателя
    serializer_class = serializers.BuyerSerializer

    def get_queryset(self):
        queryset = models.Buyer.objects.filter(user=self.request.user.id)
        return queryset
