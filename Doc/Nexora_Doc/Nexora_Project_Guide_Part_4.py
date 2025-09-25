# This part will cover:

# * **Order & OrderItem models**
# * **Order APIs** (list history, detail, admin update status)
# * **Payment API (simulation)** – store transactions
# * (Optional here) **Wishlist API** (customer feature)



# Part 4 — Orders & Payments

## 1) Create `orders` app


# python manage.py startapp orders


# Add in `settings.py`:


'orders',



## 2) `orders/models.py`


from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING'
        PAID = 'PAID'
        SHIPPED = 'SHIPPED'
        DELIVERED = 'DELIVERED'
        CANCELLED = 'CANCELLED'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product} x {self.quantity}"


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50, default="Razorpay")
    transaction_id = models.CharField(max_length=100, unique=True)
    success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.transaction_id} for Order {self.order.id}"




## 3) `orders/serializers.py`


from rest_framework import serializers
from .models import Order, OrderItem, Payment
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'total', 'status', 'created_at', 'items')
        read_only_fields = ('id', 'user', 'total', 'created_at', 'items')


class PaymentSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = Payment
        fields = ('id', 'order', 'amount', 'method', 'transaction_id', 'success', 'created_at')
        read_only_fields = ('id', 'created_at')




## 4) `orders/views.py`


import uuid
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Order, Payment
from .serializers import OrderSerializer, PaymentSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "ADMIN":
            return Order.objects.all().order_by('-created_at')
        return Order.objects.filter(user=user).order_by('-created_at')


class PaymentViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        order_id = request.data.get("order_id")
        method = request.data.get("method", "Razorpay")
        amount = request.data.get("amount")

        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        if order.status != Order.Status.PENDING:
            return Response({"error": "Order already paid or processed"}, status=400)

        txn_id = str(uuid.uuid4())

        payment = Payment.objects.create(
            order=order,
            amount=amount,
            method=method,
            transaction_id=txn_id,
            success=True
        )

        # update order status
        order.status = Order.Status.PAID
        order.save()

        return Response(PaymentSerializer(payment).data, status=201)




## 5) `orders/urls.py`


from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, PaymentViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = router.urls




## 6) Update main `nexora/urls.py`


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/catalog/', include('products.urls')),
    path('api/', include('cart.urls')),
    path('api/', include('orders.urls')),   # 👈 added
]




## 7) Run migrations


# python manage.py makemigrations
# python manage.py migrate



## 8) Postman Test Examples

### 🔹 Checkout (from Part 3)


# POST http://127.0.0.1:8000/api/checkout/
# Authorization: Bearer <token>


# Response:


{ "message": "Order placed successfully", "order_id": 3 }


### 🔹 Pay for Order


# POST http://127.0.0.1:8000/api/payments/
# Authorization: Bearer <token>
# Content-Type: application/json

{
  "order_id": 3,
  "amount": 5000,
  "method": "UPI"
}


# Response:


{
  "id": 1,
  "order": 3,
  "amount": "5000.00",
  "method": "UPI",
  "transaction_id": "d2e30a9f-75e4-4ef0-b0f9-1a9dc8b9a4a9",
  "success": true,
  "created_at": "2025-08-20T06:30:00Z"
}


### 🔹 View My Orders


# GET http://127.0.0.1:8000/api/orders/
# Authorization: Bearer <token>


### 🔹 Admin Update Order Status

# (Admin user can PATCH)


# PATCH http://127.0.0.1:8000/api/orders/3/
# Authorization: Bearer <admin_token>
# Content-Type: application/json

{ "status": "SHIPPED" }




## ✅ What You Have Now

# * **Order system** with items and statuses.
# * **Payment simulation** (with unique transaction id).
# * **Customer order history** + Admin can update order status.
# * Integrated seamlessly with **Cart → Checkout → Order → Payment** flow.

