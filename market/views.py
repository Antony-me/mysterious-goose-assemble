from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ProductSerializer, MallSerializer, ShopSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Product, Mall, Shop
from rest_framework import mixins, viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view



class ProductList(viewsets.ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

        def post(self, request, format=None):
            serializers = ProductSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
  
class ShopList(viewsets.ModelViewSet):
   
        queryset = Shop.objects.all()
        serializer_class = ShopSerializer

        def post(self, request, format=None):
            serializers = ShopSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class MallList(viewsets.ModelViewSet):
   
        queryset = Mall.objects.all()
        serializer_class = MallSerializer

        def post(self, request, format=None):
            serializers = ShopSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)