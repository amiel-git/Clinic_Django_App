from django.shortcuts import render
from django.contrib.auth.models import User
from doctor.models import Doctor

from doctor.forms import DoctorForm
from accounts.forms import UserForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.views import generic

def create_doctor_view(request):
    user_form = UserForm()
    doctor_form = DoctorForm()
    context = {"user_form":user_form,"doctor_form":doctor_form}

    if request.method == "POST":
        user_form = UserForm(request.POST)
        doctor_form = DoctorForm(request.POST)

        if user_form.is_valid() and doctor_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            doctor = doctor_form.save(commit=False)
            doctor.user = user

            if 'profile_picture' in request.FILES:
                doctor.profile_picture = request.FILES['profile_picture']
            doctor.save()

            return HttpResponseRedirect(reverse('accounts:login'))

        else:
            return HttpResponse("Invalid form submission")

    return render(request,'doctor/register_doctor.html',context=context)


class Doctor_listview(generic.ListView):
    context_object_name = 'doctors'
    template_name = 'doctor/doctors_list.html'
    model = Doctor


class Doctor_detailview(generic.DetailView):
    template_name = 'doctor/doctors_detail.html'
    model = Doctor
    context_object_name = 'doctor_detail'