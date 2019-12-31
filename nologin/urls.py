from django.contrib import admin
from django.urls import path, include
from nologin import views



app_name = "nologin"

urlpatterns = [
    path('', views.nologin, name = "nologin"),
    
    
    
]