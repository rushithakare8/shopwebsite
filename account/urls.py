
from django.contrib import admin
from django.urls import path, include
from mywebsite import views
urlpatterns = [
    path("register", views.register, name='register'),
   
]
