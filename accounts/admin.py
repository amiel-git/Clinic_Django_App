from django.contrib import admin
from accounts.models import StaffAdmin
from doctor.models import Doctor
from patient.models import Patient
# Register your models here.
admin.site.register(StaffAdmin)
admin.site.register(Doctor)
admin.site.register(Patient)