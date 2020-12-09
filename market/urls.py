from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register("api/products", views.ProductList, basename='Product')
router.register("api/malls", views.MallList, basename='Mall')
router.register("api/shops", views.ShopList, basename='Shop')

app_name='market'

urlpatterns =[
    path('', include(router.urls)),
    path('registration/', views.registration_view, name="register"),
    path('login/', obtain_auth_token, name='login')
]