from rest_framework import viewsets, permissions, filters
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

# Admin only permission
class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'ADMIN'


# Admin only can manage categories
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOnly]


# Admin only can manage brands
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOnly]


class IsAdminOrProductOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Everyone can view
        if request.method in permissions.SAFE_METHODS:
            return True

        # Admin full access
        if request.user.role == 'ADMIN':
            return True

        # Seller → only their own products
        return obj.seller == request.user


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrProductOwner]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


# 1) Wishlist API

from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
