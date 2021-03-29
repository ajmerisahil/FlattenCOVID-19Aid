from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="ShopHome" ),
    path('about/', views.about , name="ShopAbout" ),
    path('appointment/',views.appointment,name="ShopAppointment"),
    path('comingsoon/',views.comingsoon,name="ShopComingsoon"),
    path('contact/', views.contact , name="ShopContact" ),
    path('doctors/', views.doctors, name="ShopDoctors"),
    path('error/', views.error, name="ShopError"),
    path('logout/',views.logout,name="ShopLogout"),
    path('shoplogin/',views.shoplogin,name="ShopLogin"),
    path('measures/',views.measures,name="ShopMeasures"),
    path('prevention/',views.prevention,name="ShopPrevention"),
    path('signup/',views.signup,name="ShopSignup"),
    path('symptoms/',views.symptoms,name="ShopSymptoms"),
    path('tips/',views.tips,name="ShopTips"),
    

]
