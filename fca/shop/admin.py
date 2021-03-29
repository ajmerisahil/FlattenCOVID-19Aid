from django.contrib import admin

# Register your models here.
from .models import Contact,Appointment,Hospital,Sanitization

admin.site.register(Contact)
admin.site.register(Appointment)
admin.site.register(Hospital)
admin.site.register(Sanitization)