from django.urls import path
from patient import views
app_name = 'patient'


urlpatterns = [
    path('',views.PatientsListView.as_view(),name='list'),
    path('create/',views.PatientsCreateView.as_view(),name='create'),
]
