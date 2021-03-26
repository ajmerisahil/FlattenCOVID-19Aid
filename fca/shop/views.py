from django.shortcuts import render
from django.http import HttpResponse
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

def measures(request):
    return render(request,'shop/measures.html')

def prevention(request):
    return render(request,'shop/prevention.html')

def symptoms(request):
    return render(request,'shop/symptoms.html')

def tips(request):
    return render(request,'shop/tips.html')






