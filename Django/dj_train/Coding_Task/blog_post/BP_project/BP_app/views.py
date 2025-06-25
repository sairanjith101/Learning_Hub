from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

def blog_post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Latest first
    return render(request, 'BP_app/post_list.html', {'posts': posts})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # set the logged-in user as author
            blog_post.save()
            return redirect('posts')  # redirect after successful post
    else:
        form = BlogPostForm()
    
    return render(request, 'BP_app/create_post.html', {'form': form})
