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
   