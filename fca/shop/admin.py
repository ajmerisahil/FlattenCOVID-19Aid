from django.contrib import admin

# Register your models here.
from .models import Contact,Appointment

admin.site.register(Contact)
admin.site.register(Appointment)