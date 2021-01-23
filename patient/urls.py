from django.urls import path
from patient import views

app_name = 'patient'

urlpatterns = [
    path('',views.PatientsCreateView.as_view(),name='create'),
    path('list/',views.PatientsListView.as_view(),name='list'),
    path('<int:pk>/',views.PatientsDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',views.PatientsUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.PatientsDeleteView.as_view(),name='delete'),
    
]
