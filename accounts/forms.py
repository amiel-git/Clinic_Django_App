from django import forms
from django.contrib.auth.models import User
from accounts.models import StaffAdmin

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password']


class StaffForm(forms.ModelForm):

    class Meta():
        model = StaffAdmin
        fields = ('profile_picture',)