from django.http import HttpResponse

def home(request):
    return HttpResponse("Hellow world!")

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home")
]