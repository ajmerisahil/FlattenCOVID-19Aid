from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password 
from .models import Contact,Appointment,Hospital,Sanitization
from django.core.mail import send_mail
from django.conf import settings

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
        message="Dear {fname}, \n\n i would like to confirm your apointment with our Doctor at {date} at {time}. Please contact me with any questions and keep me informed if there should be any changes.\n\nThank-You Have a great day ! ".format(fname=name,date=date,time=time)
        send_mail("Confirmation of appointment" , 
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False)
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
        message="Dear {fname}, \n\n We appreciate you contacting us. one of our Representative will get back in touch with you soon! \n\nThank-You Have a great day ! ".format(fname=name)
        send_mail("Thank you for getting in touch !" , 
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False)
    return render(request , 'shop/contact.html')

def doctors(request):
    return render(request , 'shop/doctors.html')

def error(request):
    return render(request , 'shop/error.html')

def hospitalization(request):
    if request.method=="POST":
        name  = request.POST.get('name' , '')
        email = request.POST.get('email' , '')
        phone = request.POST.get('phone' , '')
        age = request.POST.get('age', '')
        date = request.POST.get('date','')
        hospital = request.POST.get('hospital','')
        desc= request.POST.get('desc' , '')
        print( name , email , phone , age , date ,hospital , desc)
        hospital = Hospital(name=name,email=email,phone=phone,age=age,date=date,hospital=hospital,desc=desc)
        hospital.save()
        message="Dear {fname}, \n\n your response has been recorded. our team will respond you as soon as possible. \n\n if you have any further changes in upcomming days than contact us Again. \n\nTHANK-YOU have a Great day !".format(fname=name)
        send_mail("Hospitalization" , 
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False)
    return render(request,'shop/hospitalization.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/shoplogin/')

def measures(request):
    return render(request,'shop/measures.html')

def prevention(request):
    return render(request,'shop/prevention.html')


def sanitization(request):
    if request.method=="POST":
        name  = request.POST.get('name' , '')
        email = request.POST.get('email' , '')
        phone = request.POST.get('phone' , '')
        address = request.POST.get('address', '')
        desc= request.POST.get('desc' , '')
        print( name , email , phone , address , desc)
        sanitize = Sanitization(name=name,email=email,phone=phone,address=address,desc=desc)
        sanitize.save()
        message="Dear {fname}, \n\n   Thanks for booking.  your request is confirmed for Sanitization service. our team will come to your respective address as soon as possible. \n\n if you have any Query than contact us again. \n\nTHANK-YOU have a Great day !".format(fname=name)
        send_mail("Sanitization Booked" , 
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False)
    return render(request,'shop/sanitization.html')


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





