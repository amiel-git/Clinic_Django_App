from django.shortcuts import render
from django.views import generic
from accounts import forms

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.decorators import login_required


def index(request):

    return render(request,'core/index.html')


def create_staff_view(request):
    user_form = forms.UserForm
    staff_form = forms.StaffForm
    staff = request.user.is_staff
    context = {'user_form':user_form,'staff_form':staff_form, 'is_staff':staff }

    #Only staff can register doctors
    if request.user.is_staff == False:
        return HttpResponseRedirect(reverse('accounts:index'))

    if request.method == "POST":

        user_form = forms.UserForm(request.POST)
        staff_form = forms.StaffForm(request.POST)

        if user_form.is_valid() and staff_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.is_staff = True
            user.save()

            staff = staff_form.save(commit=False)
            staff.user = user
            if 'profile_picture' in request.FILES:

                staff.profile_picture = request.FILES['profile_picture']
                staff.save()
            
            return HttpResponseRedirect(reverse('accounts:login'))

        else:
            return HttpResponse(user_form.errors)

    return render(request,'core/register.html',context=context)


def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('accounts:index'))
            
            else:
                return HttpResponse("User is inactive")
        
        else:
            raise ValueError("Incorrect Credentials")

    return render(request,'core/login.html')


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))