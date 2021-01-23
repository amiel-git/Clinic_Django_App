from django import forms
from patient.models import Patient

class PatientRegistrationForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta():
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'email',
            'contact_number',
            'birthday',
            'profile_picture'
        ]