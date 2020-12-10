from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
]