from django.shortcuts import render
from .models import Post
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(
        request,
        "posts/main.html",
        {"posts": posts}
    )

def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(
        request,
        "posts/details.html",
        {"post": post}
    )