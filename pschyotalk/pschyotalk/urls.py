from django.contrib import admin
from django.urls import path
from pschyotalk import views

urlpatterns = [
    path('', views.index1),
]
