from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Posts

def posts(request):
    #return HttpResponse("<h1>here all the posts will be displayed</h1>")
    blogs = Posts.objects.all()
    context = {
        "user" : "Ghana's Work base",
        "posts": blogs
    }
    return render(request, 'blog/index.html',context)

def details(request, id):
    post = Posts.objects.get(id=id)
    context ={
        'post':post
    }
    return render(request, 'blog/details.html',context)