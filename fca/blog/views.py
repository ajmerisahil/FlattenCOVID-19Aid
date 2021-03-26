from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost , Comment

# Create your views here.

def index(request):
    myposts= Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/blog.html', {'myposts': myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',{'post':post})


def blogdetail(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        comments = Comment(name=name, email=email, phone=phone, desc=desc)
        comments.save()
    return render(request , 'blog/blogdetail.html')
