from django.urls import path
from accounts import views
app_name = 'accounts'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.create_staff_view,name='create_staff'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')
]
