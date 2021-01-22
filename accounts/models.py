from django.db import models
from django.contrib.auth.models import User



class StaffAdmin(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def get_absolute_url(self):
        return reverse("doctor:doctor_list")
    