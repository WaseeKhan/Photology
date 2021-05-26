from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def homeView(request):
    cats = Category.objects.all()
    img = Photo.objects.all()
    heroImg = Hero.objects.all()
    data = {
        'heroImg': heroImg,
        'img': img,
        'cats': cats,

    }
    return render(request, 'picApp/home.html', data)


def ShowCatView(request, cid):
    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    img = Photo.objects.filter(cat=category)
    data = {
        'img': img,
        'cats': cats,
        'category': category,
    }
    return render(request, 'picApp/home.html', data)


def BlogView(request):
    blogs = Blog.objects.order_by('-created')
    top3 = Blog.objects.order_by('-created')[:3]
    mycats = Blog.objects.all()

    context = {
        'blogs': blogs,
        'top3': top3,
        'mycats': mycats,

    }
    return render(request, 'picApp/blog.html', context)


def BlogShowCategory(request,cat_id):
    cats = Category.objects.all()

    posts = Blog.objects.filter(category=cat_id)

    context = {
        'cats':cats,
        'posts':posts,
    }
    return render(request, 'picApp/blog.html', context)


def BlogRead(request, blog_id):
    blogs = Blog.objects.order_by('-created')
    top3 = Blog.objects.order_by('-created')[:3]
    read = Blog.objects.get(pk=blog_id)
    readPage = Blog.objects.filter(pk=blog_id)

    context = {'blogs': blogs, 'read': read, 'readPage': readPage, 'top3': top3}
    return render(request, 'picApp/blogRead.html', context)


def aboutView(request):
    return render(request, 'picApp/about.html', {})


def galleryView(request):
    return render(request, 'picApp/gallery.html', {})


def blogView(request):
    return render(request, 'picApp/blog.html', {})


def contactView(request):
    return render(request, 'picApp/contact.html', {})
