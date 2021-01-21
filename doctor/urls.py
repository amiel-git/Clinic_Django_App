from django.urls import path
from doctor import views

app_name = 'doctor'

urlpatterns = [
    path('',views.Doctor_listview.as_view(),name='doctor_list'),
    path('<slug:pk>/',views.Doctor_detailview.as_view(),name='doctor_detail'),
    path('create/',views.create_doctor_view,name='register_doctor'),
]
