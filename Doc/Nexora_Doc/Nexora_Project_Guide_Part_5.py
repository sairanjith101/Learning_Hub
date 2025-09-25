# This will give your project a **real-world polish**:

# * **Wishlist API**
# * **Coupons / Discounts**
# * **API Docs (Swagger / Redoc)**
# * **Rate Limiting**
# * **Logging & Error Handling**
# * **Deployment notes**



# Part 5 — Extra Features

## 1) Wishlist API

# 👉 Add it to the **products** app since it belongs to the catalog.

### `products/models.py` (add at bottom)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlisted_by")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} → {self.product.name}"


### `products/serializers.py`


from .models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source="product", write_only=True)

    class Meta:
        model = Wishlist
        fields = ('id', 'product', 'product_id', 'added_at')
        read_only_fields = ('id', 'added_at')


### `products/views.py`


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


### `products/urls.py`


from .views import WishlistViewSet

router.register('wishlist', WishlistViewSet, basename='wishlist')


# ✅ Now customers can **add/remove products** to their wishlist.



## 2) Coupons / Discounts

### `orders/models.py`


class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.PositiveIntegerField()  # e.g., 10 for 10%
    active = models.BooleanField(default=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    def __str__(self):
        return f"{self.code} - {self.discount_percent}%"


### `orders/serializers.py`


from .models import Coupon

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


### `orders/views.py`


from .models import Coupon
from .serializers import CouponSerializer
from rest_framework import viewsets

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAdminUser]


### `orders/urls.py`


from .views import CouponViewSet

router.register('coupons', CouponViewSet, basename='coupons')


# 👉 In `CheckoutViewSet` (Part 3), you can extend it to **apply coupon** before creating the order.



## 3) API Docs with Swagger

# Install:


# pip install drf-yasg


### `nexora/urls.py`


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Nexora API",
      default_version='v1',
      description="Backend APIs for Nexora E-Commerce",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/catalog/', include('products.urls')),
    path('api/', include('cart.urls')),
    path('api/', include('orders.urls')),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


# ✅ Now visit:

# * `http://127.0.0.1:8000/swagger/`
# * `http://127.0.0.1:8000/redoc/`



## 4) Rate Limiting

# Install:


# pip install django-ratelimit


### `nexora/settings.py`


# INSTALLED_APPS += ['ratelimit']


### Example in `accounts/views.py`:


from ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

@method_decorator(ratelimit(key='ip', rate='5/m', block=True), name='dispatch')
class RegisterView(generics.CreateAPIView):
    ...


# 👉 This prevents **spam account creation** (5 requests per minute per IP).



## 5) Logging & Error Handling

### `nexora/settings.py`


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}


# 👉 All errors will go to `errors.log`.



## 6) Deployment Notes

# 1. **Production DB** → MySQL on AWS RDS or DigitalOcean Managed DB.
# 2. **Server** → AWS EC2 (Ubuntu) or PythonAnywhere.
# 3. **Gunicorn + Nginx** setup for EC2.
# 4. Use **`.env` file** for secrets (via `django-environ`).
# 5. Enable **HTTPS (Let’s Encrypt)**.



## ✅ What You Have Now

# * **Wishlist API** (customer feature).
# * **Coupon system** (admin-managed discounts).
# * **Swagger docs** for all APIs.
# * **Rate-limiting** for security.
# * **Logging & error tracking**.
# * **Deployment roadmap** (AWS EC2 + RDS).

