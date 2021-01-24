from django.urls import path
from appointment import views

app_name = 'appointment'

urlpatterns = [
    path('list/',views.AllAppointmentsListView.as_view(),name='list'),
    path('',views.CreateAppointmentView, name='create'),
]
