from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CartViewSet, CheckoutViewSet

router = DefaultRouter()
router.register('cart', CartViewSet, basename='cart')
router.register('checkout', CheckoutViewSet, basename='checkout')

urlpatterns = router.urls
