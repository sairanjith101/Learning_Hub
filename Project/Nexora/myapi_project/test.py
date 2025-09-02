from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet, ProductViewSet

router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('brand', BrandViewSet, basename='brand')
router.register('product', ProductViewSet, basename='product')

urlpatterns = router.urls