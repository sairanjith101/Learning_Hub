from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet, ProductViewSet, WishlistViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('brands', BrandViewSet, basename='brands')
router.register('products', ProductViewSet, basename='products')
router.register('wishlist', WishlistViewSet, basename='wishlist')

urlpatterns = router.urls
