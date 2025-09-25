# This part will cover:

# * **Cart model** (per customer).
# * APIs to **add/remove/update** cart items.
# * **Checkout API** → creates an **Order** from the cart.



# Part 3 — Cart & Checkout

## 1) Create `cart` app


# python manage.py startapp cart


# Add in `settings.py`:

'cart',




## 2) `cart/models.py`


from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("cart", "product")

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    @property
    def subtotal(self):
        return self.product.price * self.quantity




## 3) `cart/serializers.py`


from rest_framework import serializers
from .models import Cart, CartItem
from products.serializers import ProductSerializer
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source="product", write_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'product_id', 'quantity', 'subtotal')

    def get_subtotal(self, obj):
        return obj.subtotal


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'user', 'items', 'total_price')
        read_only_fields = ('id', 'user')

    def get_total_price(self, obj):
        return obj.total_price




## 4) `cart/views.py`


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from products.models import Product

class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def create(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data['product']
            quantity = serializer.validated_data['quantity']

            item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                item.quantity += quantity
            else:
                item.quantity = quantity
            item.save()
            return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        try:
            item = cart.items.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)

        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(CartSerializer(cart).data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        try:
            item = cart.items.get(pk=pk)
            item.delete()
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)
        return Response(CartSerializer(cart).data)




## 5) Checkout API (`cart/views.py` add)


from orders.models import Order, OrderItem  # we’ll create in Part 4

class CheckoutViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        if not cart.items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        # Create order
        order = Order.objects.create(user=request.user, total=cart.total_price)

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            # reduce stock
            item.product.stock -= item.quantity
            item.product.save()

        cart.items.all().delete()  # clear cart after checkout
        return Response({"message": "Order placed successfully", "order_id": order.id}, status=201)




## 6) `cart/urls.py`


from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CartViewSet, CheckoutViewSet

router = DefaultRouter()
router.register('cart', CartViewSet, basename='cart')
router.register('checkout', CheckoutViewSet, basename='checkout')

urlpatterns = router.urls




## 7) Hook into main `nexora/urls.py`


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/catalog/', include('products.urls')),
    path('api/', include('cart.urls')),   # 👈 added
]




## 8) Postman Test Examples

### 🔹 View Cart


# GET http://127.0.0.1:8000/api/cart/
# Authorization: Bearer <token>


### 🔹 Add Item to Cart


# POST http://127.0.0.1:8000/api/cart/
# Authorization: Bearer <token>
# Content-Type: application/json

{
  "product_id": 1,
  "quantity": 2
}


### 🔹 Update Item Quantity


# PUT http://127.0.0.1:8000/api/cart/1/
# Authorization: Bearer <token>
# Content-Type: application/json

{
  "quantity": 5
}


### 🔹 Remove Item


# DELETE http://127.0.0.1:8000/api/cart/1/
# Authorization: Bearer <token>


### 🔹 Checkout (Creates Order)


# POST http://127.0.0.1:8000/api/checkout/
# Authorization: Bearer <token>


# Response:


{
  "message": "Order placed successfully",
  "order_id": 3
}




## ✅ What You Have Now

# * Fully working **Cart API** (add, update, remove, view).
# * **Checkout API** → automatically creates **Order** (next part).
# * Auto **stock deduction** after order.
# * Clears cart on successful checkout.

