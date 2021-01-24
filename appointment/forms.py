from django import forms
from appointment.models import Appointment

class AppointmentForm(forms.ModelForm):
    schedule_date = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    schedule_time = forms.TimeField(widget=forms.DateTimeInput(attrs={'type':'time'}))
    description = forms.CharField(widget=forms.Textarea())
    class Meta():
        
        model = Appointment
        fields = [
            'doctor',
            'patient',
            'schedule_date',
            'schedule_time',
            'is_paid',
            'is_complete',
            'price',
            'description',
        ]
