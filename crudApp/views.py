from django.shortcuts import render
from .models import Post


def homePage(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "index.html", {
        'posts': posts
    })


def aboutPage(request):
    title = "About"
    return render(request, "about.html", dict(title=title))
