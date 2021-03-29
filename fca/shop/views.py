from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password 
from .models import Contact,Appointment

# Create your views here.

def index(request):
    return render(request , 'shop/index.html')

def about(request):
    return render(request , 'shop/about.html')

def appointment(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        skype = request.POST.get('skype', '')
        number = request.POST.get('number', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        print(name, email, skype, number, date, time, subject, message)
        appoint = Appointment(name=name,email=email,skype=skype,number=number,date=date,time=time,subject=subject,message=message)
        appoint.save()
    return render(request,'shop/appointment.html')

def comingsoon(request):
    return render(request,'shop/comingsoon.html')

def contact(request):
    if request.method=="POST":
        name  = request.POST.get('name' , '')
        email = request.POST.get('email' , '')
        phone = request.POST.get('phone' , '')
        desc  = request.POST.get('desc' , '')
        print( name , email , phone , desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request , 'shop/contact.html')

def doctors(request):
    return render(request , 'shop/doctors.html')

def error(request):
    return render(request , 'shop/error.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/shoplogin/')

def measures(request):
    return render(request,'shop/measures.html')

def prevention(request):
    return render(request,'shop/prevention.html')

def shoplogin(request):
    if request.method == "POST":
        #Get the post Parameters
        uname=request.POST['uname']
        passw=request.POST['password']

        user=auth.authenticate(username=uname,password=passw)

        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect("/appointment/")
        else:
            msg="Username Or Password Incorrect"
            return render(request,'shop/shoplogin.html',{"msg":msg})
    else:
        if request.user.is_authenticated:
             return HttpResponseRedirect("/appointment/")
        else:
            return render(request,'shop/shoplogin.html')


def signup(request):
    if request.method == "POST":
        #Get the post Parameters
        uname=request.POST['uname']
        email=request.POST['email']
        pas=request.POST['password']
        passw=make_password(pas)

        if User.objects.filter(username=uname).exists():
           msg1="User Name Taken"
           #return HttpResponseRedirect("/signup/",{"msg":msg}) 
           return render(request,'shop/signup.html',{"msg1":msg1})
        elif User.objects.filter(email=email).exists():
           msg2="Email Taken"  
           return render(request,'shop/signup.html',{"msg2":msg2})
        else:
            user=User.objects.create(username=uname,email=email,password=passw)
            user.save()
        return HttpResponseRedirect("/shoplogin/")
    else:  
            return render(request,'shop/signup.html')


def symptoms(request):
    return render(request,'shop/symptoms.html')


def tips(request):
    return render(request,'shop/tips.html')






