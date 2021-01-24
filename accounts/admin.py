from django.contrib import admin
from accounts.models import StaffAdmin
from doctor.models import Doctor
from patient.models import Patient
from appointment.models import Appointment
# Register your models here.
admin.site.register(StaffAdmin)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)