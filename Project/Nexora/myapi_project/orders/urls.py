from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, PaymentViewSet, CouponViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')
router.register('payments', PaymentViewSet, basename='payments')
router.register('coupons', CouponViewSet, basename='coupons')

urlpatterns = router.urls
