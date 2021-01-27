from django.urls import path
from patient import views

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

app_name = 'patient'

urlpatterns = [
    path('',staff_member_required(views.PatientsCreateView.as_view()),name='create'),
    path('list/',login_required(views.PatientsListView.as_view()),name='list'),
    path('<int:pk>/',login_required(views.PatientsDetailView.as_view()),name='detail'),
    path('update/<int:pk>/',staff_member_required(views.PatientsUpdateView.as_view()),name='update'),
    path('delete/<int:pk>/',staff_member_required(views.PatientsDeleteView.as_view()),name='delete'),
    
]
