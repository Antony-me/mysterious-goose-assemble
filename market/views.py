from .serializer import ProductSerializer, MallSerializer, ShopSerializer, UserSerializer
from rest_framework.response import Response
from .models import Product, Mall, Shop, User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permission import IsAdminOrReadOnly




class ProductList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, format=None):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
  
class ShopList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def post(self, request, format=None):
        serializers = ShopSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserList(viewsets.ModelViewSet):
    
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class MallList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Mall.objects.all()
    serializer_class = MallSerializer

    def post(self, request, format=None):
        serializers = ShopSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer= UserSerializer(data=request.data)
        data= {}
        if serializer.is_valid():
            user= serializer.save()
            # data['response']= 'succefully registered a new user'
            data['email']=user.email
            data['first_name']=user.first_name
            data['last_name']=user.last_name
        else:
            data=serializer.errors
        return Response(data)

