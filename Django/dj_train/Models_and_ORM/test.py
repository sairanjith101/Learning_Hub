from django.urls import path
from . import views

urspattern = [
    path('start/', views.index(), name='first')
]