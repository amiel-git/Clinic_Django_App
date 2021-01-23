from django.db import models
from django import forms
from django.urls import reverse

class Patient(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact_number = models.IntegerField()
    birthday = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return f"{ self.first_name } { self.last_name }"
    
    def get_absolute_url(self):
        return reverse("patient:detail", kwargs={
                "pk": self.id
            })
    