from django.contrib import admin
from django.urls import path,include
from cropapp import views


urlpatterns = [
    path('home/',views.home),
    path('contact/',views.contact),


]
 