from django.urls import path
from doctor import views

app_name = 'doctor'

urlpatterns = [
    path('create/',views.create_doctor_view,name='register_doctor'),
]
