from django.urls import pathgit 
from . import views

urspattern = [
    path('start/', views.index(), name='first')
]