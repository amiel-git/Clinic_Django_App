from django.urls import path
from doctor import views

app_name = 'doctor'

urlpatterns = [
    path('list/',views.Doctor_listview.as_view(),name='doctor_list'),
    path('<slug:pk>/',views.Doctor_detailview.as_view(),name='doctor_detail'),
    path('',views.create_doctor_view,name='register_doctor'),
    path('delete/<slug:pk>/',views.Doctor_deleteview.as_view(),name='doctor_delete'),
    path('update/<slug:pk>',views.Doctor_updateview.as_view(),name='doctor_update'),
]
