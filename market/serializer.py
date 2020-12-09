from re import T
from rest_framework import serializers
from rest_framework.fields import NOT_READ_ONLY_WRITE_ONLY
from .models import Mall, Shop, Product, User

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['email', 'first_name', 'last_name', 'password','avatar']
        extra_kwargs={
            'password': {'write_only':True}
        }

        def save(self):
            user = User(
                email=self.validated_data['email'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name']
            )
            password=self.validated_data['password'],
         
            user.set_password(password)
            user.save()
            return user

