from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('add/', views.add_application, name='add'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('userprofile/', views.user_profile, name='user_profile'),
    path('applications/', views.application_list, name='application_list'),
    path('applications/approve/<int:application_id>/', views.approve_application, name='approve_application'),
    path('applications/reject/<int:application_id>/', views.reject_application, name='reject_application'),
]