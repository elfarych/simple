from rest_framework import serializers
from . import models


class DocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SellerDocument
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    documents = DocumentsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Seller
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Buyer
        fields = '__all__'
