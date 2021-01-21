from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_doctor = models.BooleanField(default=True)
    contact_number = models.PositiveIntegerField()
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
