from django.shortcuts import render
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

# 2) Coupons / Discounts

from .models import Coupon
from .serializers import CouponSerializer
from rest_framework import viewsets

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAdminUser]
