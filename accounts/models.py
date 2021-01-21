from django.db import models
from django.contrib.auth.models import User



class StaffAdmin(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username
    