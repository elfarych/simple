from rest_framework import serializers
from . import models


class ShopImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ShopImage
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    images = ShopImageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Shop
        fields = '__all__'


class ShopListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Shop
        fields = ('id', 'name', 'logo', 'phone_number')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'


class MainCategorySerializer(serializers.ModelSerializer):
    child = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = models.MainCategory
        fields = '__all__'


class CharacteristicTypeNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CharacteristicType
        fields = ('id', 'name')


class CharacteristicSerializer(serializers.ModelSerializer):
    type = CharacteristicTypeNameSerializer(many=False, read_only=True)

    class Meta:
        model = models.Characteristic
        fields = '__all__'


class CharacteristicTypeSerializer(serializers.ModelSerializer):
    values = CharacteristicSerializer(many=True, read_only=True)

    class Meta:
        model = models.CharacteristicType
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    characteristic_types = CharacteristicTypeSerializer(many=True)

    class Meta:
        model = models.Category
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'miniature', 'rating', 'old_price', 'price', 'quantity', 'order', 'product_reviews')


class ProductDetailSerializer(serializers.ModelSerializer):
    shop = ShopSerializer(many=False, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    main_categories = MainCategorySerializer(many=True, read_only=True)
    characteristics = CharacteristicSerializer(many=True, read_only=True)
    related_products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductImage
        fields = '__all__'


class ProductVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductVideo
        fields = '__all__'


