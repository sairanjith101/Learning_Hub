from django.shortcuts import render
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


# Checkout API (cart/views.py add)

from orders.models import Order, OrderItem  # we’ll create in Part 4
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions

class CheckoutViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        # Restrict checkout → Customers only
        if request.user.role != "CUSTOMER":
            raise PermissionDenied("Only customers can checkout")

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
            # Reduce stock
            item.product.stock -= item.quantity
            item.product.save()

        cart.items.all().delete()
        return Response({"message": "Order placed successfully", "order_id": order.id}, status=201)
