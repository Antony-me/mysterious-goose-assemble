from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("api/products", views.ProductList, basename='Product')
router.register("api/malls", views.MallList, basename='Mall')
router.register("api/shops", views.ShopList, basename='Shop')

app_name='supermall'

urlpatterns =[
    path('', include(router.urls)),
    # path('registration/', views.registration_view, name="register")
]