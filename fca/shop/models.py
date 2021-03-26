from django.db import models

# Create your models here.

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Appointment(models.Model):
    appt_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    skype = models.CharField(max_length=70, default="")
    number = models.CharField(max_length=70, default="")
    date = models.CharField(max_length=500, default="")
    time = models.CharField(max_length=500, default="")
    subject = models.CharField(max_length=500, default="")
    message = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
