from django.urls import path
from appointment import views

from django.contrib.admin.views.decorators import staff_member_required

app_name = 'appointment'

urlpatterns = [
    path('list/',views.AppointmentsListView,name='list'),
    path('',views.CreateAppointmentView, name='create'),
    path('update/<int:pk>',staff_member_required(views.AppointmentUpdateView.as_view()),name='update'),
    path('<int:pk>/',staff_member_required(views.AppointmentDetailView.as_view()),name='detail'),
    path('delete/<int:pk>',staff_member_required(views.AppointmentDeleteView.as_view()),name='delete'),
]
