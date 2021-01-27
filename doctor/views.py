from django.shortcuts import render
from django.contrib.auth.models import User
from doctor.models import Doctor

from doctor.forms import DoctorForm
from accounts.forms import UserForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy

from django.views import generic
from extra_views import UpdateWithInlinesView, InlineFormSet

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
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


class Doctor_deleteview(generic.DeleteView):
    model = Doctor

    success_url = reverse_lazy('doctor:doctor_list')

class DoctorInline(InlineFormSet):
    model = Doctor
    fields = ('contact_number','profile_picture')

class Doctor_updateview(UpdateWithInlinesView):

    model = User
    inlines = [DoctorInline]
    fields = ('username','first_name','last_name','email')
    template_name = 'doctor/doctor_update.html'

    def get_success_url(self):
        return self.object.get_absolute_url()