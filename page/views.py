from page.models import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def page(request, slug):
    page = get_object_or_404(Page, url=slug )
    return render(request, 'pages/page.html', {'page' : page})

def blog_detail(request, slug):
    blog_post = get_object_or_404(Post, url=slug )
    return render(request, 'pages/page.html', {'page':blog_post})

def blog(request):
    blog_posts = Post.objects.all()
    return render(request, 'pages/blog.html', {'blog_posts':blog_posts})