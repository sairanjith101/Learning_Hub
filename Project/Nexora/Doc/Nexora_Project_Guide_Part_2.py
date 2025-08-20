
# * **Models** for `Category`, `Brand`, `Product`.
# * **CRUD APIs** (Create/Update/Delete → only `Admin` & `Seller`, Read → Everyone).
# * **Filters & Search** for products.

# Part 2 — Catalog (Categories, Brands, Products)

## 1) Create app

# python manage.py startapp products


# Add to `INSTALLED_APPS` in **settings.py**:

'products',



## 2) `products/models.py`


from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="products")

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.brand}"




## 3) `products/serializers.py`


from rest_framework import serializers
from .models import Category, Brand, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source="category", write_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), source="brand", write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock',
                  'category', 'brand', 'category_id', 'brand_id',
                  'seller', 'created_at', 'updated_at')
        read_only_fields = ('id', 'seller', 'created_at', 'updated_at')




## 4) `products/views.py`


from rest_framework import viewsets, permissions, filters
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

class IsAdminOrSeller(permissions.BasePermission):
    """
    Custom permission: only Admin or Seller can create/update/delete.
    Customers can only read.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role in ['ADMIN', 'SELLER']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrSeller]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOrSeller]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrSeller]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)




## 5) `products/urls.py`


from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet, ProductViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('brands', BrandViewSet, basename='brands')
router.register('products', ProductViewSet, basename='products')

urlpatterns = router.urls




## 6) Hook into main urls (`nexora/urls.py`)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/catalog/', include('products.urls')),
]



## 7) Run migrations


# python manage.py makemigrations
# python manage.py migrate




## 8) Postman Test Examples

### 🔹 Create Category (Admin/Seller only)


# POST http://127.0.0.1:8000/api/catalog/categories/
# Authorization: Bearer <token>
# Content-Type: application/json

{ "name": "Electronics", "description": "All gadgets" }


### 🔹 Create Brand


# POST http://127.0.0.1:8000/api/catalog/brands/
# Authorization: Bearer <token>
# Content-Type: application/json

{ "name": "Samsung", "description": "Smart Devices" }


### 🔹 Create Product


# POST http://127.0.0.1:8000/api/catalog/products/
# Authorization: Bearer <token>
# Content-Type: application/json

{
  "name": "Galaxy S25",
  "description": "Latest Samsung flagship",
  "price": 65000,
  "stock": 100,
  "category_id": 1,
  "brand_id": 1
}


### 🔹 Search & Filter


# GET http://127.0.0.1:8000/api/catalog/products/?search=galaxy
# GET http://127.0.0.1:8000/api/catalog/products/?ordering=-price




## ✅ What You Have Now

# * **Categories, Brands, Products** API.
# * CRUD allowed for **Admin & Seller** only.
# * Customers → **Read-only** access.
# * Search & sort products by **price, created\_at, name, description**.



