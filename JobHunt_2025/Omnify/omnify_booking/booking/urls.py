from django.urls import path
from .views import FitnessClassList, BookClass, ClientBookings

urlpatterns = [
    path('classes/', FitnessClassList.as_view()),
    path('book/', BookClass.as_view()),
    path('bookings/', ClientBookings.as_view()),
]