from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

routers = DefaultRouter()
routers.register('books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(routers.urls))
]
