from django.db import models
from patient.models import Patient
from doctor.models import Doctor
from django.contrib.auth.models import User

from django.urls import reverse

class Appointment(models.Model):
    
    created_by = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null = True,
        related_name='appointments'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete = models.SET_NULL,
        related_name='appointments',
        null = True,
        blank=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        null = True,
        related_name='appointments'
    )

    created_on = models.DateTimeField(auto_now_add=True)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    description = models.CharField(max_length=500)
    is_paid = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name} - ID: {self.id}"
    

    def get_absolute_url(self):
        return reverse("appointment:detail", kwargs={"pk": self.pk})
    