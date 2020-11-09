from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


app_name = "user"

urlpatterns = [
    path('register/', views.register, name= "register"),
    path('login/', views.loginUser, name= "login"),
    path('logout/', views.logoutUser, name="logout"),
    path('password/', views.change_password, name='change_password'),
    path('account/', views.Account, name="account"),
    path('password/', views.change_password, name='change_password'),
    path('username/', views.change_username, name='change_username'),

    path('password_reset/', 
        PasswordResetView.as_view(template_name='password_reset.html'), 
        name='password_reset'),

    path('password_reset/done/', 
        PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
        name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
        name='password_reset_confirm'),

    path('password_reset_complete/', 
        PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
        name='password_reset_complete')
]