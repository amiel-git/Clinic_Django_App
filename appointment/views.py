from django.shortcuts import render
from django.views import generic

from appointment.forms import AppointmentForm
from appointment.models import Appointment

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from appointment.models import Appointment
from doctor.models import Doctor

@login_required
def AppointmentsListView(request):

    if request.user.is_staff:
        appointments = Appointment.objects.all()
    
    else:
        doctor = Doctor.objects.get(user_id=request.user.id)
        appointments = Appointment.objects.filter(doctor_id = doctor.id)
    
    context = {
        'appointments':appointments,
    }

    return render(request,'appointment/appointment_list.html',context=context)


@staff_member_required
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


class AppointmentDetailView(generic.DetailView):

    model = Appointment
    template_name = 'appointment/appointment_detail.html'
    context_object_name = 'appointment_detail'



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


class AppointmentDeleteView(generic.DeleteView):

    model = Appointment
    success_url = reverse_lazy('appointment:list')
