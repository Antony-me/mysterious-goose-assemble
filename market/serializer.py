from rest_framework import serializers
from .models import Mall, Shop, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ="__all__"

class ShopSerializer(serializers.ModelSerializer):
    products =ProductSerializer(read_only=True, many=True);
    class Meta:
        model = Shop
        fields ="__all__"

class MallSerializer(serializers.ModelSerializer):
    shops= ShopSerializer(read_only=True, many=True);
    class Meta:
        model = Mall
        fields ="__all__"
