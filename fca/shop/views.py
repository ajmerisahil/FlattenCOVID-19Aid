from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request , 'shop/index.html')

def about(request):
    return render(request , 'shop/about.html')

def appointment(request):
    return render(request,'shop/appointment.html')

def comingsoon(request):
    return render(request,'shop/comingsoon.html')

def contact(request):
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






