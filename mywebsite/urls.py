from django.contrib import admin
from django.urls import path
from mywebsite import views

urlpatterns = [
    path("", views.index, name='mywebsite'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("shop", views.shop, name='shop'),
    path("automob", views.automob, name='automob'),
    path("electrician", views.electrician, name='electrician'),
    path("shoplogin", views.shoplogin, name='shoplogin'),
    path("registershop", views.registershop, name='registershop'),
    #path("", views.index, name='mywebsite')

]
