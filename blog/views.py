from django.shortcuts import render
from .models import Post


def blog(request):

    posts = Post.objects.filter(
        published=True
    ).order_by('-created_at')

    return render(
        request,
        'blog/blog.html',
        {
            'posts': posts
        }
    )