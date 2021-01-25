from django.shortcuts import render
from django.views import generic

from appointment.forms import AppointmentForm
from appointment.models import Appointment

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

class AllAppointmentsListView(generic.ListView):

    model = Appointment
    context_object_name = 'appointments'
    template_name = 'appointment/appointment_list.html'


def CreateAppointmentView(request):

    form = AppointmentForm()
    context = {'form':form}

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.save(commit=False)
            appointment.created_by = request.user
            appointment.save()

            return HttpResponseRedirect(reverse('appointment:list'))

        else:
            return HttpResponse(form.errors)

        
    return render(request,'appointment/create_appointment.html',context=context)


class AppointmentUpdateView(generic.UpdateView):

    template_name = 'appointment/create_appointment.html'
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
