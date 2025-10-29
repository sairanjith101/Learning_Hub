# models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


# 🧠 View Example 1 — Manual Filtering Using Query Parameters
# You can filter data manually inside your get_queryset() method:

# views.py
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer   # ✅ remove the square brackets

    def get_queryset(self):
        queryset = Post.objects.all()
        author_id = self.request.query_params.get('author')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        return queryset


# DRF filter backend version

# ✅ Install dependency (if not yet installed)

# pip install django-filter

# Then, in your settings.py, add:

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
}


# ✅ Full Example — DRF Filter Backend
# views.py

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Enable filtering using DRF’s filter backend
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'title']   # fields you can filter by


# ✅ Optional: Add More Features (search + ordering)

from rest_framework import filters

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'title']
    search_fields = ['title', 'content']       # ?search=django
    ordering_fields = ['title', 'author']      # ?ordering=title

