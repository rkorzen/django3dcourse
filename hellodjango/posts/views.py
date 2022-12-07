from django.shortcuts import render
from .models import Post
# Create your views here.

def posts_list(request):

    q = request.GET.get("title")
    before = request.GET.get("before")
    posts = Post.objects.all()
    if q:
        posts = posts.filter(title__icontains=q)
    
    if before:
        posts = posts.filter(created__lt=before)


# https://github.com/rkorzen/django3dcourse
        
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