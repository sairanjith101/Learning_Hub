from django.shortcuts import render
from .models import BlogPost

def blog_post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Latest first
    return render(request, 'BP_app/post_list.html', {'posts': posts})
