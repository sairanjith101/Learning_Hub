from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import localtime
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer, BookingCreateSerializer

class FitnessClassList(APIView):
    def get(self, request):
        classes = FitnessClass.objects.all()
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)

class BookClass(APIView):
    def post(self, request):
        serializer = BookingCreateSerializer(data=request.data)
        if serializer.is_valid():
            class_id = serializer.validated_data['class_id']
            try:
                fitness_class = FitnessClass.objects.get(id=class_id)
            except FitnessClass.DoesNotExist:
                return Response({'error': 'Fitness class not found'}, status=404)

            if fitness_class.available_slots <= 0:
                return Response({'error': 'No slots available'}, status=400)

            booking = Booking.objects.create(
                fitness_class=fitness_class,
                client_name=serializer.validated_data['client_name'],
                client_email=serializer.validated_data['client_email']
            )
            fitness_class.available_slots -= 1
            fitness_class.save()

            return Response(BookingSerializer(booking).data, status=201)

        return Response(serializer.errors, status=400)

class ClientBookings(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email parameter is required'}, status=400)
        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)