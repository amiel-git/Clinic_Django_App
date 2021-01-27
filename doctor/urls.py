from django.urls import path
from doctor import views

from django.contrib.admin.views.decorators import staff_member_required

app_name = 'doctor'

urlpatterns = [
    path('list/',staff_member_required(views.Doctor_listview.as_view()),name='doctor_list'),
    path('<slug:pk>/',staff_member_required(views.Doctor_detailview.as_view()),name='doctor_detail'),
    path('',views.create_doctor_view,name='doctor_create'),
    path('delete/<slug:pk>/',staff_member_required(views.Doctor_deleteview.as_view()),name='doctor_delete'),
    path('update/<slug:pk>',staff_member_required(views.Doctor_updateview.as_view()),name='doctor_update'),
]
