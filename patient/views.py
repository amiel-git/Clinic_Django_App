from django.shortcuts import render

from patient.models import Patient
from patient.forms import PatientRegistrationForm

from django import forms
from django.views import generic, decorators


class PatientsListView(generic.ListView):

    model = Patient
    context_object_name = 'patients'

class PatientsCreateView(generic.CreateView):

    model = Patient
    form_class = PatientRegistrationForm
   
class PatientsDetailView(generic.DetailView):
    template_name = 'patient/patient_detail.html'
    context_object_name = 'patient_detail'
    model = Patient


class PatientsUpdateView(generic.UpdateView):

    model = Patient
    fields = [
            'first_name',
            'last_name',
            'email',
            'contact_number',
            'birthday',
            'profile_picture'
        ]


class PatientsDeleteView(generic.DeleteView):

    model = Patient