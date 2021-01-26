from django.urls import path
from appointment import views

app_name = 'appointment'

urlpatterns = [
    path('list/',views.AllAppointmentsListView.as_view(),name='list'),
    path('',views.CreateAppointmentView, name='create'),
    path('update/<int:pk>',views.AppointmentUpdateView.as_view(),name='update'),
    path('<int:pk>/',views.AppointmentDetailView.as_view(),name='detail'),
    path('delete/<int:pk>',views.AppointmentDeleteView.as_view(),name='delete'),
]
